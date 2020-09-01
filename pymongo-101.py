import pymongo
from pymongo import MongoClient

cluster = MongoClient("") # Insert MongoDB URL and replace <password> with database password
db = cluster["test"] # Name of database
collection = db["test"]

# Define dictionary, aka post or document
post1 = {
    "_id": 0, # _id will be randomized if not specifically given
     "name": "Nathan",
     "role": "dev"
}

post2 = {
    "_id": 1,
    "name": "Meagan",
    "role": "artist"
}

# Add dictionary to collection
# collection.insert_one(post)

# Add multiple dictionaries
collection.insert_many([post1, post2])

# Get all dictionaries by field
results1 = collection.find({"name": "Meagan"}) # Can also be replaced with regex - to search multiple fields at once, add , then another field

# This will return an object ID - use for loop to print out details
# print(results)

for result in results1:
    # prints id of result matching the dictionary and filter from results = collection.find()
    print(result["_id"])
    
# Get one dictionary by field - strongly recommended to search by id
results2 = collection.find_one({"_id": 0 })
print(results2)

# Get all dictionaries
results3 = collection.find({})
for x in results3:
    print(x)
    
# Update dictionary
result4 = collection.update_one({"_id": 0 }, {"$set": {"role": "lead dev"}})
# $set: can be used to create a new field
# collection.update_many can update multiple

# count how many documents fit criteria
post_count = collection.count_documents({})
print(post_count) # returns 2

# Delete dictionary by specific field
results5 = collection.delete_one({"_id": 0})
# use collection.delete_many() to delete multiple entries by field or leave {} blank to delete all
print(post_count) # returns 1