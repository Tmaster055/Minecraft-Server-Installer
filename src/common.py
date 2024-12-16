import subprocess
import os
import platform
import sys


def start_server(path: str):
    print(f"Searching {path} after Minecraft-Server-Files...")
    server_file = None

    for file in os.listdir(path):
        if "minecraft_server" in file and file.endswith(".jar"):
            server_file = file
            break

    if not server_file:
        raise ValueError("No server jar found!")

    print(f"Found file: {server_file}")

    command = [
        "java",
        "-jar",
        absolute,
        "--nogui"
    ]
    subprocess.run(command, cwd=path, check=True)


def configure_server(version: str, package: str, path: str,
                     port: int, ram: float):
    folder = f"minecraft_server_{package}_{version}"
    filename = f"minecraft_server_{package}_{version}.jar".lower()
    absolute = os.path.join(path, folder, filename)
    command = [
        "java",
        f"-Xmx{ram}G",
        "-jar",
        absolute,
        "--port",
        str(port),
        "--nogui"
    ]
    subprocess.run(command, cwd=path, check=True)
    eula = os.path.join(path, folder, "eula.txt")
    try:
        with open(eula, "r", encoding="utf-8") as file:
            content = file.readlines()

        updated_content = []
        for line in content:
            if "eula=false" in line:
                updated_content.append(line.replace("eula=false", "eula=true"))
            else:
                updated_content.append(line)

        with open(eula, "w", encoding="utf-8") as file:
            file.writelines(updated_content)

        print("The eula was accepted!")
    except FileNotFoundError:
        print(f"The file '{eula}' was not found!")

    subprocess.run(command, cwd=path, check=True)


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
