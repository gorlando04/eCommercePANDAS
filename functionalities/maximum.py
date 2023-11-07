
from functionalities.auxiliar import *
from createDB.db_var import db
from functionalities.plot_grafico_ import *


def maxCustomers(store_id):


    
    collection = db.get_collection(f"Store-{store_id}")
    
    if not store_exists(collection):
        return None
    
    cursor = collection.aggregate([
    { "$unwind" :'$logs'},
    { "$sort": { "logs.Customers": -1 } },
    { "$group": {
        "_id": "$_id",
        "Year": {"$first": "$year"},
        "Month": {"$first": "$month"},
        "Day": { "$first": "$logs.Day" },
        "MaxCustomers": { "$max":"$logs.Customers"}
    }}
])
    
    order = {}
    order2 = {}
    
    for i in [2013,2014,2015]:
        for j in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            if i == 2015 and int(j) > 7:
                break
            
            order[f"{i}-{j}"] = -1
            order2[f"{i}-{j}"] = -1
        
    for i in cursor:
        order[f"{i['Year']}-{i['Month']}"] = i['MaxCustomers']
        order2[f"{i['Year']}-{i['Month']}"] = int(i['Day'])
    
    x = list(order.values())
    y = list(order.keys())
    days = list(order2.values())

    title = f"Max Customers for Store-{store_id}"
    plot_grafico(x,y,title,True,days)



def maxSales(store_id):

    collection = db.get_collection(f"Store-{store_id}")
    
    if not store_exists(collection):
        return None

    cursor = collection.aggregate([
    { "$unwind" :'$logs'},
    { "$sort": { "logs.Sales": -1 } },
    { "$group": {
        "_id": "$_id",
        "Year": {"$first": "$year"},
        "Month": {"$first": "$month"},
        "Day": { "$first": "$logs.Day" },
        "MaxSales": { "$max":"$logs.Sales"}
    }}
])
    
    order = {}
    order2 = {}
    
    for i in [2013,2014,2015]:
        for j in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            if i == 2015 and int(j) > 7:
                break
            
            order[f"{i}-{j}"] = -1
            order2[f"{i}-{j}"] = -1
        
    for i in cursor:
        order[f"{i['Year']}-{i['Month']}"] = i['MaxSales']
        order2[f"{i['Year']}-{i['Month']}"] = int(i['Day'])
    
    x = list(order.values())
    y = list(order.keys())
    days = list(order2.values())

    title = f"Max Sales for Store-{store_id}"
    plot_grafico(x,y,title,True,days)