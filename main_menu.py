from button import Button
import pygame as pg

class MainMenu:
    def __init__(self, shape) -> None:
        pg.init()
        settings = {
            'text': 'Play a game?',
            'hover_color': pg.Color('blue'),
            'clicked_color': pg.Color('red')
        }
        self.play = Button(
            pg.rect.Rect(shape[0] * 0.4, shape[1] * 0.4, shape[0] * 0.2, shape[1] * 0.2), 
            pg.Color('gray'), 
            self.played,
            **settings
        )
    
    def played(self):
        print('game played')
    
    def update(self, screen) -> bool:
        self.play.update(screen)
        return self.play.clicked
    
    def event(self, event):
        self.play.check_event(event)