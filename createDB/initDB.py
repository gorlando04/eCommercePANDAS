from pymongo import MongoClient #Conexão com MongoDB
import pprint #Mostrar informações dos dados do banco de dados
import pandas as pd #Leitura dos arquivos
from pymongo import timeout
import numpy as np


client = MongoClient('localhost', 27017)
#Nome do banco de dados
nome_bd = 'Sales-Forecasting_' 

db = client[nome_bd]


#Pega o nome dos arquivos e remove o .csv deles
import os

mylist = os.listdir("/PANDAS/datasets")
dic_files = {}
for file in mylist:
    if not file.startswith("test"):
        aux = file.split(".")[0]
        dic_files[aux] = pd.read_csv(f"/PANDAS/datasets/{file}")

# Verificando se todos os datasets tem mais de 0 instâncias

final_dic = dic_files.copy()
for i in dic_files:

    if dic_files[i].shape[0] == 0:
        del final_dic[i]


final_dic['store'].loc[final_dic['store']['CompetitionDistance'].isna(),'CompetitionDistance'] = int(1e5)


stores = db.Stores


main_fdata = []

for i in final_dic['store']['StoreType'].unique():
    d = {'store_type':i, 'stores': []}
    main_fdata.append(d)

d = {'c':0,'a':1,'d':2,'b':3}


columns = final_dic['store'].columns

rows,cols = final_dic['store'].shape


for index, row in final_dic['store'].iterrows():
        fdata = {}
        store_type = 'a'
        for i in range(cols):
                if not columns[i] == 'StoreType':
                    fdata[columns[i]] = row[columns[i]]
                else:
                    store_type = row[columns[i]]
        main_fdata[d[store_type]]['stores'].append(fdata)

with timeout(100):
    stores.insert_many(main_fdata)



# Adiciona a coluna ANO-MES
df = final_dic['train'].copy()
df.loc[:,"Year"] = df['Date'].str.slice(0,4)
df.loc[:,"Month"] = df['Date'].str.slice(5,7)
df.loc[:,"Day"] = df['Date'].str.slice(8,10)


store_collections = []

for store_id in df['Store'].unique():
    
    stores = db.get_collection(f"Store-{store_id}")
    store_collections.append(stores)


main_fdata = []
dic_aux = {}
import copy

years = np.sort(df['Year'].unique())
months = np.sort(df['Month'].unique())
dic_indexes = 0
for year in years:
    for month in months:
        if year == '2015' and int(month) > 7:
            break
        d = {'store_id':-1,'year':year,'month':month,'logs': [] , 'mean_month':-1}
        dic_aux[f'{year}-{month}']= dic_indexes
        dic_indexes += 1
        main_fdata.append(d)


columns = df.columns

rows,cols = df.shape

N = len(store_collections)
import time
index_a = 0
t0 = time.time()

for store_id in df['Store'].unique():

    # O que será inserido.
    main_fdata2 = copy.deepcopy(main_fdata)
    df_aux = df[df['Store'] == store_id] # Linhas que são da loja com ID store_id

    for i in main_fdata2:
        i['store_id'] = int(store_id)

    year = '2013'
    month = '01'
    for index, row in df_aux.iterrows():
            fdata = {}
            
            for i in range(cols):
                    if columns[i] in ['Sales','Customers', 'Open','Promo','StateHoliday','SchoolHoliday','Day']:
                        try:
                            fdata[columns[i]] = row[columns[i]]
                        except:
                            fdata[columns[i]] = row[columns[i]]
                    elif columns[i] == 'Year':
                        year = row[columns[i]]
                    elif columns[i] == 'Month':
                        month = row[columns[i]]
            main_fdata2[dic_aux[f"{year}-{month}"]]['logs'].append(fdata)
    with timeout(100):
        store_collections[store_id-1].insert_many(main_fdata2)
    print(f"\r{index_a}/{N} ({(time.time()-t0):.3f} s)" , end=' ')
    index_a += 1

def update_document(q_param,value,collection):

    collection.update_one(q_param,{"$set":value})

N = len(store_collections)
import time
index_a = 0
t0 = time.time()

for collection in store_collections:
    for document in collection.aggregate([
        { "$unwind": "$logs" },
        { "$group" : { "_id": "$_id", "avgMonth" : {  "$avg" : "$logs.Sales" } } }
    ]):
        q_param = {'_id':document['_id']}
        value = {'mean_month':document['avgMonth'] }
        update_document(q_param,value,collection)
    print(f"\r{index_a}/{N} ({(time.time()-t0):.3f} s)" , end=' ')
    index_a += 1