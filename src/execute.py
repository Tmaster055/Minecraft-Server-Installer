from arguments import args
from common import configure_server, clear
from downloads import download_minecraft_jar

while True:
    print("Your server settings:")
    print("Version: ", args.version)
    print("Package: ", args.package)
    print("Path: ", args.path)
    print(f"RAM: {args.ram}G")
    print("Port: ", args.port)
    Answer = input("Continue? (Y|N)").lower()
    if Answer == "y":
        break
    elif Answer == "n":
        quit()
    else:
        clear()

download_minecraft_jar(args.version, args.package, args.path)
configure_server(args.version, args.package, args.path, args.port, args.ram)
