from ursina import Ursina, camera, Text
from player import Player
from level import Level
from timer import Timer

class Game(Ursina):
    def __init__(self):
        super().__init__()
        self.level_index = 0
        self.level = None
        self.player = Player(position=(0,1,0))
        camera.parent = self.player
        camera.position = (0, 1.8, -5)
        camera.rotation = (0,0,0)
        camera.fov = 90
        self.timer = Timer()
        self.timer.start()
        self.info = Text(text='', position=(-0.85,0.45))
        self.load_level(self.level_index)

    def load_level(self, index):
        if self.level:
            self.level.clear()
        self.level = Level(index)
        self.player.position = (0,1,0)
        self.timer.reset()

    def update(self):
        self.player.update()
        if self.player.intersects(self.level.finish).hit:
            duration = self.timer.stop()
            self.level_index += 1
            if self.level_index >= 5:
                self.info.text = f'Finished! Total time: {duration:.2f}s'
            else:
                self.info.text = f'Level {self.level_index} done in {duration:.2f}s'
                self.load_level(self.level_index)
        self.info.text = f'Health: {self.player.health}  Time: {self.timer.elapsed:.2f}s'

if __name__ == "__main__":
    game = Game()
    game.run()

