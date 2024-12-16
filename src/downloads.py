import requests
import os

def download_minecraft_jar(version: str, package: str, path: str):
    url = f"https://serverjar.org/download/{package}/{version}".lower()
    filename = f"minecraft_server_{package}_{version}.jar".lower()
    path = os.path.join(path, filename)

    try:
        print(f"Download was started to: {path}")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded jar to: {path}")
    except requests.exceptions.RequestException:
        raise ValueError("Failed to download jar!")


def install_java_21():
    pass


if __name__ == "__main__":
    download_minecraft_jar("1.20.4", "Vanilla", "/home/tobias/Downloads")
