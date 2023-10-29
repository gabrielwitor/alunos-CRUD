from pymongo_get_database import get_database


dbname = get_database()
collection_name = dbname["aluno"]


while(1):
    print("1 - Inserir\n2 - Ler\n3 - Atualizar\n4 - Deletar\n5 - Encerrar")
    option = 0
    
    try:
        option = int(input("Digite a opção: "))
        if 0 > option or option > 5:
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
                    
            name = input("Digite o nome do aluno: ")
            age = int(input("Digite a idade do aluno: "))
            email = input("Digite o email do aluno: ")
            password = input("Digite a senha do aluno: ")
            
            item = {
                "_id" : greatest_id+1,
                "nome": name,
                "idade": age,
                "email": email,
                "senha" : password,
            }
            collection_name.insert_one(item)

        case 2:
            item_details = collection_name.find()
            for item in item_details:
                print(f"Id: {item['_id']} | Nome: {item['nome']} | Idade: {item['idade']} | Email: {item['email']}\n")
        
        case 3:
            
            try:
                id_to_update = int(input("Digite o id do aluno que deseja modificar: "))
            except (ValueError, TypeError):
                print("Essa não é uma opção válida")
                
            name = input("Digite o nome do aluno: ")
            age = int(input("Digite a idade do aluno: "))
            email = input("Digite o email do aluno: ")
            password = input("Digite a senha do aluno: ")
            
            filter = filter = { '_id': id_to_update }
            
            item = { "$set": {
                "nome": name,
                "idade": age,
                "email": email,
                "senha" : password,
            } } 
            collection_name.update_one(filter, item)
            
        case 4:
            try:
                id_to_delete = int(input("Digite o id do aluno que deseja deletar: "))
            except (ValueError, TypeError):
                print("Essa não é uma opção válida")
                
            collection_name.delete_one( { "_id": id_to_delete } )
        
        case 5:
            break

