import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_grafico(x, y,title,day=False,days=None):

    
    plt.rcParams["figure.figsize"] = (20,8)
    
    
    # Pega as informações do cliente
    height = x
    bars = y

    for i in range(len(bars)):

        bars[i] = bars[i][2:]
        
    y_pos = np.arange(len(bars))

    

    plt.plot(y_pos,height,color = 'r',marker='o',markeredgecolor='black',markerfacecolor='black')

    if days:
        # zip joins x and y coordinates in pairs
        idx = 0
        for x,y in zip(y_pos,height):
        
            label = f"D:{days[idx]}"
            idx += 1
            plt.annotate(label, # this is the text
                         (x,y), # these are the coordinates to position the label
                         textcoords="offset points", # how to position the text
                         xytext=(0,10), # distance from text to points (x,y)
                         ha='center') # horizontal alignment can be left, right or center

        # Cria os nomes para o eixo X, o título, o label para o eixo Y e a legenda dos gráficos
    plt.xticks(y_pos, bars)
    plt.title(f"{title}")
    plt.ylabel("Quantidade")

    plt.grid()

 
    
    plt.show()

    plt.savefig('imgs/return.png')
    plt.clf()


def plot_grafico_comparacao(x1,y1,x2,title,store_id,store_type):


    plt.rcParams["figure.figsize"] = (20,8)
    

    bars = y1

    for i in range(len(bars)):

        bars[i] = bars[i][2:]
        
    y_pos = np.arange(len(bars))

    

    plt.plot(y_pos,x1,color = 'r',label=f'Store-{store_id}',marker='o',markeredgecolor='black',markerfacecolor='black')

    plt.plot(y_pos,x2,color = 'b',label=f'{store_type} store_type',marker='o',markeredgecolor='black',markerfacecolor='black')
   
        # Cria os nomes para o eixo X, o título, o label para o eixo Y e a legenda dos gráficos
    plt.xticks(y_pos, bars)
    plt.title(f"{title}")
    plt.ylabel("Quantidade")

    plt.grid()
    plt.legend()

 
    
    plt.show()

    plt.savefig('imgs/return.png')
    plt.clf()


def plot_grafico_prediction(model,forecast,i):


    fig, ax = plt.subplots(figsize=(20, 8))
    model.plot(forecast,uncertainty=True,  ax=ax)

    ax.set_xbound(lower=pd.Timestamp('2015-07-31'), 
                upper=pd.Timestamp('2015-08-30'))
    ax.set_xlabel('Data')
    ax.set_ylabel('Vendas')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right',fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='right',fontsize=12)
    plot = plt.suptitle(f'Previsão de Vendas Loja {i}')
    plt.show()

    plt.savefig('imgs/return.png')
    ax.clear()
    plt.clf()

    # Cálculo de Métricas

    # Substituindo os valores negativos por zero
    forecast['yhat'] = forecast['yhat'].clip(lower=0)

    total = forecast['yhat'].sum()

    mean = forecast['yhat'].mean()

    forecast_sorted = forecast.sort_values(by='yhat')
    max_day, max_sale = forecast_sorted[['ds', 'yhat']].iloc[-1]



    return total, mean, (max_day.date(),max_sale)
