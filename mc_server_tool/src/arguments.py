import argparse
import os

from mc_server_tool.src import (
    DEFAULT_PACKAGE,
    DEFAULT_PORT,
    DEFAULT_PATH,
    DEFAULT_RAM
)


parser = argparse.ArgumentParser(
    description="Minecraft Server Tool Arguments"
)

parser.add_argument(
    "--install",
    action="store_true",
    help="To install a new Server!"
)
parser.add_argument(
    "--start",
    action="store_true",
    help="To start a Server in your path!"
)
parser.add_argument(
    "--settings",
    action="store_true",
    help="To open the settings of the Server in your path!"
)
parser.add_argument(
    "--install_java_21",
    action="store_true",
    help="To install java version 21 to run the server!"
)
parser.add_argument(
    "--version",
    type=str,
    help="Choose a minecraft version e.x 1.20.1, 1.21..."
)
parser.add_argument(
    "--package",
    type=str,
    choices=["Forge", "Fabric", "Paper", "Vanilla", "Spigot", "Pufferfish",
             "Bukkit", "Purpur", "Neoforge", "Quilt", "Folia", "Mohist",
             "Arclight", "Sponge", "BungeeCord"],
    default=DEFAULT_PACKAGE,
    help="Choose a Modloader-Package e.x Forge, Vanilla..."
)
parser.add_argument(
    "--path",
    type=str,
    default=DEFAULT_PATH,
    help="Pick a folder were to save/edit the server!\n"
         "It is creating a new folder in it!\n"
         "e.x C:Users/User/Server (Default is User Directory!)\n"
)
parser.add_argument(
    "--port",
    type=int,
    default=DEFAULT_PORT,
    help="Choose a Port for the Server! Default is 25565"
)
parser.add_argument(
    "--ram",
    type=float,
    default=DEFAULT_RAM,
    help="Choose how many RAM the server may use! Default is 2 Gigabyte!"
)

args = parser.parse_args()


if __name__ == "__main__":
    print(f"Minecraft-Version: {args.version}")
    print(f"Modloader-Package: {args.package}")
    print(f"Server Path: {args.path}")
    print(f"Ram: {args.ram}")
    print(f"Port: {args.port}")
