class NetworkController:
    def __init__(self, connection):
        self.connection = connection

    def list_networks(self):
        networks = [['id', 'name', 'status']]

        for network in self.connection.network.networks():
            network_attrs = []
            network_attrs.append(network.id)
            network_attrs.append(network.name)
            network_attrs.append(network.status)
            networks.append(network_attrs)

        return networks

    def network_exist(self, network_name):
        return self.connection.get_network(network_name) != None
