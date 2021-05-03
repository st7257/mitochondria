import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://steven:j7257197@cluster0.gjjwq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.get_database('Data')
items = db.Profiles

length = 0
for x in items.find({"_id":323269402588086283}, {"Pulls": 1}):
  print(x)
  print(x["Pulls"])
  length = len(x["Pulls"])
  for item in x["Pulls"]:
      if item == ["Diluc", "10"]:
          x["Pulls"].remove(item)
          break
if len(x["Pulls"]) != length:
    print("Removed")
print(x["Pulls"]) 
