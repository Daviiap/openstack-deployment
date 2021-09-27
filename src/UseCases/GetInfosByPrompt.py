from os import system
from Utils import get_security_groups_input, get_input, print_table
from Controllers.TratamentoController import TratamentoController
from Exceptions.VcpuException import VcpuException
from time import sleep

def get_infos_by_prompt(imageController, flavorController, securityGroupController, networkController, keypairController, errorController):
    
    TratamentoController.instancia(errorController)

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
   
    #TratamentoController.vcpu(errorController, flavor_name)
    TratamentoController.ram(errorController, flavor_name)
    
    system('clear')
    print_table(securityGroupController.list_security_groups())
    security_groups = get_security_groups_input(
        'Digite o nome dos security groups separados somente por \';\': ',
        securityGroupController.security_group_exist)

    TratamentoController.grupo_seguranca(errorController, security_groups)

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
