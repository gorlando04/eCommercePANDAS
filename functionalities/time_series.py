# Importando as bibliotecas
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns

from functionalities.request_data import *

df = pd.read_csv('', low_memory=False)

# Variável que receberá o input da seleção da loja do usuário
i = 1

# Selecionando os dados apenas de uma loja
df = df.loc[df.Store == i]

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

fig, ax = plt.subplots(figsize=(10, 5))
model.plot(forecast,uncertainty=True,  ax=ax)
ax.set_xbound(lower=pd.Timestamp('2015-07-31'), 
              upper=pd.Timestamp('2015-08-30'))
ax.set_xlabel('Data')
ax.set_ylabel('Vendas')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plot = plt.suptitle(f'Previsão de Vendas Loja {i}')
plt.show()

# Cálculo de Métricas

# Substituindo os valores negativos por zero
forecast['yhat'] = forecast['yhat'].clip(lower=0)

total = forecast['yhat'].sum()

mean = forecast['yhat'].mean()

forecast_sorted = forecast.sort_values(by='yhat')
max_day, max_sale = forecast_sorted[['ds', 'yhat']].iloc[-1]

print(f'Total de Vendas: {total:.0f}')
print(f'Média de Vendas: {mean:.2f}')
print(f'Dia de Maior Venda:', max_day.date(), f', Vendas: {max_sale:.0f}')