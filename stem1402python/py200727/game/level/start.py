
#
# import py200727.game.image.change
#


"""
package: level
module: start
"""

import py200727.game.image.open as image_open

print("Welcome to ________ Game. ~~")

def start_level():
    print(f"level.start()")

    img = 'map.jpg'
    image_open.open_image(img)

    img = 'char.png'
    image_open.open_image(img)

    img = 'img1.png'
    image_open.open_image(img)

    img = 'img2.png'
    image_open.open_image(img)



