import crud
import sys
import os

bancodados = crud.Crud("dbimpacta.postgresql.dbaas.com.br",
            "dbimpacta",
            "impacta#2020",
            "dbimpacta")
init = 0
while init != 8:
    try:
        print('*'*26)
        print('Sistema de Alunos\n')
        print('1 - Criar tabela')       
        print('2 - Cadastrar aluno')
        print('3 - Atualizar aluno')
        print('4 - Excluir aluno')
        print('5 - Consultar aluno')
        print('6 - Consultar todos alunos')
        print('7 - Excluir todos registros')
        print('8 - Sair do Sistema')
        print('*'*26)
        init = int(input('Selecione a opção desejada: '))
        print('*'*26)
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
            bancodados.connect()
            bancodados.delete_todos()
            bancodados.close()
    except:
        print('Digite apenas as opções acima! ')
else:
    print('Saindo do sistema! Até logo \o/')
    sys.exit()