import matplotlib.pyplot as plt
import random
import os

WIDTH = 100
HEIGHT = 100

def generate_building (ax, x):

    base_height = random.randint (20, 80)
    width = random.uniform (2, 6)


    rect = plt.Rectangle((x, 0), width, base_height, color=(random.random()*0.5, random.random()*0.5, random.random()*0.5))

    ax.add_patch (rect)

    for y in range (2, base_height, 4):
        if random.random() < 0.7:
            win = plt.Rectangle((x+width*0.2, y), width*0.2, 1, color="yellow")
            ax.add_patch(win)
    
    if random.random() < 0.6:
        tower_height = random.randint(5, 20)
        tower = plt.Rectangle((x + width/3, base_height), width/3, tower_height, color="black")
        ax.add_patch(tower)

def generate_city(seed=None):

    if seed:
        random.seed(seed)
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    ax.set_facecolor("black")

    x = 0

    while x < WIDTH:
        generate_building(ax, x)

        x += random.uniform(3, 8)
    ax.axis("off")
    return fig

def save_city():
    if not os.path.exists("gallery"):
        os.mkdir ("gallery")
    
    seed = random.randint (0, 100000)
    fig = generate_city(seed)
    filename = f"gallery/city_{seed}.png"

    plt.savefig(filename, bbox_inches="tight", pad_inches=0)
    plt.close()

    print ("Saved:", filename)

if __name__ == "__main__":
    save_city()