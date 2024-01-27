# Importando as bibliotecas
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns

from functionalities.request_data import *
from functionalities.plot_grafico_ import *



def predict_sales(store_id):

  df = collections_request(store_id)

  # Transformando data para datetime
  df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d')

  # Criando o DataFrame Holiday

  # Public Holiday
  public_holiday=df[df['StateHoliday']=='a']

  public = pd.DataFrame({
    'holiday': 'public',
    'ds': public_holiday['Date'],
    'lower_window': 0,
    'upper_window': 0,
  })

  # Easter Holiday
  easter_holiday=df[df['StateHoliday']=='b']

  easter = pd.DataFrame({
    'holiday': 'easter',
    'ds': easter_holiday['Date'],
    'lower_window': 0,
    'upper_window': 0,
  })

  # Christmas Holiday
  christmas_holiday=df[df['StateHoliday']=='c']

  christmas = pd.DataFrame({
    'holiday': 'christmas',
    'ds': christmas_holiday['Date'],
    'lower_window': -1,
    'upper_window': 0,
  })

  # School Holiday
  school_holiday=df[df['SchoolHoliday']==1]

  school = pd.DataFrame({
    'holiday': 'school',
    'ds': school_holiday['Date'],
    'lower_window': 0,
    'upper_window': 0,
  })

  holidays=pd.concat((public, easter, christmas, school))

  # Ajustando os parâmetros nos moldes do prophet
  df_prophet = df.reset_index() \
      .rename(columns={'Date':'ds',
                      'Sales':'y'})

  # Treinando o modelo com os dados de treino
  model = Prophet(holidays=holidays, weekly_seasonality=True)
  model.fit(df_prophet)

  future = model.make_future_dataframe(periods=90)
  future = future.tail(90)

  forecast = model.predict(future)


  # Plotando o gráfico de Predição
  forecast['ds'] = pd.to_datetime(forecast['ds'])
  total, mean, (max_day, max_sale) = plot_grafico_prediction(model,forecast,store_id)

  return total, mean, (max_day, max_sale)


