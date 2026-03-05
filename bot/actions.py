import time


def start_game(page):
    page.keyboard.press("Space")


def jump(page):
    page.keyboard.press("Space")


def duck(page):
    page.keyboard.down("ArrowDown")
    time.sleep(0.2)
    page.keyboard.up("ArrowDown")