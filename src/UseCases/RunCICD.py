from os import system


def run_ci_cd():
    system('clear')
    input('Conecte-se à VPN e pressione Enter para continuar...')
    configs_path = input('Informe o path para o arquivo de CI/CD: ')
    system('bash ' + configs_path)
