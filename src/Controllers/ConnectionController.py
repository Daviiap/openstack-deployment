import openstack
from Utils import get_env_variables

class ConnectionController:
    def create_connection():
        print(get_env_variables())
        try:
            print(get_env_variables())
            openstack_connection = openstack.connect(**get_env_variables())
            openstack_connection.authorize()
        except:
            print("Invalid credentials.")
            exit()
        return openstack_connection



