import matplotlib.pyplot as plt
import random

# Define constants for different states
CLEAN = 0
WALL = 1
DIRT = 2

# Define actions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
CLEAN_ACTION = 4
END = 5

# Define the world matrix
world = [
    [WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, CLEAN, CLEAN, CLEAN, CLEAN, WALL],
    [WALL, CLEAN, CLEAN, CLEAN, CLEAN, WALL],
    [WALL, CLEAN, CLEAN, CLEAN, CLEAN, WALL],
    [WALL, CLEAN, CLEAN, CLEAN, CLEAN, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL]
]

# Define the actions matrix
actions_matrix = [
    [END, END, END, END, END, END],
    [END, DOWN, RIGHT, DOWN, CLEAN_ACTION, END],
    [END, DOWN, UP, DOWN, UP, END],
    [END, DOWN, UP, DOWN, UP, END],
    [END, RIGHT, UP, RIGHT, UP, END],
    [END, END, END, END, END, END]
]

def render_world(curr_row, curr_col):
    plt.imshow(world, cmap='cool', vmin=0, vmax=2)
    plt.plot(curr_col, curr_row, '*r', markersize=10)
    plt.xticks([])
    plt.yticks([])
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

def find_next_action(row, col):
    return actions_matrix[row][col]

def simple_agent(row, col):
    if world[row][col] == DIRT:
        return CLEAN_ACTION
    return find_next_action(row, col)

def distribute_dirt():
    for i in range(1, len(world) - 1):
        for j in range(1, len(world[i]) - 1):
            world[i][j] = random.choice([CLEAN, DIRT])

def main():
    curr_row, curr_col = 1, 1
    distribute_dirt()
    render_world(curr_row, curr_col)

    while True:
        action = simple_agent(curr_row, curr_col)
        if action == UP:
            curr_row -= 1
        elif action == DOWN:
            curr_row += 1
        elif action == LEFT:
            curr_col -= 1
        elif action == RIGHT:
            curr_col += 1
        elif action == CLEAN_ACTION:
            world[curr_row][curr_col] = CLEAN

        all_clean = all(all(cell == CLEAN for cell in row) for row in world[1:-1])
        if all_clean:
            action = END
            render_world(curr_row, curr_col)  # Show the final state before termination
            plt.close()  # Close the plot window
            break

        render_world(curr_row, curr_col)

    print("Cleaning is done. Terminating.")

if __name__ == "__main__":
    main()

