# DinoHacked

An automated bot that plays the Chrome Dinosaur Game using browser automation. It detects obstacles in real time via JavaScript injection and reacts with jumps or ducks to achieve a target score.

## How It Works

1. **Launches a Chromium browser** using Playwright and navigates to the dino game.
2. **Reads game state** by evaluating JavaScript against the game's internal `Runner` instance, extracting the current score, speed, T-Rex position, and nearest obstacle data.
3. **Decides actions** based on obstacle type and proximity:
   - **Cactus** — Jumps when within configured distance.
   - **Pterodactyl** — Ducks if flying low, jumps otherwise.
4. **Stops reacting** once the target score is reached, letting the dino run into the next obstacle.

## Project Structure

```
DinoHacked/
├── main.py                  # Entry point — prompts for target score, launches the bot
├── config.py                # Tunable parameters (distances, delays, game URL)
├── browser/
│   └── launcher.py          # Playwright browser setup and page navigation
├── bot/
│   ├── game_controller.py   # Main game loop — reads state, triggers actions
│   ├── obstacle_detector.py # JS evaluation to extract live game state
│   └── actions.py           # Keyboard actions (jump, duck, start)
├── utils/
│   └── helpers.py           # Utility functions
└── requirements.txt
```

## Prerequisites

- **Python** 3.10+
- **Playwright** with Chromium browser binaries

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd DinoHacked

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install chromium
```

## Usage

```bash
python main.py
```

You will be prompted to enter a target score. The bot will play the game automatically and stop reacting once the target is reached.

## Configuration

All tunable parameters are in [`config.py`](config.py):

| Parameter        | Default                      | Description                                          |
|------------------|------------------------------|------------------------------------------------------|
| `GAME_URL`       | `https://chromedino.com/`    | URL of the dino game                                 |
| `JUMP_DISTANCE`  | `120`                        | Pixel distance at which the bot jumps over obstacles  |
| `BIRD_DUCK_HEIGHT`   | `50`                    | Y-position threshold for ducking under pterodactyls   |
| `LOOP_DELAY`     | `0.015`                      | Seconds between each game-state poll (lower = faster) |

## Limitations

- Relies on the internal `Runner` API of the Chrome Dino game. Changes to the game's source may break obstacle detection.
- Reaction timing is dependent on system performance and `LOOP_DELAY` — very high game speeds may outpace the bot.
- The `chrome://dino/` URL does not work with Playwright; a hosted version of the game is used instead.

## License

This project is intended for educational and entertainment purposes only.
