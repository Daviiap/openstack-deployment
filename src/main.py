from os import system

from Controllers.NetworkController import NetworkController
from Controllers.FlavorController import FlavorController
from Controllers.ImageController import ImageController
from Controllers.SecurityGroupController import SecurityGroupController
from Controllers.ServerController import ServerController
from Controllers.KeypairController import KeypairController
from Controllers.ConnectionController import ConnectionController
from Utils import get_security_groups_input, get_input, load_yml, print_table


def get_infos_by_prompt(imageController, flavorController, securityGroupController, networkController, keypairController):
    system('clear')
    print_table(imageController.list_images())
    image_id = get_input('Digite o id da imagem desejada: ',
                         'Imagem não existe, tente novamente: ',
                         imageController.image_exist)

    system('clear')
    print_table(flavorController.list_flavors())
    flavor_name = get_input('Digite o nome do flavor desejado: ',
                            'Flavor não existe, tente novamente: ',
                            flavorController.flavor_exist)

    system('clear')
    print_table(securityGroupController.list_security_groups())
    security_groups = get_security_groups_input(
        'Digite o nome dos security groups separados somente por \';\': ',
        securityGroupController.security_group_exist)

    system('clear')
    print_table(networkController.list_networks())
    network = get_input('Digite o nome da network desejada: ',
                        'Network não existe, tente novamente: ',
                        networkController.network_exist)

    system('clear')
    print_table(keypairController.list_keypairs())
    keypair = get_input('Digite o nome da keypair desejada: ',
                        'Keypair não existe, tente novamente: ',
                        keypairController.keypair_exist)

    system('clear')
    instance_name = input('Digite o nome da instância: ').strip()

    return {
        'instance_name': instance_name,
        'image_id': image_id,
        'flavor_name': flavor_name,
        'security_groups': security_groups,
        'network': network,
        'keypair': keypair,
    }


def get_infos_by_file(imageController, flavorController, securityGroupController, networkController, keypairController):
    system('clear')
    file_path = input('Digite o path para o arquivo de configuração: ')
    file_configs = load_yml(file_path)

    entry_is_valid = True

    if imageController.image_exist(file_configs['image_id']) == False:
        print('[ERROR] Image' + file_configs['image_id'] + 'não existe.')
        entry_is_valid = False

    if flavorController.flavor_exist(file_configs['flavor_name']) == False:
        print('[ERROR] Flavor' + file_configs['flavor_name'] + 'não existe.')
        entry_is_valid = False

    if networkController.network_exist(file_configs['network']) == False:
        print('[ERROR] Network' + file_configs['network'] + 'não existe.')
        entry_is_valid = False

    if keypairController.keypair_exist(file_configs['keypair']) == False:
        print('[ERROR] Keypair' + file_configs['keypair'] + 'não existe.')
        entry_is_valid = False

    for security_group in file_configs['security_groups']:
        if securityGroupController.security_group_exist(security_group) == False:
            print('[ERROR] Security_group' + security_group + 'não existe.')
            entry_is_valid = False

    configs = None
    if entry_is_valid:
        configs = file_configs

    return configs


def main():
    cloud = input('Digite o nome da cloud que você deseja se conectar: ')
    openstack_conn = ConnectionController.create_connection(cloud)

    flavorController = FlavorController(openstack_conn)
    imageController = ImageController(openstack_conn)
    securityGroupController = SecurityGroupController(openstack_conn)
    serverController = ServerController(openstack_conn)
    networkController = NetworkController(openstack_conn)
    keypairController = KeypairController(openstack_conn)

    system('clear')
    print('Lista de servers já existentes na cloud \'' + cloud + '\':')
    print_table(serverController.list_servers())
    input('Pressione Enter para continuar...')

    system('clear')
    print('(1) Criar instância à partir de configurações de arquivo .yml / .yaml')
    print('(2) Criar instância à 0partir de configurações de opções pelo terminal')
    print('(3) Excluir instância')
    print('(0) Sair\n')
    option = input('Selecione: ')
    while option != '0' and option != '1' and option != '2' and option != '3':
        option = input('Opção inválida, tente novamente: ')

    instance_infos = None
    if option == '1':
        instance_infos = get_infos_by_file(
            imageController=imageController,
            flavorController=flavorController,
            securityGroupController=securityGroupController,
            networkController=networkController,
            keypairController=keypairController
        )
    elif option == '2':
        instance_infos = get_infos_by_prompt(
            imageController=imageController,
            flavorController=flavorController,
            securityGroupController=securityGroupController,
            networkController=networkController,
            keypairController=keypairController
        )
    elif option == '3':
        system('clear')
        print_table(serverController.list_servers())
        status = serverController.delete_server(
            input('\nDigite o nome da instância que você deseja excluir: '))
        if status == 'success':
            print('Instância excluída com sucesso.')
        else:
            print('Instância não encontrada.')

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

        print(status)


main()
