import pymongo
 
 
client = pymongo.MongoClient("mongodb+srv://arm:123321@moves.yxjpv.mongodb.net/?retryWrites=true&w=majority")
 
# Database Name
db = client["myFirstDatabase"]
 
# Collection Name
col = db["moves"]
 
x = col.find()
 
for data in x:
    print(data)