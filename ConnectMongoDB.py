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
#document = {"ResultKey" : "13", "OutcomeResult" : "Equilateral Rightangle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "11", "OutcomeResult" : "Equilateral AcuteAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "12", "OutcomeResult" : "Equilateral ObtuseAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "21", "OutcomeResult" : "Isosceles AcuteAngleAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "22", "OutcomeResult" : "Isosceles ObtuseAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "23", "OutcomeResult" : "Isosceles RightAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "31", "OutcomeResult" : "Scalene AcuteAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "32", "OutcomeResult" : "Scalene ObtuseAngle Triangle"}
#insert_document = collection.insert_one(document)
#document = {"ResultKey" : "33", "OutcomeResult" : "Scalene Rightangle Triangle"}
#insert_document = collection.insert_one(document)

#for Triangles in collection.find():
  #  print(Triangles)
Triangles = collection.find_one({"ResultKey" : "11"})
#ResultOutcome = collection.find_one({"11" : "Equilateral AcuteAngle Triangle"})

#if Triangles["11"] == "Equilateral AcuteAngle Triangle":
print(Triangles["OutcomeResult"])

#for Triangles in collection.find({}, {"11": 1 }):
   # ResultOutcome = Triangles.values()
 #   print(Triangles)

#print(insert_document.inserted_id)
client.close()

#from pymongo import MongoClient

#client = MongoClient('mongodb+srv://deevasbohra_db_user:Microsoft~123456@cluster0.2qsnd79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
#db = client['DeeshnaTriangleDB']
#collection = db['Triangles']
#document = collection.find_one()