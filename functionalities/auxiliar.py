
def store_exists(collection):
    try:
        _ = collection.find({})[0]
        return True
    except:
        print("Loja não existe")
        return False

# Query com pymongo
def get_document(q_param,col):
    return col.find(q_param)[0]
    

def update_document(q_param,value,collection):

    collection.update_one(q_param,{"$set":value})