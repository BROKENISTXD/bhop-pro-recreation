from ursina import Entity, color

class Level:
    """Creates a level with platforms and a finish area."""

    def __init__(self, index: int):
        self.index = index
        self.entities = []
        self.finish = None
        self.build_level()

    def build_level(self):
        # Simple platform layout: start pad, some cubes, and finish cube
        start = Entity(model='cube', color=color.gray, scale=(4, 0.5, 4), position=(0, -0.25, 0), collider='box')
        self.entities.append(start)
        for i in range(5 + self.index):
            block = Entity(model='cube', color=color.azure, scale=(2, 0.5, 2), position=(0, 1 * (i+1), -3 * (i+1)), collider='box')
            self.entities.append(block)
        self.finish = Entity(model='cube', color=color.lime, scale=(3,0.5,3), position=(0, 0.25 + (5 + self.index), -3*(5 + self.index + 1)), collider='box')
        self.entities.append(self.finish)

    def clear(self):
        for e in self.entities:
            e.disable()
        self.entities.clear()

