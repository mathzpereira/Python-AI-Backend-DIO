import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

def create_database():
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS desafiobancobd')
    cursor.close()

def create_table():
    cursor = connection.cursor()
    cursor.execute('USE desafiobancobd')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS cliente (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), idade INT, cidade VARCHAR(255), cpf VARCHAR(11) UNIQUE, cnpj VARCHAR(14) UNIQUE)')
    cursor.close()

def insert_pf(nome, idade, cidade, cpf):
    cursor = connection.cursor()
    try:
        cursor.execute(
        'INSERT INTO cliente (nome, idade, cidade, cpf) VALUES (%s, %s, %s, %s)',
        (nome, idade, cidade, cpf))
        connection.commit()
        
    except Exception as e:
        print('Error on inserting the data:', e)
        connection.rollback()
    cursor.close()

def insert_pj(nome, cidade, cnpj):
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO cliente (nome, cidade, cnpj) VALUES (%s, %s, %s)',
        (nome, cidade, cnpj)
    )
    connection.commit()
    cursor.close()

def select():
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM cliente')
        for linha in cursor.fetchall():
            if linha['cpf'] is not None:
                print('\nPessoa Física')
                print('Nome:', linha['nome'], '\nIdade:', linha['idade'], '\nCidade:', linha['cidade'], '\nCPF:', linha['cpf'])
            elif linha['cnpj'] is not None:
                print('\nPessoa Jurídica')
                print('Nome:', linha['nome'], '\nCidade:', linha['cidade'], '\nCNPJ:', linha['cnpj'])
    except Exception as e:
        print('Error on selecting the data:', e)
    cursor.close()

def main():
    create_database()
    create_table()

    while(True):
        print('\nWelcome to the menu')
        print('1 - Insert PF (Pessoa Física)')
        print('2 - Insert PJ (Pessoa Jurídica)')
        print('3 - Select all the clients')
        print('4 - Exit')
        option = input('Choose an option: ')
        if option == '1':
            nome = input('Name: ')
            idade = int(input('Age: '))
            cidade = input('City: ')
            cpf = input('CPF: ')
            insert_pf(nome, idade, cidade, cpf)
        elif option == '2':
            nome = input('Name: ')
            cidade = input('City: ')
            cnpj = input('CNPJ: ')
            insert_pj(nome, cidade, cnpj)
        elif option == '3':    
            select()
        elif option == '4':
            break

main()