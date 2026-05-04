# Pixel Runner

## About

**Pixel Runner** is a fun 2D platformer game built with Pygame. The player controls a character that must jump over obstacles (snails and flying enemies) to survive as long as possible. The game features pixel-art graphics, smooth animations, and an endless runner gameplay mechanic with a score system based on survival time.

This project demonstrates clean, modular code architecture and efficient game development practices using object-oriented design principles.

## Screenshots

![Start Screen](ss/start_screen.png)

![Gameplay](ss/gameplay.png)

## Project Structure

The project follows a **modular, object-oriented design** for maintainability and scalability:

- **`pixel_runner.py`** - Main game controller managing game loop, events, and state
- **`player.py`** - Player sprite with jump mechanics and walking animations
- **`obstacle.py`** - Obstacle sprite (snails and flies) with collision detection
- **`background.py`** - Background rendering (sky and ground)
- **`intro_page.py`** - Start screen and game-over display
- **`game_stat.py`** - Score tracking and display
- **`settings.py`** - Centralized configuration for all game parameters
- **`graphics/`** - Sprite assets organized by character type
- **`audio/`** - Background music and sound effects
- **`font/`** - Game fonts

## Code Architecture

This project demonstrates **efficient module-based coding** through:

- **Separation of Concerns**: Each class handles a single responsibility (player movement, obstacle behavior, UI rendering, etc.)
- **Centralized Configuration**: Settings stored in one place for easy tweaking and consistency
- **Reusable Components**: Generic sprite classes that inherit from Pygame's Sprite class
- **Clean Dependencies**: Minimal coupling between modules with clear interfaces
- **Organized Asset Management**: Separate folders for graphics, audio, and fonts for easy asset management

## Getting Started

To run this project, install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run the game:

```bash
python3 pixel_runner.py
```

Built by following [this YouTube tutorial](https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=4812s).
