import crud
import sys

bancodados = crud.Crud("dbimpacta.postgresql.dbaas.com.br",
            "dbimpacta",
            "impacta#2020",
            "dbimpacta")

print('*'*26)
print('Sistema de Alunos\n')
print('1 - Criar tabela')       
print('2 - Cadastrar aluno')
print('3 - Atualizar aluno')
print('4 - Excluir aluno')
print('5 - Consultar aluno')
print('6 - Consultar todos alunos')
print('7 - Sair do Sistema')
print('*'*26)

init = int(input('Selecione a opção desejada: '))

while init:
    if init == 1:
        bancodados.connect()
        bancodados.create_table()
        bancodados.close()
    if init == 2:
        bancodados.connect()
        bancodados.insert_aluno()
        bancodados.close()
    if init == 3:
        bancodados.connect()
        bancodados.update()
        bancodados.close()
    if init == 4:
        bancodados.connect()
        bancodados.delete_aluno()
        print('DELETADO COM SUCESSO! ')
        bancodados.close()
    if init == 5:
        bancodados.connect()
        bancodados.consultar()
        bancodados.close()
    if init == 6:
        bancodados.connect()
        bancodados.consultar_todos()
        bancodados.close()
    if init == 7: 
        bancodados.close()
        print('Saindo do sistema! Até logo \o/')
        sys.exit()
    break
        
        