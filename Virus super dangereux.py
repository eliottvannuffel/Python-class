import os
import sys
import pygame
from pynput import mouse

def play_sound_on_mouse_move():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('youtube-uwuuuuu.wav')
    
    def on_move(x, y):
        sound.play()
    
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
    
if __name__ == '__main__':
    play_sound_on_mouse_move()