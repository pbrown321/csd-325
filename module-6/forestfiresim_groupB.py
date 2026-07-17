"""Forest Fire Sim, modified by Group B: Aurora Crippen, Christopher Craig,
Lane Dorscher, and Phillip Brown, July 12, 2026
Originally modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation

Group B's modifications:
    - Added a lake near the center of the display (see createLake()).
    - The lake is placed using the same Cartesian (x, y) coordinate system
      the forest grid already uses, the same idea covered in the Mod5
      Cartesian video: x grows to the right, y grows downward, and the
      lake's shape is just every (x, y) point that falls within an
      ellipse centered on the grid.
    - Water is drawn with a new character (WATER = '~') in blue so it's
      visually distinct from trees (green 'A') and fire (red '@').
    - Water tiles are placed once, after the forest is generated, and are
      never touched again by the grow/lightning/burn rules below, so
      they stay put for the entire run.
    - Because fire only spreads to neighboring cells that are currently
      TREE, and a water cell is never TREE, fire cannot cross the lake.
      The lake acts as a natural firebreak.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # (!) Group B: new character for the lake/water feature.

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Group B: Lake settings, in the same Cartesian (x, y) space as the forest.
# The lake is centered roughly in the middle of the display, and LAKE_RX /
# LAKE_RY control how wide and tall the ellipse is (its "radius" along
# each axis). Feel free to change these to reshape or move the lake.
LAKE_CENTER_X = WIDTH // 2
LAKE_CENTER_Y = HEIGHT // 2
LAKE_RX = 10  # horizontal radius of the lake
LAKE_RY = 4   # vertical radius of the lake

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    createLake(forest)  # Group B: place the lake once, after the forest exists.
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees only.
                            # Group B: WATER tiles are never TREE, so this
                            # check already keeps fire from crossing
                            # the lake - the water acts as a firebreak.
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object (this is how WATER
                    # tiles survive unchanged from one step to the next,
                    # since they never match the EMPTY/TREE/FIRE cases
                    # above):
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def createLake(forest):
    """Group B: Carves an elliptical lake into the forest, centered at
    (LAKE_CENTER_X, LAKE_CENTER_Y). Every (x, y) point in the grid whose
    Cartesian distance from that center falls within the ellipse defined
    by LAKE_RX and LAKE_RY becomes WATER. This is called once, before the
    simulation loop starts, so the lake is carved into the forest and
    never regenerated or altered afterward.
    """
    for x in range(forest['width']):
        for y in range(forest['height']):
            # Standard ellipse equation: ((x-cx)/rx)^2 + ((y-cy)/ry)^2 <= 1
            dx = (x - LAKE_CENTER_X) / LAKE_RX
            dy = (y - LAKE_CENTER_Y) / LAKE_RY
            if (dx ** 2) + (dy ** 2) <= 1:
                forest[(x, y)] = WATER


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                # Group B: draw the lake in blue.
                bext.fg('blue')
                print(WATER, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
