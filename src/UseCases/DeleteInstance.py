from os import system
from Utils import print_table


def delete_instance(serverController):
    system('clear')
    print_table(serverController.list_servers())
    delete_status = serverController.delete_server(
        input('\nDigite o nome da instância que você deseja excluir: '))
    if delete_status == 'success':
        status = 'Instância excluída com sucesso.'
    else:
        status = 'Instância não encontrada.'
    return status
