import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.shields import Shields
from game.casting.ship import Ship
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.handle_enemy_creation import HandleEnemyCreation
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()

    # create player ship
    cast.add_actor("ships", Ship())
    # create display elements
    scores = Score()
    shields = Shields()
    scores.set_color(constants.WHITE)
    shields.set_color(constants.WHITE)
    cast.add_actor("scores", scores)
    cast.add_actor("shields", shields)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(keyboard_service))
    script.add_action("update", HandleEnemyCreation())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
