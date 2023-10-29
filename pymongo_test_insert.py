# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["aluno"]

counter = 0

item_1 = {
    "_id" : counter,
    "nome": "Gabriel Witor",
    "idade": 19,
    "email": "witor.alm@gmail.com",
    "senha" : "123456"
}

item_2 = {
    "_id" : counter+1,
    "nome": "Rafael Tomaz",
    "idade": 17,
    "email": "rafaeltomaz@gmail.com",
    "senha" : "01234"
}

collection_name.insert_many([item_1,item_2])


item_3 = {
    "_id" : counter+2,
    "nome": "Gustav Keller",
    "idade": 19,
    "email": "gustav.keller@gmail.com",
    "senha" : "maskeiko",
}
collection_name.insert_one(item_3)