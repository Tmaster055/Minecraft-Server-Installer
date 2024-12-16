import subprocess
import os

def configure_server(version: str, package: str, path: str,
                     port: int, ram: int):
    command = [
        "java",
        f"-Xmx{ram}G",
        "-jar",
        f"minecraft_server_{package}_{version}.jar".lower(),
        f"--port {port}",
        "--nogui"
    ]
    subprocess.run(command, cwd=path, check=True, shell=True)
    eula = os.path.join(path, "eula.txt")
    try:
        with open(eula, "r") as file:
            content = file.readlines()

        updated_content = []
        for line in content:
            if "eula=false" in line:
                updated_content.append(line.replace("eula=false", "eula=true"))
            else:
                updated_content.append(line)

        with open(eula, "w") as file:
            file.writelines(updated_content)

        print("The eula was accepted!")
    except FileNotFoundError:
        print(f"The file '{eula}' was not found!")