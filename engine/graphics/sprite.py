import pygame

# TODO DESIGN should inherit Rect or Surface?
# RECT is unique for everyone, SPRITE isn't


class Sprite(pygame.Rect):
  # example
  sprites = ["frog"]
  bgr_depth = 0

  def __init__(self, GAME, sprite_type):
    self.GAME = GAME
    self.sprite_type = sprite_type
    self.change_sprite_to(0)
    super().__init__((0, 0), self._surf.get_size())

  def change_sprite_to(self, i):
    self.sprite = self.sprites[i]
    self.change_sprite(self.sprite_type, self.sprite)

  def change_sprite(self, sprite_type, sprite):
    self.surf = self.GAME.ENGINE.graphical_asset_handler[sprite_type][sprite]

  # TODO this method blits, doesn't draw
  # TODO the updated surface should be configurable,
  # now it defaults to entity behaviour
  # Handle bgr cases and such
  def draw(self):
    self.GAME.ENGINE.updates[self.bgr_depth].append((self.surf, self))

  @property
  def sprite(self):
    return self._sprite

  @sprite.setter
  def sprite(self, new_sprite):
    self._sprite = new_sprite

  @property
  def surf(self):
    return self._surf

  @surf.setter
  def surf(self, new_surf):
    self._surf = new_surf
    self.size = self.surf.get_size()

  def drawable_rect(self):
    return self.GAME.ENGINE.camera.clip(self)

  def __repr__(self):
    return "Sprite {0} {1} at {2} ".format(self.sprite_type, self.sprite, self)