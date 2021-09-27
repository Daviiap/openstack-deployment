from Exceptions.VcpuException import VcpuException
from Exceptions.InstanciaException import InstanciaException
from Exceptions.SecurityGroupException import SecurityGroupException
from Exceptions.RamException import RamException

class ErrorController:
    
    def __init__(self, connection) -> None:
        self.connection = connection

    def erro_vcpu(self, flavor):
        print(flavor)
        vcpu_wanted = self.connection.compute.find_flavor(flavor).vcpus
        vcpu_used = self.connection.get_compute_limits()['total_cores_used']
        vcpu_max = self.connection.get_compute_limits()['max_total_cores']
        if (vcpu_wanted+vcpu_used > vcpu_max):
            raise VcpuException()
    
    def erro_instancias(self):
        instancias_usadas=self.connection.get_compute_limits()['total_instances_used']
        max_instancias=self.connection.get_compute_limits()['max_total_instances']
        if instancias_usadas == max_instancias:
            raise InstanciaException()
    
    def erro_grupo_seguranca(self, security_groups_list):
        security_group_used = self.connection.get_compute_limits()['total_server_groups_used']
        security_group_max = self.connection.get_compute_limits()['properties']['maxSecurityGroups']
        if (security_group_used+len(security_groups_list) > security_group_max):
            raise SecurityGroupException()
    
    def erro_ram(self, flavor):
        ram_necessaria = self.connection.compute.find_flavor(flavor).ram
        ram_usada=self.connection.get_compute_limits()['total_ram_used']
        ram_max=self.connection.get_compute_limits()['max_total_ram_size']
        if (ram_usada + ram_necessaria > ram_max):
            raise RamException()  