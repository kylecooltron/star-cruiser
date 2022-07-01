from game.shared.color import Color


# Game grid sizes
COLUMNS = 40
ROWS = 60
CELL_SIZE = 15

# Screen size
MAX_X = 600  # COLUMNS * CELL_SIZE
MAX_Y = 705  # ROWS * CELL_SIZE

# Pyray window settings
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "STAR CRUISER 5000 ✈"

# Colors
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BROWN = Color(165, 42, 42)
BLUE = Color(5, 90, 255)
ORANGE = Color(255, 190, 0)

# Ship shields and damage
STARTSHEILDS = 20
LOWSHIELDS = 5

# Asteroid attributes
ASTEROID_TYPES = [["SML", "`"], ["MED", "*"],
                  ["LRG", "@"], ["SML-xmove", "."], ["HUGE", "@"]]
ASTEROIDSLRG_DAMAGE = 3
ASTEROIDSMED_DAMAGE = 2
ASTEROIDSSML_DAMAGE = 1

ASTEROID_SINGLE_HEALTH = 1
ASTEROIDS_HUGE_HEALTH = 3

# Sound
SHIPFIRE_SOUND = ""
ASTEROIDSEXPLOSION_SOUND = ""
SHIPSEXPLOSION_SOUND = ""
LOWSHIELDSWARNING_SOUND = ""
GAMEOVER_SOUND = ""
