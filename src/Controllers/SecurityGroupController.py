class SecurityGroupController:
    def __init__(self, connection) -> None:
        self.connection = connection

    def list_security_groups(self):
        security_groups = [['id', 'name', 'description']]

        for security_group in self.connection.list_security_groups():
            security_group_attrs = []
            security_group_attrs.append(security_group.id)
            security_group_attrs.append(security_group.name)
            security_group_attrs.append(security_group.description)
            security_groups.append(security_group_attrs)

        return security_groups

    def security_group_exist(self, security_group_name):
        return self.connection.get_security_group(security_group_name) != None
