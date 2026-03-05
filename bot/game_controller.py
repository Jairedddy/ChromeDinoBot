import time
import config
from bot.obstacle_detector import get_game_state
from bot.actions import jump, duck, start_game

def _need_high_jump(obstacle):
    if obstacle["type"] == "PTERODACTYL":
        return True
    if obstacle.get("height", 0) >= config.HIGH_JUMP_HEIGHT_THRESHOLD:
        return True
    if obstacle.get("width", 0) >= config.HIGH_JUMP_WIDTH_THRESHOLD:
        return True
    return False

def play_game(page):
    
    start_game(page)
    
    print("Game started")
    
    target_reached = False
    last_jump_time = 0
    jump_cooldown_same_obstacle = 0.25  # avoid double-trigger on same obstacle
    last_obstacle_x = None  # allow immediate jump for next cactus

    while True:

        state = get_game_state(page, config.SCORE_DIVISOR)

        score = state["score"]
        obstacle = state["obstacle"]
        trex_x = state["trexX"]

        print(f"\rScore: {int(score)}", end="")

        if score >= config.TARGET_SCORE:
            target_reached = True

        if target_reached:
            time.sleep(config.LOOP_DELAY)
            continue

        if obstacle:

            distance = obstacle["xPos"] - trex_x
            is_new_obstacle = last_obstacle_x is None or abs(obstacle["xPos"] - last_obstacle_x) > 50
            cooldown_ok = (time.time() - last_jump_time) >= jump_cooldown_same_obstacle

            # Jump when close enough, and either cooldown passed or it's a different (next) obstacle
            if distance < config.JUMP_DISTANCE and (cooldown_ok or is_new_obstacle):

                if obstacle["type"] == "PTERODACTYL":

                    if obstacle["yPos"] < config.BIRD_DUCK_HEIGHT:
                        duck(page)
                        last_jump_time = time.time()
                        last_obstacle_x = obstacle["xPos"]
                    else:
                        jump(page, high=True)
                        last_jump_time = time.time()
                        last_obstacle_x = obstacle["xPos"]

                else:
                    jump(page, high=_need_high_jump(obstacle))
                    last_jump_time = time.time()
                    last_obstacle_x = obstacle["xPos"]

        else:
            last_obstacle_x = None  # clear when no obstacle so next one counts as new

        time.sleep(config.LOOP_DELAY)