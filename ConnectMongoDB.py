from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://deevasbohra_db_user:Microsoft~123456@cluster0.2qsnd79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
#try:
   # client.admin.command('ping')
   # print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
  #  print(e)

db = client['DeeshnaTriangleDB']
collection = db['Triangles']
#document = {"13" : "Equilateral Rightangle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"11": "Equilateral AcuteAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"12": "Equilateral ObtuseAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"21": "Isosceles AcuteAngleAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"22": "Isosceles ObtuseAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"23": "Isosceles RightAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"31": "Scalene AcuteAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"32": "Scalene ObtuseAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"33": "Scalene Rightangle Triangle"}
#insert_document = collection.insert_one(document)

for Triangles in collection.find():
    print(Triangles)
#Triangles = collection.find_one({11 : "Equilateral AcuteAngle Triangle"})
#print(Triangles)

#print(insert_document.inserted_id)
client.close()

#from pymongo import MongoClient

#client = MongoClient('mongodb+srv://deevasbohra_db_user:Microsoft~123456@cluster0.2qsnd79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
#db = client['DeeshnaTriangleDB']
#collection = db['Triangles']
#document = collection.find_one()