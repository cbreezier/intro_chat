import pygame
import random
import math
import os
import subprocess
from ast import literal_eval

background_colour = (0, 0, 0)
(width, height) = (800, 600)
drag = 0.999
elasticity =1
gravity = (-math.pi, -0.1)
my_platforms = []
my_particles = []
my_boosters = []

def addVectors((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

def load_particles():
    botdir = "bouncingballs"
    for botname in os.listdir(botdir):
        botpath = os.path.join(botdir, botname)
        program = subprocess.Popen(["python", botpath], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        program.stdin.write("colour")
        colour, stderr = program.communicate()
        
        program = subprocess.Popen(["python", botpath], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        program.stdin.write("collision")
        collisionMove, stderr = program.communicate()

        particle = Particle((20, 20), 20, literal_eval(colour), float(collisionMove))
        particle.speed = random.random()
        particle.angle = random.uniform(0, math.pi*2)

        my_particles.append(particle)
    
class Platform(object):
    def __init__(self, x, y, width, colour):
        self.x = x
        self.y = y
        self.height = 5
        self.width = width
        self.colour = colour

    def display(self):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height), 0)

class Particle():
    def __init__(self, (x, y), size, colour, collision):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.collision = collision / 360 * 2 * math.pi

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag

    def in_platform(self):
        for i in range(len(my_platforms)):
            platform = my_platforms[i]
            if platform.x - self.size <= self.x <= platform.x + platform.width + self.size and platform.y - self.size <= self.y <= platform.y + platform.height + self.size:
                return True
        return False

    def in_booster(self):
        for booster in my_boosters:
            if booster.x - self.size <= self.x <= booster.x + self.size \
            and booster.y - self.size <= self.y <= booster.y + self.size:
                return True
        return False   
        
    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        if self.in_platform():
            # if -math.pi/2 < self.angle < math.pi/2:
            self.angle = math.pi - self.angle
            self.speed *= elasticity
            
        if self.in_booster():
            self.angle, self.speed = addVectors((self.angle, self.speed), (self.collision, 0.5))

class Booster():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 3
        self.colour = (255, 255, 255)

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, 0)        
            
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fun with pygame!")

number_of_platforms = 10
number_of_boosters = 30

for n in range(number_of_platforms):
    sizeX = random.randint(50, 100)
    x = random.randint(sizeX, width - sizeX)
    y = random.randint(5, height - 5)
    #colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    colour = (255, 255, 255)
    my_platforms.append(Platform(x, y, sizeX, colour))

for n in range(number_of_boosters):
    x = random.randint(sizeX, width - sizeX)
    y = random.randint(5, height - 5)
    my_boosters.append(Booster(x, y))

    
load_particles()

selected_particle = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findParticle(my_particles, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_particle = None
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                my_particles[0].angle, my_particles[0].speed = addVectors((my_particles[0].angle, my_particles[0].speed), (0, -2))
            elif event.key == pygame.K_LEFT:
                my_particles[0].angle, my_particles[0].speed = addVectors((my_particles[0].angle, my_particles[0].speed), (math.pi/2, 2))
            elif event.key == pygame.K_RIGHT:
                my_particles[0].angle, my_particles[0].speed = addVectors((my_particles[0].angle, my_particles[0].speed), (-math.pi/2, 2))
                

    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = 0.5*math.pi + math.atan2(dy, dx)
        selected_particle.speed = math.hypot(dx, dy) * 0.1

    screen.fill(background_colour)

    for particle in my_particles:
        particle.move()
        particle.bounce()
        particle.display()

    for platform in my_platforms:
        platform.display()
        
    for booster in my_boosters:
        booster.display()
    
    pygame.display.flip()
    pygame.time.delay(10)
