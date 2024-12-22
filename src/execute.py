import sys

from arguments import args
from common import configure_server, clear, start_server, open_settings
from downloads import download_minecraft_jar, install_java_21


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
    start_server(args.path, args.ram)

if args.settings:
    open_settings(args.path)
