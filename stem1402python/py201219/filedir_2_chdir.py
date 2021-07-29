"""
change current director

absolute path
"""

import os

current_path = os.getcwd()
print(current_path)

os.chdir(r"/Users/kevinteng/PycharmProjects/stem1402b")

current_path = os.getcwd()
print(current_path)
