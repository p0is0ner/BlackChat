"""
This file contains all server-side networking processes
must be run by this way:
python server.py <host> <port> <max connections>
"""

import sys  # manage exits and add the path to the modules

# add the path to import database adapter and crypto module
c = sys.path.insert(0, '/home/robot/PycharmProjects/BlackChat/utils/')

from utils import adapter

# ASCII-art banner just for fun :)
print('888888b.   888                   888       .d8888b.  888               888 \n'
      '888  "88b  888                   888      d88P  Y88b 888               888 \n'
      '888  .88P  888                   888      888    888 888               888 \n'
      '8888888K.  888  8888b.   .d8888b 888  888 888        88888b.   8888b.  888888 \n'
      '888  "Y88b 888     "88b d88P"    888 .88P 888        888 "88b     "88b 888 \n'
      '888    888 888 .d888888 888      888888K  888    888 888  888 .d888888 888 \n'
      '888   d88P 888 888  888 Y88b.    888 "88b Y88b  d88P 888  888 888  888 Y88b. \n'
      '8888888P"  888 "Y888888  "Y8888P 888  888  "Y8888P"  888  888 "Y888888  "Y888 \n\n'
      'p0is0n / AKA sad machine / RSA secured TCP chat software, for all CLI lovers <3\n')

