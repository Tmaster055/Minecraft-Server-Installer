import os
import re
import sys
import platform
import subprocess
import requests
from bs4 import BeautifulSoup


def download_minecraft_jar(version: str, package: str, path: str):
    if package == "Forge":
        url = get_forge_link(version)
    elif package == "Neoforge":
        url = get_neoforge_link(version)
    else:
        url = get_serverjar_link(version, package)

    folder = f"Minecraft_Server_{package}_{version}"
    filename = f"Minecraft_Server_{package}_{version}.jar"
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


def get_serverjar_link(version: str, package: str):
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
                return url


def get_forge_link(version: str):
    url = f"https://files.minecraftforge.net/net/minecraftforge/forge/index_{version}.html"
    response = requests.get(url)
    response.raise_for_status()
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    version_tags = soup.find_all('td', class_='download-version')
    for version_tag in version_tags:
        if version_tag.find('i', class_='promo-latest'):
            forge_version = version_tag.text.strip()
            link = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{version}-{forge_version}/forge-{version}-{forge_version}-installer.jar"
            return link


def get_neoforge_link(version: str):
    formatted_version = version.lstrip('1.')

    url = 'https://maven.neoforged.net/releases/net/neoforged/neoforge'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    highest_version = None
    highest_value = -1
    is_beta = False

    for link in links:
        pattern = rf"\./({re.escape(formatted_version)}\.(\d+))(-beta)?/"

        match = re.match(pattern, link['href'])

        if match:
            version_number = int(match.group(2))
            version_with_beta = match.group(1)
            beta_suffix = match.group(3)

            if version_number > highest_value:
                highest_value = version_number
                highest_version = version_with_beta
                is_beta = beta_suffix is not None

    if highest_version:
        beta_suffix = '-beta' if is_beta else ''
        link = f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{highest_version}{beta_suffix}/neoforge-{highest_version}{beta_suffix}-installer.jar"
        return link
    else:
        return None


def install_java_21():
    def detect_package_manager():
        package_managers = ["apt", "dnf", "yum", "pacman", "zypper"]
        for manager in package_managers:
            if subprocess.call(["which", manager], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                return manager
        return None

    system = platform.system()

    if system == "Windows":
        print("Installing Java 21 on Windows...")
        subprocess.run(["winget", "install", "-e", "--id", "Oracle.JDK.21"], check=True)

    elif system == "Darwin":  # macOS
        print("Installing Java 21 on macOS...")
        subprocess.run(["brew", "install", "openjdk@21"], check=True)
        subprocess.run(["sudo", "ln", "-s", "/usr/local/opt/openjdk@21/libexec/openjdk.jdk",
                        "/Library/Java/JavaVirtualMachines/openjdk-21.jdk"], check=True)

    elif system == "Linux":
        print("Installing Java 21 on Linux...")
        package_manager = detect_package_manager()
        if not package_manager:
            print("No supported package manager found on this system.")
            sys.exit(1)

        if package_manager == "apt":
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "openjdk-21-jdk"], check=True)
        elif package_manager in ["dnf", "yum"]:
            subprocess.run(["sudo", package_manager, "install", "java-21-openjdk"], check=True)
        elif package_manager == "pacman":
            subprocess.run(["sudo", "pacman", "-S", "jdk-openjdk"], check=True)
        elif package_manager == "zypper":
            subprocess.run(["sudo", "zypper", "install", "java-21-openjdk"], check=True)
        else:
            print(f"Unsupported package manager: {package_manager}")
            sys.exit(1)

    else:
        print(f"Unsupported operating system: {system}")
        sys.exit(1)

    print("Java 21 installed successfully!")


if __name__ == "__main__":
    download_minecraft_jar("1.20.4", "Vanilla", "/home/tobias/Downloads")
    print(get_neoforge_link("1.21.1"))