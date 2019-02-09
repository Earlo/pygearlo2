import pygame

from ..graphicalAssetHandler import GraphicalAssetHandler
# TODO DESIGN should inherit Rect or Surface?
# RECT is unique for everyone, Grafic isn't


class Sprite(pygame.Rect):
  # example
  sprites = ["frog"]
  graphic_layer = 0
  graphicalAssetHandler = GraphicalAssetHandler()

  def __init__(self, parent, sprite_type):
    self.parent = parent
    self.sprite_type = sprite_type
    self.change_sprite_to(0)
    super().__init__((0, 0), self._surf.get_size())

  # TODO make sprite a property
  def change_sprite_to(self, i):
    self.sprite = self.sprites[i]
    self.change_sprite(self.sprite_type, self.sprite)

  def change_sprite(self, sprite_type, sprite):
    self.surf = self.graphicalAssetHandler[sprite_type][sprite]

  def draw(self):
    print("adding {}".format(self))
    self.parent.updates.append(self)
    self.parent.surf.blit(self.surf, self)

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

  # This is shit
  # @property
  # def rect(self):
  #  return self.GAME.ENGINE.camera.clip(self)

  def __repr__(self):
    try:
      return "Sprite {0} {1} at {2} ".format(self.sprite_type, self.sprite, self)
    except AttributeError:
      return "{}".format(self)
