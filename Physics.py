import tkinter as tk
import pymunk
from pymunk.vec2d import Vec2d

# Initialize the Pymunk space
space = pymunk.Space()
space.gravity = 0, -981

# Function to add objects to the space
def add_object(shape_type, position, size=50):
    if shape_type == 'cube':
        body = pymunk.Body(1, pymunk.moment_for_box(1, (size, size)))
        shape = pymunk.Poly.create_box(body, (size, size))
    elif shape_type == 'circle':
        body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, size/2))
        shape = pymunk.Circle(body, size/2)
    body.position = position
    space.add(body, shape)

# Function to add a static ground plane to the space
def add_ground_plane(position_y, space, length=600, thickness=5):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (-length/2, position_y), (length/2, position_y), thickness)
    shape.friction = 1.0
    space.add(body, shape)
    return shape

# Add the ground plane at a specific Y position
ground_plane = add_ground_plane(position_y=50, space=space)

# Function to update the simulation
def update(dt):
    space.step(dt)
    for shape in space.shapes:
        if isinstance(shape, pymunk.Poly):
            # Update cubes
            pass
        elif isinstance(shape, pymunk.Circle):
            # Update circles
            pass

# Tkinter GUI setup
root = tk.Tk()
root.title("Physics-Based 2D Sandbox")

# Add a canvas
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Bind keyboard shortcuts
root.bind('b', lambda event: add_object('cube', (300, 50)))
root.bind('c', lambda event: add_object('circle', (300, 50)))
root.bind('p', lambda event: add_ground_plane(50, space))

# Main loop
def main():
    while True:
        update(1/50.0)
        root.update_idletasks()
        root.update()

# Run the application
main()
