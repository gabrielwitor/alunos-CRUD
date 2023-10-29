

def main():

    while(1):
    # chossing option to do CRUD operations
        selection = input('\nDigite 1 para inserir, 2 para atualizar, 3 para ler, 4 para remover\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print ('\n INVALID SELECTION \n')

# Function to insert data into mongo db
def insert():
    try:
        employeeId = input('Enter Employee id :')
        employeeName = input('Enter Name :')
        employeeAge = input('Enter age :')
        employeeCountry = input('Enter Country :')
    
    except Exception as e:
        print (str(e))

