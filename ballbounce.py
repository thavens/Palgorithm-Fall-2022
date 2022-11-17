import pygame as pg
from button import Button
class Ball:
    def __init__(self, screen_shape, radius=100, damper=0.9):
        self.max_x = screen_shape[0]
        self.max_y = screen_shape[1]
        self.x = screen_shape[0] / 2
        self.y = screen_shape[1] / 2
        self.vx = 10
        self.vy = 30
        self.radius = radius
        self.damper = damper
        
        settings = {
            'text': 'End Game',
            'hover_color': pg.Color('blue'),
            'clicked_color': pg.Color('red')
        }
        self.button = Button(
            pg.rect.Rect(screen_shape[0] * 0.025, screen_shape[1] * 0.025, screen_shape[0] * 0.05, screen_shape[1] * 0.05), 
            pg.Color('gray'), 
            self.b_pressed,
            **settings
        )
    
    def update(self, screen):
        '''update game'''
        
        self.x += self.vx
        self.y += self.vy
        self.vy += 2
        
        if pg.mouse.get_pressed()[0]:
            self.x, self.y = pg.mouse.get_pos()
            self.vx, self.vy = pg.mouse.get_rel()
        
        screen.fill((0,0,0))
        
        if self.y + self.radius > self.max_y:
            self.vy = -abs(self.vy) * self.damper
        elif self.y - self.radius < 0:
            self.vy = abs(self.vy) * self.damper
        elif self.x + self.radius > self.max_x:
            self.vx = -abs(self.vx) * self.damper
        elif self.x - self.radius < 0:
            self.vx = abs(self.vx) * self.damper
        
        
        pg.draw.circle(screen, [255, 0, 0], [self.x, self.y], self.radius)
        self.button.update(screen)
        
        return self.button.clicked
        
    
    def event(self, event):
        '''event'''
        self.button.check_event(event)
    
    def b_pressed(self):
        pass