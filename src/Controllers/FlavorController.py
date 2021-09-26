class FlavorController:
    def __init__(self, connection) -> None:
        self.connection = connection

    def list_flavors(self):
        flavors = [['id', 'name', 'ram', 'disk (GB)', 'vcpus']]

        for flavor in self.connection.compute.flavors():
            flavor_attrs = []
            flavor_attrs.append(flavor.id)
            flavor_attrs.append(flavor.name)
            flavor_attrs.append(flavor.ram)
            flavor_attrs.append(flavor.disk)
            flavor_attrs.append(flavor.vcpus)
            flavors.append(flavor_attrs)

        return flavors

    def flavor_exist(self, flavor_name):
        return self.connection.get_flavor(flavor_name) != None
