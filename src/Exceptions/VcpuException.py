class VcpuException(Exception):
    
    def __init__(self):
        super().__init__("Máximo de vcpu execedida!")

