import subprocess
import os
import platform
import sys


def start_server(path: str):
    try:
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                if dir_name.startswith("minecraft_server"):
                    server_path = os.path.join(root, dir_name)

                    for file_name in os.listdir(server_path):
                        if file_name.endswith(".jar"):
                            jar_path = os.path.join(server_path, file_name)
                            print(f"Found .jar-File: {jar_path}")
    except FileNotFoundError:
        raise FileNotFoundError("No server folder or jar file found!")

    if not jar_path or not server_path:
        raise FileNotFoundError("No server folder or jar file found!")

    command = [
        "java",
        "-jar",
        jar_path,
        "--nogui"
    ]
    subprocess.run(command, cwd=server_path, check=True)


def open_settings(path: str):
    try:
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                if dir_name.startswith("minecraft_server"):
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
    folder = f"minecraft_server_{package}_{version}"
    filename = f"minecraft_server_{package}_{version}.jar".lower()
    absolute = os.path.join(path, folder, filename)
    folderpath = os.path.join(path, folder)
    command = [
        "java",
        f"-Xmx{ram}G",
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


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
