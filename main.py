import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music/GoodMorningFreedom.mp3")
pygame.mixer.music.play()
echo("playing")
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)