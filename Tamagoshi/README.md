# Tamagoshi Game

Welcome to the Tamagoshi game! This is a virtual pet simulation where you can take care of your own digital pet, interact with it, and watch it grow. 

## Project Structure

The project is organized into the following files:

- **src/tamagoshi.py**: Contains the main class `BichinhoVirtual`, which manages the virtual pet's attributes and interactions. It includes methods for displaying the pet's status, altering its attributes, and handling user interactions.

- **src/graphics.py**: Responsible for managing the graphical representation of the game. This file includes functions to draw the pet, display the game interface, and handle animations or visual effects.

- **src/actions.py**: Defines various actions that the player can perform with the virtual pet. This includes functions for feeding, playing, training, and other interactions that affect the pet's state.

- **src/utils.py**: Contains utility functions that support the main game logic, such as random event generation, saving and loading game progress, and other helper functions.

- **requirements.txt**: Lists the dependencies required for the project, specifying the libraries needed to run the game.

## Gameplay

In Tamagoshi, you will:

1. **Create Your Pet**: Choose a name for your virtual pet and start your journey.
2. **Interact**: Feed, play, and take care of your pet to keep it happy and healthy.
3. **Monitor Status**: Keep an eye on your pet's hunger, health, humor, and age.
4. **Complete Challenges**: Achieve milestones and complete challenges as your pet grows.
5. **Save Progress**: Save your game progress and load it later to continue your adventure.

## Setup Instructions

To run the Tamagoshi game, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` using the command:
   ```
   pip install -r requirements.txt
   ```
4. Run the game by executing the `tamagoshi.py` file:
   ```
   python src/tamagoshi.py
   ```

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are welcome!

## License

This project is open-source and available under the MIT License. Enjoy taking care of your virtual pet!