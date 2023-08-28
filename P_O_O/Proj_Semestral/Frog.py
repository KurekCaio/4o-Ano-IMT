#===== Imports =====
import pygame as p
import sys

#=====
p.init()
#=====

#===== Classes =====
class Frog(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = width/2
        self.y = 50
        self.step = 20
        self.width = 50
        self.height = 50

        # Frog Images
        self.frog_up = p.image.load('.\images\Sapo_cima.png')
        self.frog_down = p.image.load('.\images\Sapo_baixo.png')
        self.frog_left = p.image.load('.\images\Sapo_esquerda.png')
        self.frog_right = p.image.load('.\images\Sapo_direita.png')

        #Resize
        self.frog_up = p.transform.scale(self.frog_up, (self.width, self.height))
        self.frog_down = p.transform.scale(self.frog_down, (self.width, self.height))
        self.frog_left = p.transform.scale(self.frog_left, (self.width, self.height))
        self.frog_right = p.transform.scale(self.frog_right, (self.width, self.height))

        #Inicial image
        self.image = self.frog_up
        self.rect = self.image.get_rect()

#===== Functions =====

def update(self):
    #self.movement()
    self.rect.center = (self.x, self.y)

# def movement(self):
#     key = p.key.get_pressed()
#     if key[p.K_UP]:
#         self.y -= self.step
#     elif key[p.K_DOWN]:
#         self.y += self.step
#     elif key[p.K_LEFT]:
#         self.x -= self.step
#     elif key[p.K_RIGHT]:
#         self.x += self.step

def teste_teclas(self):
    if event.type == p.KEYDOWN:
        if event.key == p.K_UP:
            print("Key UP has been pressed")
            
        # checking if key "J" was pressed
        if event.key == p.K_DOWN:
            print("Key DOWN has been pressed")
            
        # checking if key "P" was pressed
        if event.key == p.K_LEFT:
            print("Key LEFT has been pressed")
            
        # checking if key "M" was pressed
        if event.key == p.K_RIGHT:
            print("Key RIGHT has been pressed")

#===== Screen configuration =====
width = 820
height = 580
screen = p.display.set_mode((width,height))
p.display.set_caption("Frog Game")

#=========================================================================================================================================================
frog = Frog()
frog_group = p.sprite.Group()
frog_group.add(frog)

clock = p.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False              
        #==============================================
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                print("Key UP has been pressed")
            if event.key == p.K_DOWN:
                print("Key DOWN has been pressed")
            if event.key == p.K_LEFT:
                print("Key LEFT has been pressed")
            if event.key == p.K_RIGHT:
                print("Key RIGHT has been pressed")
        #==============================================
        
    screen.fill((40,115,97))
    frog_group.draw(screen)
    frog_group.update()
    p.display.update()
p.quit()