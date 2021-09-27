class InstanciaException(Exception):
    
    def __init__(self):
        super().__init__("Máximo de instância execedida!")

