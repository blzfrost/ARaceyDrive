import pygame
import time
import random
import ClassObjects

pygame.init()
game_display = pygame.display.set_mode((ClassObjects.display_width, ClassObjects.display_height))
pygame.display.set_caption("A Racey Drive")
clock = pygame.time.Clock()


def display_score():
    font = pygame.font.Font("georgia.ttf", 25)
    text = font.render("Dodged: " + str(ClassObjects.score), True, ClassObjects.black)
    game_display.blit(text, (0, 0))


def message_display(text):
    """Used in the crashed screen"""
    large_text = pygame.font.Font("georgia.ttf", 115)
    text_surface = large_text.render(text, True, ClassObjects.black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((ClassObjects.display_width/2), (ClassObjects.display_height/2))
    game_display.blit(text_surface, text_rect)

    pygame.display.update()
    time.sleep()
    gameloop()


def crash():
    message_display("You Can Do It")


def gameloop:
    pass