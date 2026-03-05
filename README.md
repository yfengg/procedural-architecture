# procedural-architecture
# Procedural City Generator

A small Python project that generates random city skylines using procedural generation techniques.

Each time the program runs, it creates a unique skyline made of randomly sized buildings, windows, and antenna towers, then saves the result as an image.

The project demonstrates basic concepts used in procedural generation systems commonly found in simulation software and games.

Features

- Randomly generated building heights and widths
- Nighttime skyline aesthetic
- Randomized window lighting
- Optional antenna towers on buildings
- Deterministic generation using seeds
- Automatic export of generated images

Each run produces a new skyline image saved to the `gallery/` directory.

Example Output

Running the generator produces images like:
gallery/city_48321.png
gallery/city_92014.png
gallery/city_12773.png


Each image corresponds to the random seed used to generate that city.

Installation

Clone the repository:

git clone https://github.com/yourusername/procedural-architecture.git
cd procedural-architecture


Install dependencies:

pip install -r requirements.txt


Usage

Run the generator:

python generate_city.py

The script will create a skyline image and save it in the `gallery/` folder.

Example output:

Saved: gallery/city_48291.png

Project Structure

procedural-architecture/
│
├── generate_city.py      # main skyline generator
├── gallery/              # output images
├── requirements.txt      # Python dependencies
└── README.md


Concepts Demonstrated

This project demonstrates several programming and graphics concepts:

- Procedural generation
- Randomized simulation
- 2D graphics using Matplotlib
- Deterministic world generation via seeds
- Programmatic image export

Procedural generation is commonly used in simulation and game development to create large environments automatically.

How It Works

The skyline is generated using a simple procedural generation approach based on randomized parameters.

 1. Coordinate System

The city is generated inside a fixed 2D coordinate space:

- Width: 100 units
- Height: 100 units

Buildings are placed sequentially along the x-axis until the width of the city is filled.

2. Building Generation

Each building is generated using randomized attributes:

- Height: random integer between 20 and 80
- Width: random float between 2 and 6

Buildings are rendered as rectangles using Matplotlib patches.

3. Window Generation

Windows are placed along the building height using a vertical loop:

- Window spacing: every 4 units
- Window probability: 70%

This creates the appearance of randomly lit buildings at night.

4. Tower Generation

Some buildings receive antenna towers.

Probability of tower placement: 60%

Tower height is randomly chosen between 5 and 20 units.

5. Deterministic Generation (Seeds)

Each skyline is associated with a random seed.

If the same seed is reused, the same skyline will be generated.
This technique is commonly used in procedural world generation systems.

Example:
seed = 12345

will always produce the same city layout.

6. Rendering

The skyline is rendered using Matplotlib and exported as a PNG image.

The final image is saved to the `gallery/` directory.

Future Improvements

Possible extensions for this project include:

- Procedural road networks
- Multiple building styles or districts
- Day/night lighting systems
- 3D building generation
- Animated city growth