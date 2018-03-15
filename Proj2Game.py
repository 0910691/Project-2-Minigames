import pygame
import sys
import os
import time

pygame.init()


class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
    	         font_color=(255, 255, 255), xy=(0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x, self.pos_y = xy
        self.position = xy

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

    def is_mouse_selection(self, xy):
        posx, posy = xy
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) \
            and (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False


class GameMenu():
    def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.funcs = funcs
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item)

            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            # This line includes a bug fix by Ariel (Thanks!)
            # Please check the comments section for an explanation
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                    mpos = pygame.mouse.get_pos()
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            mainloop = False
                            self.funcs[item.text]()

            # Redraw the background
            self.screen.fill(self.bg_color)

            for item in self.items:
                if item.is_mouse_selection(pygame.mouse.get_pos()):
                    item.set_font_color((255, 0, 0))
                    item.set_italic(True)
                else:
                    item.set_font_color((255, 255, 255))
                    item.set_italic(False)
                self.screen.blit(item.label, item.position)

            pygame.display.flip()


if __name__ == "__main__":
    def test_menu():
        print ('Testing menu options')

    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)

    funcs = {'Start': test_menu,
             'How to Play': sys.exit,
             'Settings': sys.exit,
             'Quit': sys.exit}

    menu_items = ('Start', 'How to Play', 'Settings', 'Quit')

    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, menu_items)
    gm.run()