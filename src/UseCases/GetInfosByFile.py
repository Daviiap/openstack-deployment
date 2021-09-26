from os import system
from Utils import load_yml


def get_infos_by_file(imageController, flavorController, securityGroupController, networkController, keypairController):
    system('clear')
    file_path = input('Digite o path para o arquivo de configuração: ')
    file_configs = load_yml(file_path)

    entry_is_valid = True

    if file_configs != None:
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
                print('[ERROR] Security_group' +
                      security_group + 'não existe.')
                entry_is_valid = False
    else:
        print('Arquivo não encontrado, tente novamente. ')
        entry_is_valid = False

    configs = None
    if entry_is_valid:
        configs = file_configs

    return configs
