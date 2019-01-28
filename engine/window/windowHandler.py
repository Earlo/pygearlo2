import pygame
from collections import defaultdict

from .guiHandler import GuiHandler
from .bgrHandler import BgrHandler
from .gameCamera import GameCamera


class WindowHandler(GuiHandler, BgrHandler):
  def __init__(self):

    super().__init__()
    self.window = pygame.display.set_mode((self.w, self.h),
                                          pygame.HWSURFACE |
                                          pygame.DOUBLEBUF)

    self.needs_resize = False
    self.last_resie_request = 0
    self.camera = GameCamera(self, self.w, self.h)
    self.to_display = defaultdict(list)
    self.to_erase = []
    self.flip = False

  def draw_frame(self, depth, surface, rect, area=None):
    self.to_display[depth].append((surface, rect, area))

  def force_erase(self, rect):
    self.to_erase.append(rect)

  def rezise_request(self, event):
    self.needs_resize = True
    self.last_resie_request = pygame.time.get_ticks()
    super().rezise_request(event)

  def update_display(self):
    if self.needs_resize:
      if pygame.time.get_ticks() - self.last_resie_request > 50:
        self.update_resolution()
        self.needs_resize = False
        self.flip = True

    update_rects = self.blit_updates()
    if self.flip:
      self.flip = False
      pygame.display.flip()
    elif update_rects:
      pygame.display.update(update_rects)

  def blit_updates(self):
    update_rects = self.erase()
    sorted(self.to_display)

    cam_x = -self.camera.x
    cam_y = -self.camera.y
    for depth in self.to_display:
      for change in self.to_display[depth]:
        sprite, rect, area = change
        self.window.blit(sprite, rect.move(cam_x, cam_y), area)
        update_rects.append(rect)
        # TODO fix design error
        # Only things that have moved should be erased
        # self.to_erase.append(rect)
      self.to_display[depth] = []
    return update_rects

  def erase(self):
    update_rects = []
    cam_x = -self.camera.previous.x
    cam_y = -self.camera.previous.y
    for rect in self.to_erase:
      pos = rect.move(cam_x, cam_y)
      self.window.blit(self.bgr_surf, pos, rect)
      update_rects.append(rect)
    self.to_erase = []
    return update_rects
