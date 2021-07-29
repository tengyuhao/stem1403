"""
main
"""

import py200727.game.level.load as levelload
import py200727.game.level.start as levelstart
import py200727.game.level.over as levelover

import py200727.game.image.open as imageopen

import py200727.game.sound.load as soundload

import py200727.game.message as message

# main program of game
print("==== My Game Framework ====")
level = 1
levelload.load_level(level)

img = 'map.jpg'
imageopen.open_image(img)

music = "bgm.mp3"
soundload.load_sound(music)
print()

message.message(100)
print()

# start gaming
levelstart.start_level()
print()

# stop gaming
levelover.over_level()
print()

print("Goodbye! See you next time.")









