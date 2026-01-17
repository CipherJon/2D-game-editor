class Entity:
    def __init__(self, entity_id, name, position, properties=None):
        self.entity_id = entity_id
        self.name = name
        self.position = position
        self.properties = properties or {}

    def update_position(self, new_position):
        self.position = new_position

    def add_property(self, key, value):
        self.properties[key] = value

    def get_property(self, key):
        return self.properties.get(key)
