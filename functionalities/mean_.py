from functionalities.auxiliar import *
from createDB.db_var import db
from functionalities.plot_grafico_ import *

def meanCustomers(store_id):


    
    collection = db.get_collection(f"Store-{store_id}")
    
    if not store_exists(collection):
        return None
    
    cursor = collection.aggregate([
    { "$unwind" :'$logs'},
    { "$group": {
        "_id": "$_id",
        "mean_cust": { "$avg":"$logs.Customers"},
    }}
    ])

    order = {}
    
    for i in [2013,2014,2015]:
        for j in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            if i == 2015 and int(j) > 7:
                break
            
            order[f"{i}-{j}"] = -1
        
    for i in cursor:
        year = get_document({'_id':i['_id']},collection)['year']
        month = get_document({'_id':i['_id']},collection)['month']
        order[f"{year}-{month}"] = i['mean_cust']
    
    x = list(order.values())
    y = list(order.keys())

    title = f"Média de Clientes para a loja {store_id}"
    plot_grafico(x,y,title)


def meanSales(store_id):
    

    collection = db.get_collection(f"Store-{store_id}")
    
    if not store_exists(collection):
        return None
    
    cursor = collection.find({})
    
    order = {}
    
    for i in [2013,2014,2015]:
        for j in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            if i == 2015 and int(j) > 7:
                break
            
            order[f"{i}-{j}"] = -1
        
    for i in cursor:
        order[f"{i['year']}-{i['month']}"] = i['mean_month']
    
    x = list(order.values())
    y = list(order.keys())

    title = f"Média de Vendas para a loja {store_id}"
    plot_grafico(x,y,title)
