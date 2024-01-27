
import pandas as pd #Leitura dos arquivos
from pymongo import timeout
import numpy as np
from pymongo import MongoClient

def collections_request(store_id) :

    input_list = []
    nome_bd = 'Sales-Forecasting_' 

    client = MongoClient('localhost', 27017)

    db = client[nome_bd]

    collection = db.get_collection(f"Store-{store_id}")

    cursor = collection.find({})

    store_id = cursor[0]['store_id']


    for document in cursor:
        mean = document['mean_month']
        year = document['year']
        month = document['month']
        for daily in document['logs']:
            input_dic = {'ID_store':store_id,'Open':daily['Open'],'StateHoliday':daily['StateHoliday'],'SchoolHoliday':daily['SchoolHoliday'],
                    'Date':f"{year}-{month}-{daily['Day']}",'Sales':daily['Sales'] }
            input_list.append(input_dic)
        
    df = pd.DataFrame.from_records(input_list).sort_values(by='Date').reset_index().drop("index",axis=1)
    return df