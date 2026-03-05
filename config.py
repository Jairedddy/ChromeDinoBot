TARGET_SCORE = None

GAME_URL = "https://chromedino.com/"
# Jump when obstacle is this far (px). Lower = jump later (when cactus is closer).
JUMP_DISTANCE = 150
# Obstacles with height >= this need a high jump (long Space hold); else use short tap.
HIGH_JUMP_HEIGHT_THRESHOLD = 50
# Obstacles with width >= this (e.g. multi-cactus) need high jump if height not available.
HIGH_JUMP_WIDTH_THRESHOLD = 50
BIRD_DUCK_HEIGHT = 50

LOOP_DELAY = 0.015
# Match game display: if script shows ~75 when game shows 41, increase divisor (e.g. 40)
SCORE_DIVISOR = 40