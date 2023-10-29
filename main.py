from pymongo_get_database import get_database


dbname = get_database()
collection_name = dbname["aluno"]

item_3 = {
    "_id" : 3,
    "nome": "Gustav Keller",
    "idade": 19,
    "email": "gustav.keller@gmail.com",
    "senha" : "maskeiko",
}
collection_name.insert_one(item_3)

while(1):
    print("1 - Inserir\n2 - Ler\n 3 - Atualizar\n 4 - Deletar")
    
    try:
        option = int(input("Digite a opção: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    match option:
        case 1:
        

        case 2:
        

        case 3:
        
    
        case 4:
        


