"""
A simple platformer game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Platformer game"

# Scaling factors
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Height and width of the tiles we will place
TILE_H = int(128 * TILE_SCALING) # = 64
TILE_W = int(128 * TILE_SCALING) # = 64

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

        self.player_list = None
        self.wall_list = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        # "Spacial hashing" speeds the time it takes to find collisions,
        # but it increases the time it takes to move a sprite.

        # Set up the player
        image_source = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Create the ground
        # Using a loop to place multiple sprites horizontally
        y = TILE_H // 2
        for x in range(0, 1200, TILE_W):
            image_source = ":resources:images/tiles/grassMid.png"
            wall = arcade.Sprite(image_source, TILE_SCALING)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)
        
        # Put some crates on the ground
        # Using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]
        for coordinate in coordinate_list:
            # Add a crate on the ground
            image_source = ":resources:images/tiles/boxCrate_double.png"
            wall = arcade.Sprite(image_source, TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()
        
        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
