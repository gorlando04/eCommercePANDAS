from functionalities.auxiliar import *
from createDB.db_var import db
from functionalities.plot_grafico_ import *


def compareMeanSales(store_id_):

    store_id = int(store_id_)
    
    collection = db.get_collection(f"Store-{store_id}")
    
    if not store_exists(collection):
        return None
    
    
    collection = db.get_collection(f"Stores")

    

    q = {"stores": {"$elemMatch": {"Store":store_id}}}

    cursor = collection.find(q)

    print(store_id)
    stores_id = cursor[0]['stores']
    store_type = cursor[0]['store_type']

    N = len(stores_id) - 1
    
    order_1 = {}
    order_2 = {}
    
    for i in [2013,2014,2015]:
        for j in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            if i == 2015 and int(j) > 7:
                break
            
            order_1[f"{i}-{j}"] = -1
            order_2[f"{i}-{j}"] = -1
        
    for i in order_2:
            collection_store = None
            sum_mean = 0

            year = i[:4]
            month = i[5:7]
            for j in stores_id:
                id = j['Store']
                temp_col = db.get_collection(f"Store-{id}")
                if id != store_id:

                    sum_mean += temp_col.find({'month':month,'year':year})[0]['mean_month']
                    del temp_col
                else:
                    order_1[i] = temp_col.find({'month':month,'year':year})[0]['mean_month']
                    

            order_2[i] = sum_mean / N
                

                
        
    x = list(order_1.values())
    y = list(order_1.keys())

    title = f"Média de Vendas loja do tipo: {store_type} x Média de Venda loja {store_id}"
    

    x2 = list(order_2.values())

    plot_grafico_comparacao(x,y,x2,title,store_id,store_type)
