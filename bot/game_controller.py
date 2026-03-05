import time
import config
from bot.obstacle_detector import get_game_state
from bot.actions import jump, duck, start_game

def play_game(page):
    
    start_game(page)
    
    print("Game started")
    
    target_reached = False
    
    while True:
        
        state = get_game_state(page)
        
        score = state["score"]
        obstacle = state["obstacle"]
        trex_x = state["trexX"]
        
        print(f"\rScore: {int(score)}", end="")
        
        if score >= config.TARGET_SCORE:
            target_reached = True
            
        if target_reached:
            continue
        
        if obstacle:
            
            distance = obstacle["xPos"] - trex_x
            
            if distance < config.JUMP_DISTANCE:
                
                if obstacle["type"] == "PTERODACTYL":
                    
                    if obstacle["yPos"] < config.BIRD_DUCK_HEIGHT:
                        duck(page)
                    else:
                        jump(page)
                        
                else:
                    jump(page)
            
        time.sleep(config.LOOP_DELAY)