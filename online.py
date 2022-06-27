from http import client
from pymongo import MongoClient
import pymongo
import pprint  
def database():

    conn_str="mongodb+srv://arm:123321@moves.yxjpv.mongodb.net/?retryWrites=true&w=majority"
    client=MongoClient(conn_str)

    try:
        conn = MongoClient()
        print("Connected successfully!!!")
    except:  
        print("Could not connect to MongoDB") 
    
    return client




def set_move(client):
    db=client["myFirstDatabase"]
    #print('this is db : =====>',db)
    moves=db["moves"]
    moves.insert_one({"from":"ahmed","to":"12"})
    ff=moves.find()
    print( ff)
#    print(moves)
#    return moves
#    
#
#def get_move(moves):
#   for i in moves.find()
#
#  
#    move= moves[-1]
#    return move
## 
## def sendmove(move):
set_move(database())
#
   # collection.insert_one([{"from":humenmove[0]+humenmove[1],"to":humenmove[2]+humenmove[3]}])
#