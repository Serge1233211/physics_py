import tkinter as tk
from tkinter import simpledialog
import pymunk

# Initialize the main window
root = tk.Tk()
root.title("Physics Sandbox")

# Create a Canvas for drawing
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Set up the Pymunk space
space = pymunk.Space()
space.gravity = (0, -981)  # Earth's gravity

# Function to draw objects on the canvas
def draw_objects():
    canvas.delete("all")  # Clear the canvas
    for shape in space.shapes:
        if isinstance(shape, pymunk.Circle):
            x, y = shape.body.position
            r = shape.radius
            canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")
        elif isinstance(shape, pymunk.Poly):
            vertices = [v.rotated(shape.body.angle) + shape.body.position for v in shape.get_vertices()]
            canvas.create_polygon(*sum(([v.x, 400 - v.y] for v in vertices), []), fill="red")
    root.after(50, draw_objects)  # Schedule next drawing

# Function to update the simulation
def update(dt):
    space.step(dt)
    draw_objects()  # Call the draw function

# Set up the simulation update
root.after(20, update, 1/50.0)

# Slider for gravity control
gravity_scale = tk.Scale(root, from_=-2000, to=2000, orient='vertical', label='Gravity')
gravity_scale.pack(side='left')

# Entry for gravity control
gravity_entry = tk.Entry(root)
gravity_entry.pack(side='left')

# Function to update gravity from the entry
def set_gravity(event):
    try:
        new_gravity = float(gravity_entry.get())
        space.gravity = (0, new_gravity)
    except ValueError:
        print("Please enter a valid number for gravity.")

gravity_entry.bind('<Return>', set_gravity)

# Function to change the friction of an object
def change_friction(shape, new_friction):
    shape.friction = new_friction

# Detect object click and change friction
def on_canvas_click(event):
    point_query = space.point_query_nearest((event.x, 400 - event.y), 0, pymunk.ShapeFilter())
    if point_query and point_query.shape:
        # Use Tkinter's simple dialog to ask for new friction value
        new_friction = simpledialog.askfloat("Input", "Enter new friction value for the selected object:",
                                             minvalue=0.0, maxvalue=1.0)
        if new_friction is not None:  # Check if the user entered a value
            change_friction(point_query.shape, new_friction)

canvas.bind('<Button-1>', on_canvas_click)

# Functions to add objects
def add_cube():
    body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    shape = pymunk.Poly.create_box(body, (50, 50))
    space.add(body, shape)

def add_circle():
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 25, (0, 0)))
    shape = pymunk.Circle(body, 25)
    space.add(body, shape)

def add_plane():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Poly.create_box(body, (600, 20))  # Elongated cube at the bottom
    shape.body.position = (300, 10)  # Centered at the bottom of the canvas
    space.add(body, shape)

# Create buttons and assign commands
button_cube = tk.Button(root, text="Add Cube", command=add_cube)
button_cube.pack()

button_circle = tk.Button(root, text="Add Circle", command=add_circle)
button_circle.pack()

button_plane = tk.Button(root, text="Add Plane", command=add_plane)
button_plane.pack()

# Bind keys to the add functions
root.bind('b', lambda event: add_cube())
root.bind('c', lambda event: add_circle())
root.bind('p', lambda event: add_plane())

# Collision handler function
def collision_handler(arbiter, space, data):
    print("Collision detected between two objects!")
    return True

# Add the collision handler to the space
handler = space.add_default_collision_handler()
handler.begin = collision_handler

# Initialize the drawing loop
draw_objects()

# Start the Tkinter event loop
root.mainloop()
