class SecurityGroupException(Exception):
    
    def __init__(self):
        super().__init__("Máximo de grupos de segurança alcançado!")

