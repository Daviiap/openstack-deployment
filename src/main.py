from os import system

from Controllers.NetworkController import NetworkController
from Controllers.FlavorController import FlavorController
from Controllers.ImageController import ImageController
from Controllers.SecurityGroupController import SecurityGroupController
from Controllers.ServerController import ServerController
from Controllers.KeypairController import KeypairController
from Controllers.ConnectionController import ConnectionController
from Controllers.ErrorController import ErrorController
from UseCases.DeleteInstance import delete_instance
from UseCases.GetInfosByFile import get_infos_by_file
from UseCases.GetInfosByPrompt import get_infos_by_prompt
from UseCases.ListServers import list_servers
from UseCases.RunCICD import run_ci_cd
from Utils import print_table


def program(flavorController, imageController, securityGroupController, networkController, keypairController, serverController, errorController):
    system('clear')
    print('(1) Criar instância à partir de configurações de arquivo .yml / .yaml')
    print('(2) Criar instância à partir de configurações de opções pelo terminal')
    print('(3) Excluir instância')
    print('(4) Rodar script CI/CD')
    print('(5) Listar VM\'s na cloud')
    print('(0) Sair\n')
    option = input('Selecione: ')
    while option != '0' and option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
        option = input('Opção inválida, tente novamente: ')

    if option != '0':
        instance_infos = None
        status = None
        if option == '1':
            instance_infos = get_infos_by_file(
                imageController=imageController,
                flavorController=flavorController,
                securityGroupController=securityGroupController,
                networkController=networkController,
                keypairController=keypairController,
                errorController=errorController
            )
        elif option == '2':
            instance_infos = get_infos_by_prompt(
                imageController=imageController,
                flavorController=flavorController,
                securityGroupController=securityGroupController,
                networkController=networkController,
                keypairController=keypairController,
                errorController=errorController
            )
        elif option == '3':
            status = delete_instance(serverController=serverController)
        elif option == '4':
            run_ci_cd()
        elif option == '5':
            list_servers(serverController)

        if instance_infos != None:
            system('clear')
            print('Criando instância \'' +
                  instance_infos['instance_name'] + '\'...')
            status = serverController.create_server(
                flavor_name=instance_infos['flavor_name'],
                image_id=instance_infos['image_id'],
                instance_name=instance_infos['instance_name'],
                keypair_name=instance_infos['keypair'],
                network_name=instance_infos['network'],
                security_groups=instance_infos['security_groups']
            )

        if status != None:
            print(status)
        input('Pressione Enter para continuar...')
        program(flavorController, imageController,
                securityGroupController, networkController, keypairController, serverController, errorController)


def main():
    openstack_conn = ConnectionController.create_connection()

    flavorController = FlavorController(openstack_conn)
    imageController = ImageController(openstack_conn)
    securityGroupController = SecurityGroupController(openstack_conn)
    serverController = ServerController(openstack_conn)
    networkController = NetworkController(openstack_conn)
    keypairController = KeypairController(openstack_conn)
    errorController = ErrorController(openstack_conn)

    system('clear')
    print('Lista de servers já existentes na cloud:')
    print_table(serverController.list_servers())
    input('Pressione Enter para continuar...')

    program(
        flavorController,
        imageController,
        securityGroupController,
        networkController,
        keypairController,
        serverController,
        errorController
    )


main()
