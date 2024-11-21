from pygame.surface import Surface


class SimObjectManager:
    def __init__(self, canvas: Surface):
        self.canvas = canvas
        self.sim_objects = []

    def add_sim_objects(self):
        self.sim_objects = []

    def update_sim_objects(self):
        for sim_object in self.sim_objects:
            sim_object.update_status()
            sim_object.update_position()
            sim_object.add_to_canvas()
