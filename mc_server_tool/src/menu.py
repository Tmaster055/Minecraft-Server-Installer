import sys
import time

from mc_server_tool.src import clear, PACKAGES, args, download_minecraft_jar, configure_server


def start_installing_menu():
    print("Welcome to the Minecraft Installer! We are now installing a server!")
    version = input("Which Minecraft version? ")

    while True:
        clear()
        try:
            counter = 1
            list = []
            for package in PACKAGES:
                answer = package + f"({counter})"
                list.append(answer)
                counter += 1
            print(list)
            package = int(input("Choose one of the packages! "))
            package -= 1
            package = PACKAGES.pop(package)
            break
        except ValueError:
            print("Should be valid a number!")
            time.sleep(1)
        except IndexError:
            print("Should be valid a number!")
            time.sleep(1)

    while True:
        clear()
        answer = input("Want to specify your the server path? (Y|N) ").lower()
        if answer == "y":
            path = input("Which path should be used? ")
            break
        if answer == "n":
            path = args.path
            break

    while True:
        clear()
        try:
            answer = input("Want to specify your max ram usage? (Y|N) ").lower()
            if answer == "y":
                ram = float(input("How many Gigabyte of ram should be used max? "))
                break
            if answer == "n":
                ram = args.ram
                break
        except ValueError:
            print("Should be a number!")
            time.sleep(1)

    while True:
        clear()
        try:
            answer = input("Want to specify a port? (Y|N) ").lower()
            if answer == "y":
                port = int(input("Which port should be used? "))
                break
            if answer == "n":
                port = args.port
                break
        except ValueError:
            print("Should be a number!")
            time.sleep(1)

    while True:
        print("Your server settings:")
        print("Version: ", version)
        print("Package: ", package)
        print("Path: ", path)
        print(f"RAM: {ram}G")
        print("Port: ", port)
        answer = input("Continue? (Y|N) ").lower()
        if answer == "y":
            break
        if answer == "n":
            sys.exit()
        else:
            clear()

    download_minecraft_jar(version, package, path)
    configure_server(version, package, path, port, ram)


if __name__ == "__main__":
    start_installing_menu()
