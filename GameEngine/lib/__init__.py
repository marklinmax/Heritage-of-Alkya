import os

from . import logger
from . import console

if "portforwardlib.py" in os.listdir():   
    from . import portforwardlib
