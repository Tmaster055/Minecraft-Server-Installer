import random
import os

#Here are stored all defaults!

DEFAULT_PACKAGE = "Vanilla"
DEFAULT_PATH = os.path.expanduser("~")
DEFAULT_RAM = 4  # Gigabyte
DEFAULT_PORT = 25565
DEFAULT_TIMEOUT = 15  # Seconds

USER_AGENTS = ["", ""] # TODO Add random User Agents

RANDOM_USER_AGENT = random.choice(USER_AGENTS)
