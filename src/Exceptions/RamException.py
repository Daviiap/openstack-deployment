class RamException(Exception):
    
    def __init__(self):
        super().__init__("Máximo de ram alcançado!")

