class ServerController:
    def __init__(self, connection):
        self.connection = connection

    def list_servers(self):
        servers = [['id', 'name']]

        for server in self.connection.compute.servers():
            server_attrs = []
            server_attrs.append(server.id)
            server_attrs.append(server.name)
            servers.append(server_attrs)

        return servers

    def create_server(self, image_id, flavor_name, network_name, security_groups, keypair_name, instance_name):
        flavor = self.connection.compute.find_flavor(
            flavor_name)
        network = self.connection.network.find_network(
            network_name)
        security_groups_list = []

        for security_group in security_groups:
            security_groups_list.append({
                'name': security_group.strip()
            })

        server = self.connection.compute.create_server(
            name=instance_name, image_id=image_id, flavor_id=flavor.id,
            networks=[{"uuid": network.id}], key_name=keypair_name,
            security_groups=security_groups_list)

        try:
            server = self.connection.compute.wait_for_server(server)
            print('IP: ' + server['addresses']['provider'][0]['addr'])
            return 'Instância criada com sucesso.'
        except Exception:
            return 'Error ao criar instância.'

    def delete_server(self, server_name):
        status = 'success'
        if self.connection.get_server(server_name) != None:
            self.connection.delete_server(server_name)
        else:
            status = 'Server not found'

        return status
