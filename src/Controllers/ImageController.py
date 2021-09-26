class ImageController:
    def __init__(self, connection) -> None:
        self.connection = connection

    def list_images(self):
        images = [['id', 'name', 'status']]

        for image in self.connection.compute.images():
            if(image.status == 'ACTIVE'):
                image_attrs = []
                image_attrs.append(image.id)
                image_attrs.append(image.name)
                image_attrs.append(image.status)
                images.append(image_attrs)

        return images

    def image_exist(self, image_id):
        return self.connection.get_image(image_id) != None
