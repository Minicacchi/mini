import arcade
# from arcade import *

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.sprite = None
        self.playerSpriteList = arcade.SpriteList()

        self.setup()

    def setup(self):
        
        self.sprite = arcade.Sprite("C:\\Users\\riccardo.cian\\Downloads\\FREE_Samurai 2D Pixel Art v1.2\\FREE_Samurai 2D Pixel Art v1.2\Sprites\IDLE.png")

        self.sprite.center_x = 300
        self.sprite.center_y = 300
        self.sprite.scale_x = 5.0
        self.sprite.scale_y = 5.0

        self.playerSpriteList.append(self.sprite)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.rect_size = 50
        if key == arcade.key.W:
            self.rect_y+=10
        if key == arcade.key.A:
            self.rect_x-=10
        if key == arcade.key.D:
            self.rect_x+=10
        if key == arcade.key.S:
            self.rect_y-=10    

    def on_draw(self):
        self.playerSpriteList.draw()
        
    def on_update(self, deltaTime):
        self.sprite.center_x += 1




def main():
    game = MyGame(
        600, 600, "Il mio giochino"
    )
    arcade.run()


if __name__ == "__main__":
    main()

