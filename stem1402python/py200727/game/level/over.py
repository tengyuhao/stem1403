"""
package: level
module: over
"""

import py200727.game.image.close as image_close
import py200727.game.sound.pause as sndpause


def over_level():
    print(f"level.over()")

    img = 'map.jpg'
    image_close.close_image(img)

    img = 'char.png'
    image_close.close_image(img)

    img = 'img1.png'
    image_close.close_image(img)

    img = 'img2.png'
    image_close.close_image(img)

    music = 'bgm.mp3'
    sndpause.sound_pause(music)

