# bhop-pro-recreation
THis is a py/js bhop recreation
# Bhop Pro Recreation

## Overview
This project is a complete recreation of the mobile game *Bhop Pro* built using the **Ursina Engine**. The game features 5 levels with all original mechanics and gameplay features fully integrated. The recreation includes AI-generated knife models, player movement mechanics, level design, and other core gameplay elements found in the original game. 

The game is developed with single-player mode only, focusing on a realistic and responsive parkour experience.

## Features
- **5 levels** with varying difficulty.
- **Player movement**: Bhop (bunny hopping), smooth acceleration, and deceleration.
- **AI-generated knife model** for player use.
- **Fully integrated gameplay features**: 
  - Health system.
  - Timer system.
  - Level completion tracking.
- **AI-generated knife models** designed for enhanced realism.
- **Ursina Engine** framework used for the game’s physics, rendering, and environment.

## Installation

### Prerequisites
Make sure you have the following software installed before running the game:

- **Python 3.x**: Ensure Python is installed on your machine. If not, download and install it from [Python's website](https://www.python.org/).
- **Ursina Engine**: The game is built on the Ursina Engine, which you can install via pip.

### Setup
To set up the game locally, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/bhop_pro_recreation.git
    cd bhop_pro_recreation
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download or create the knife model via AI if not already present. The knife models are integrated into the game and should be stored in the `assets/knives` folder.

4. Run the game:
    ```bash
    python main.py
    ```

The game will launch, and you can start playing with all features and levels intact.

## Gameplay

### Objective
The goal of the game is to complete all five levels by bunny hopping through obstacles, collecting coins, and reaching the finish line in the fastest time possible.

### Controls
- **W, A, S, D**: Move forward, left, backward, and right.
- **Spacebar**: Jump.
- **Mouse**: Look around.
- **Esc**: Pause the game and access the menu.

### Features
- **Bunny Hop Mechanics**: Players must use the bunny hop technique to progress through levels quickly. This includes a momentum-based system to allow for smooth and fluid movement.
- **Knife Model**: The knife is generated using AI and is automatically assigned to the player character. It can be equipped, and animations for swinging the knife are integrated into the game.
- **Level Progression**: Each level is designed to increase in difficulty, requiring the player to master the bunny hop technique.
- **Timer System**: Each level has a timer that tracks how fast the player completes it. The goal is to finish each level as fast as possible to unlock the next one.
- **Health System**: The player has a health bar that depletes upon colliding with obstacles or falling off the level.
  


### Key Components

- **`game.py`**: Handles the main game loop, scene management, and setup.
- **`player.py`**: Contains player movement code, including bunny hopping logic.
- **`level.py`**: Manages the level design, including obstacles and level progression.
- **`timer.py`**: Tracks and displays the time taken to complete each level.

## Level Design

Each level is designed with increasing difficulty. The levels include:

1. **Level 1**: Basic jumping and obstacle avoidance.
2. **Level 2**: Includes moving obstacles and higher jumps.
3. **Level 3**: Complex jumps with tight timing and obstacles.
4. **Level 4**: Long jumps with different platforms and walls to navigate.
5. **Level 5**: The hardest level with a combination of all mechanics and tight timing.

The levels are created using the Ursina Engine’s entity system and designed to provide an optimal challenge for players mastering bunny hopping.

## AI-Generated Knife Model

The knife model is generated using AI tools that ensure it matches the aesthetic of the original *Bhop Pro*. The knife is integrated into the player’s inventory and can be swung using designated controls. 

- The model is in **GLTF** format and is stored in the `assets/knives` folder.
- The knife’s animations are also included in the game files, providing a smooth and natural swinging motion.

## Future Plans

- **Multiplayer Mode**: Integrate multiplayer support for a competitive Bhop race mode.
- **Level Editor**: Allow players to design and upload their custom levels.
- **AI Opponents**: Create AI-controlled players to race against in future updates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to the project or report any bugs or issues you encounter. For any support or inquiries, please contact the project maintainers.


MAkKE IT IN JS IF EASIER
a
