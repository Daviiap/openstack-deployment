import openstack

class ConnectionController:
    def create_connection(cloud):
        return openstack.connect(cloud=cloud)
