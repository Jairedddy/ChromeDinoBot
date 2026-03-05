from browser.launcher import launch_browser
from bot.game_controller import play_game
import config

def main():
    target = int(input("Enter target score: "))
    config.TARGET_SCORE = target
    
    browser, page = launch_browser()
    
    play_game(page)
    
if __name__ == "__main__":
    main()