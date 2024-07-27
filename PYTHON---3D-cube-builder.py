import pygame
import numpy as np
from pygame.locals import *

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Cube Builder")
clock = pygame.time.Clock()

# Define the cube vertices and edges
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Function to project 3D points to 2D
def project(vertex, angle, distance):
    x, y, z = vertex
    s = np.sin(angle)
    c = np.cos(angle)
    x = x * c - z * s
    z = x * s + z * c
    f = distance / (distance - z)
    x = x * f
    y = y * f
    return int(x * 100 + 400), int(y * 100 + 300)

# Function to draw a cube
def draw_cube(cube_vertices):
    transformed_vertices = [project(vertex, angle, distance) for vertex in cube_vertices]
    for edge in edges:
        points = []
        for vertex in edge:
            points.append(transformed_vertices[vertex])
        pygame.draw.line(screen, (255, 255, 255), points[0], points[1])

# Function to translate cube vertices
def translate(cube_vertices, translation):
    return [[vertex[i] + translation[i] for i in range(3)] for vertex in cube_vertices]

# List to store multiple cubes
cubes = []

angle = 0
distance = 5
current_translation = [0, 0, 0]
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:  # Press space to add a new cube
                cubes.append(translate(vertices.copy(), current_translation))
            elif event.key == K_LEFT:
                current_translation[0] -= 1
            elif event.key == K_RIGHT:
                current_translation[0] += 1
            elif event.key == K_UP:
                current_translation[1] -= 1
            elif event.key == K_DOWN:
                current_translation[1] += 1
            elif event.key == K_w:
                current_translation[2] -= 1
            elif event.key == K_s:
                current_translation[2] += 1

    screen.fill((0, 0, 0))

    # Draw each cube
    for cube in cubes:
        draw_cube(cube)

    pygame.display.flip()
    angle += 0.01
    clock.tick(60)

pygame.quit()
