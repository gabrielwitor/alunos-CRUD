# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
 
# Retrieve a collection named "aluno" from database
collection_name = dbname["aluno"]
 
item_details = collection_name.find()

for item in item_details:
    # This does not give a very readable output
    # print(item)
    print(f"Nome: {item['nome']} | Email: {item['email']}")
    
