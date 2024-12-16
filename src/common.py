import subprocess
import os
import platform


def configure_server(version: str, package: str, path: str,
                     port: int, ram: float):
    absolute = os.path.join(path, f"minecraft_server_{package}_{version}.jar".lower())
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
    eula = os.path.join(path, "eula.txt")
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
