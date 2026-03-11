import sqlite3
import datetime


#Coisas para fazer
#Criar função para ler os dados
#Criar função para adionar dados
#Criar função para editar dados
#Ver como colocar a data, se vai ser no formato de texto ou algum outro - Data que terminou mesmo
    #pensei em colocar algo como dia e mes - variável para o dia + o texto da barra e depois o mês
    

#Menu esté funcionando e os registros então indo e sendo mostrados
#Modificar para ter um valor padrão caso o jogo não estaja finalizado

#O jogo não vou limitar o tamanho porque pode ser grande
#Plataforma é aonde eu joguei o jogo 
#Status do andamento da minha jogatina
#Data_finalizado é quando eu terminei o jogo
def criar_tabela(): 
    conexao = sqlite3.connect('BackLog.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS backlog(
                        id INTEGER PRIMARY KEY, 
                        GAME TEXT NOT NULL,
                        PLATFORM TEXT NOT NULL,
                        STATUS TEXT NOT NULL,
                        DATA_FINALIZADO TEXT NOT NULL,
                        CHECK (STATUS IN ("Jogando","Finalizado","Pendente")))''')
    conexao.commit()
    conexao.close()


#Registrar um jogo
def adicionar_registro(game, platform, status, dataFinalizado):
    conexao = sqlite3.connect('Backlog.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO backlog (GAME, PLATFORM, STATUS, DATA_FINALIZADO) VALUES (?, ?, ?, ?)''',(game,platform,status,dataFinalizado))
    conexao.commit()
    conexao.close()


#Listar todos os usuários
def listar_registros():
    conexao = sqlite3.connect('Backlog.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM backlog''')
    games = cursor.fetchall()
    for game in games: 
        print(game)
    conexao.close()

#Atualizar os dados 
#Separa quais parte vou querer atualizar posso querer mudar só umas partes
def atualizar_status(id,status): 
    conexao = sqlite3.connect('Backlog.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE backlog SET STATUS = ? WHERE id = ?''', (status, id))
    conexao.commit()
    conexao.close()

def atualizar_data(id,dataFinalizado):
    conexao = sqlite3.connect('Backlog.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE backlog SET DATA_FINALIZADO = ? WHERE id = ?''', (dataFinalizado, id))
    conexao.commit()
    conexao.close()


#Apagando um registro 
def deletar_registro(id): 
    conexao = sqlite3.connect('Backlog.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM backlog WHERE id = ?''', (id))
    conexao.commit()
    conexao.close()

#Menu de escolhas
def menu(): 
    print("\n1. Adicionar registro")
    print("2. Listar registro")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("5. Sair")


#Criar a tabela se ela não existir
    #Usar função de criar tabela 

if __name__ == "__main__":
    while True:
        menu()

        escolha = int(input('Escolha uma das opções: '))

        if escolha == 1:
            game = input('Digite o nome do jogo: ')
            platform =  input('\nDigite a plataforma: ') 
            print('\nDigite o status (andamento do jogo: Jogango, Finalizado, Pendente)')
            status =  input('\nStatus: ')
            dataFinalizado = input('Digite a data de finalização do jogo no formado dd/mm/yyyy: ') 
            adicionar_registro(game,platform,status,dataFinalizado)
        elif escolha == 2:
            listar_registros()
        elif escolha == 3:
            id = int(input('Digite o ID que deseja alterar: '))
            status = input('Digite o novo Status para o backlog: ')
            atualizar_status(id, status)
            if status == 'Finalizado': 
                dataFinalizado = input('Digite a data de finalização do jogo no formado dd/mm/yyyy: ') 
                atualizar_data(id,dataFinalizado)

        elif escolha == 4:  
            deletar_registro()
        else:
            exit()            
