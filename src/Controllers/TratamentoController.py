from Exceptions.VcpuException import VcpuException
from Exceptions.InstanciaException import InstanciaException
from Exceptions.SecurityGroupException import SecurityGroupException
from Exceptions.RamException import RamException
from time import sleep
from os import system

class TratamentoController:

    def instancia(errorController):
        try:
            errorController.erro_instancias()
        except InstanciaException:
            print("A instacia excedeu o limite estabelecido")
            sleep(3)
            system('clear')
            return

    def vcpu(errorController, flavor):
        try:
            errorController.erro_vcpu(flavor)
        except VcpuException:
            print("A vcpu excedeu o limite estabelecido")
            sleep(3)
            system('clear')
            return

    def ram(errorController, flavor):
        try:
            errorController.erro_ram(flavor)
        except RamException:
            print("A ram excedeu o limite estabelecido")
            sleep(3)
            system('clear')
            return

    def grupo_seguranca(errorController, security_groups):
        try:
            errorController.erro_grupo_seguranca(security_groups)
        except SecurityGroupException:
            print("O grupos de segurança excedeu o limite estabelecido")
            sleep(3)
            system('clear')
            return

    