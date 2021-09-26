import yaml
from tabulate import tabulate


def print_table(table):
    print(tabulate(table, headers='firstrow', tablefmt='grid'))


def load_yml(file_path):
    try:
        with open(file_path) as yml_file:
            dictionary = yaml.load(yml_file, Loader=yaml.FullLoader)

        return dictionary
    except FileNotFoundError:
        return None


def get_input(prompt, retry_prompt, validation_function):
    value = input(prompt).strip()

    while(validation_function(value) == False):
        value = input(retry_prompt).strip()

    return value


def get_security_groups_input(prompt, validation_function):
    value = input(prompt).split(';')

    for security_group in value:
        if validation_function(security_group.strip()) == False:
            value = get_security_groups_input(
                'Security Group ' + security_group + ' não existe, tente novamente (lembre de digitar todos novamente): ', validation_function)

    return value
