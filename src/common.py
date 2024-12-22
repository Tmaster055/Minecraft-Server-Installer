import subprocess
import os
import platform
import sys


def start_server(path: str, ram: float):
    try:
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                if dir_name.startswith("Minecraft_Server"):
                    server_path = os.path.join(root, dir_name)

                    for file_name in os.listdir(server_path):
                        if file_name.endswith(".jar"):
                            jar_path = os.path.join(server_path, file_name)
                            print(f"Found .jar-File: {jar_path}")
    except FileNotFoundError:
        raise FileNotFoundError("No server folder or jar file found!")

    if not jar_path or not server_path:
        raise FileNotFoundError("No server folder or jar file found!")

    ram = ram * 1000
    command = [
        "java",
        f"-Xmx{int(ram)}m",
        f"-Xms{int(ram)}m",
        "-jar",
        jar_path,
        "--nogui"
    ]
    subprocess.run(command, cwd=server_path, check=True)


def open_settings(path: str):
    try:
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                if dir_name.startswith("Minecraft_Server"):
                    server_path = os.path.join(root, dir_name)

                    for file_name in os.listdir(server_path):
                        if file_name.endswith(".properties"):
                            settings_path = os.path.join(server_path, file_name)
                            print(f"Found settings-File: {settings_path}")
    except FileNotFoundError:
        raise FileNotFoundError("No server folder or settings file found!")

    if not settings_path or not server_path:
        raise FileNotFoundError("No server folder or settings file found!")

    command = [
        "nano",
        settings_path,
    ]
    subprocess.run(command, cwd=server_path, check=True)


def configure_server(version: str, package: str, path: str,
                     port: int, ram: float):
    folder = f"Minecraft_Server_{package}_{version}"
    filename = f"Minecraft_Server_{package}_{version}.jar"
    absolute = os.path.join(path, folder, filename)
    folderpath = os.path.join(path, folder)

    if package == "Forge":
        unpack_forge_server(absolute, folderpath)
    elif package == "Neoforge":
        unpack_neoforge_server(absolute, folderpath)

    ram = ram * 1000
    command = [
        "java",
        f"-Xmx{int(ram)}m",
        f"-Xms{int(ram)}m",
        "-jar",
        absolute,
        "--port",
        str(port),
        "--nogui"
    ]

    subprocess.run(command, cwd=folderpath, check=True)
    eula = os.path.join(path, folder, "eula.txt")
    while True:
        Answer = input("Accept the eula? (Y|N)").lower()
        if Answer == "y":
            break
        if Answer == "n":
            sys.exit()
        else:
            pass
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

    subprocess.run(command, cwd=folderpath, check=True)


def unpack_forge_server(path: str, folder: str):
    command = [
        "java",
        "-jar",
        path,
        "--installServer"
    ]

    subprocess.run(command, cwd=folder, check=True)
    os.remove(path)
    for file_name in os.listdir(folder):
        if file_name.endswith(".jar"):
            jar_path = os.path.join(folder, file_name)
            print(f"Found .jar-File: {jar_path}")
            os.rename(jar_path, path)
    if not jar_path:
        raise ValueError("This Forge version has to be started in the folder\nand is not"
                         "currently supported by this Tool!")


def unpack_neoforge_server(path: str, folder: str):
    command = [
        "java",
        "-jar",
        path,
        "--installServer",
        "--server-jar"
    ]

    subprocess.run(command, cwd=folder, check=True)
    os.remove(path)
    for file_name in os.listdir(folder):
        if file_name.endswith(".jar"):
            jar_path = os.path.join(folder, file_name)
            print(f"Found .jar-File: {jar_path}")
            os.rename(jar_path, path)
    if not jar_path:
        raise ValueError("This Forge version has to be started in the folder\nand is not"
                         "currently supported by this Tool!")


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
