import sys
import subprocess

from mc_server_tool.src import (
    args,
    configure_server,
    clear, start_server,
    open_settings,
    download_minecraft_jar,
    install_java_21
)


def main():
    if args.install_java_21:
        install_java_21()

    if args.install:
        if not args.version:
            raise ValueError("You have to choose a version!")
        while True:
            print("Your server settings:")
            print("Version: ", args.version)
            print("Package: ", args.package)
            print("Path: ", args.path)
            print(f"RAM: {args.ram}G")
            print("Port: ", args.port)
            Answer = input("Continue? (Y|N) ").lower()
            if Answer == "y":
                break
            if Answer == "n":
                sys.exit()
            else:
                clear()

        download_minecraft_jar(args.version, args.package, args.path)
        configure_server(args.version, args.package, args.path, args.port, args.ram)

    if args.start:
        start_server(args.path, args.ram, args.version)

    if args.settings:
        open_settings(args.path, args.version, args.package)

    if not args.start and not args.settings and not args.install and not args.install_java_21:
        subprocess.run(["mc-server-tool", "--help"])
