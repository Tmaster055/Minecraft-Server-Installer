import argparse
import os


parser = argparse.ArgumentParser(
    description="Minecraft Server Tool Arguments"
)

parser.add_argument(
    "--version",
    type=str,
    required=True,
    help="Choose a minecraft version e.x 1.20.1, 1.21..."
)
parser.add_argument(
    "--package",
    type=str,
    choices=["Forge", "Fabric", "Paper", "Vanilla", "Spoigot"],
    default="Vanilla",
    help="Choose a Modloader-Package e.x Forge, Vanilla..."
)
parser.add_argument(
    "--path",
    type=str,
    default=os.path.join(os.path.expanduser("~"), "Minecraft_Server"),
    help="Pick a folder were to save/edit the server!\ne.x C:Users/User/Server (Default is User Directory!)"
)

args = parser.parse_args()


if __name__ == "__main__":
    print(f"Minecraft-Version: {args.version}")
    print(f"Modloader-Package: {args.package}")
    print(f"Server Path: {args.path}")
