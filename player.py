from ursina import Entity, Vec3, held_keys, time, color, load_model

class Player(Entity):
    """Player entity with basic bunny hop movement and health."""

    def __init__(self, **kwargs):
        super().__init__(model='cube', color=color.orange, collider='box', **kwargs)
        self.speed = 5
        self.jump_height = 1.0
        self.grounded = False
        self.velocity = Vec3(0, 0, 0)
        self.health = 100
        self.knife = Entity(model=load_model('assets/knives/knife.gltf'),
                            parent=self, scale=0.5, position=Vec3(0.5,0,0))

    def update(self):
        dt = time.dt
        move = Vec3(
            held_keys['d'] - held_keys['a'],
            0,
            held_keys['w'] - held_keys['s']
        )
        if move.length() > 0:
            move = move.normalized() * self.speed * dt
        self.position += move

        if self.grounded and held_keys['space']:
            self.velocity.y = self.jump_height
            self.grounded = False

        self.velocity.y -= 9.8 * dt
        self.position += self.velocity * dt

        if self.y <= 0:
            self.y = 0
            self.grounded = True
            self.velocity.y = 0

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

