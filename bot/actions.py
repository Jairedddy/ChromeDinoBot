import time


def start_game(page):
    page.keyboard.press("Space")


def jump(page, high=False):
    """Jump: short tap = low jump (small cacti), longer hold = high jump (tall obstacles)."""
    page.keyboard.down("Space")
    time.sleep(0.14 if high else 0.02)
    page.keyboard.up("Space")


def duck(page):
    page.keyboard.down("ArrowDown")
    time.sleep(0.2)
    page.keyboard.up("ArrowDown")