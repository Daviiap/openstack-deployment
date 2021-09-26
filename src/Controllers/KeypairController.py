class KeypairController:
    def __init__(self, connection) -> None:
        self.connection = connection

    def list_keypairs(self):
        keypairs = [['name', 'fingerprint', 'type']]

        for keypair in self.connection.list_keypairs():
            keypair_attrs = []
            keypair_attrs.append(keypair.name)
            keypair_attrs.append(keypair.fingerprint)
            keypair_attrs.append(keypair.type)
            keypairs.append(keypair_attrs)

        return keypairs

    def keypair_exist(self, keypair_name):
        return self.connection.get_keypair(keypair_name) != None
