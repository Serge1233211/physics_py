# Physics-Based 2D Sandbox

## Overview
This is a simple physics-based 2D sandbox application built using Python, Tkinter for the GUI, and Pymunk for the physics simulation. Users can interact with the simulation by adding objects and adjusting physical properties like gravity and friction.

## How It Works
- **Tkinter** is used to create the application window, canvas, and control elements like buttons and sliders.
- **Pymunk** is the physics engine that simulates gravity, collisions, and other physical interactions.
- The application allows users to add shapes (cubes and circles) and adjust their physical properties.
- A ground plane is present at the bottom to simulate a floor where objects can land.

## Features
- Add dynamic cubes and circles to the simulation.
- Static elongated cube at the bottom acts as the ground plane.
- Gravity control via a slider and text entry.
- Friction adjustment by clicking on an object.
- Real-time collision detection with console output.

## Usage
- Run the script in an environment with Python, Tkinter, and Pymunk installed.
- Use the 'Add Cube', 'Add Circle', and 'Add Plane' buttons to add objects.
- Adjust gravity using the slider or by entering a value and pressing Enter.
- Click on an object to set its friction value through a prompted dialog.
- Observe collisions in the console as they occur during the simulation.

## Keyboard Shortcuts
- 'b': Add a cube.
- 'c': Add a circle.
- 'p': Add a plane.

## Collision Handling
- Collisions between objects are detected and printed to the console.

## Development
- Developed with Python 3.8, Tkinter, and Pymunk 5.7.0.
- Ensure Pymunk is properly installed using `pip install pymunk`.

## License
- This project is open-source and available under the MIT License.
