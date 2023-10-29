from pymongo_get_database import get_database


dbname = get_database()
collection_name = dbname["aluno"]


# item_3 = {
#     "_id" : 3,
#     "nome": "Gustav Keller",
#     "idade": 19,
#     "email": "gustav.keller@gmail.com",
#     "senha" : "maskeiko",
# }
# collection_name.insert_one(item_3)

while(1):
    print("1 - Inserir\n2 - Ler\n3 - Atualizar\n4 - Deletar\n5 - Encerrar")
    option = 1
    
    try:
        option = int(input("Digite a opção: "))
        if 0 > option or option > 4:
            raise OverflowError
    except (ValueError, TypeError, OverflowError):
        print("Essa não é uma opção válida")
        
    match option:
        case 1: #Inserir
            greatest_id = 0
            item_details = collection_name.find()
            
            #find greatest id
            for item in item_details:
                if greatest_id < item['_id']:
                    greatest_id = item['_id']
                    
            print(greatest_id)

            
        

        # case 2:
        

        # case 3:
        
    
        # case 4:
        
        # case _:

