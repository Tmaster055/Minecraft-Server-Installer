import os
import re
import requests
from bs4 import BeautifulSoup


def download_minecraft_jar(version: str, package: str, path: str):
    url = f"https://serverjar.org/download/{package}/{version}".lower()

    response = requests.get(url, timeout=15)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    script_tags = soup.find_all('script')

    for script in script_tags:
        script_content = script.string
        if script_content:
            match = re.search(r"window\.location\.href = '(https://[^\']+)'", script_content)
            if match:
                url = match.group(1)
                break

    folder = f"minecraft_server_{package}_{version}"
    filename = f"minecraft_server_{package}_{version}.jar".lower()
    path = os.path.join(path, folder, filename)

    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        print(f"Download was started to: {path}")
        response = requests.get(url, stream=True, timeout=15)
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
