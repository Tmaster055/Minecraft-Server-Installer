# Minecraft-Server-Installer
## Description
This Tool is made for an easy Minecraft Server Setup!
You can easily install a Minecraft Server with over 10 different packages
and nearly all Versions out there!
## Getting started

- ### Installation
Run this command in your command prompt!
```shell
pip install mc_server_tool
```
To update:
```shell
pip install -U mc_server_tool
```
- ### Documentation
```shell
mc_server_tool --help
```
```
usage: execute.py [-h] [--install] [--start] [--settings] [--install_java_21] [--version VERSION]
                  [--package {Forge,Fabric,Paper,Vanilla,Spigot,Pufferfish,Bukkit,Purpur,Neoforge,Quilt}]
                  [--path PATH] [--port PORT] [--ram RAM]

Minecraft Server Tool Arguments

options:
  -h, --help            show this help message and exit
  --install             To install a new Server!
  --start               To start a Server in your path!
  --settings            To open the settings of the Server in your path!
  --install_java_21     To install java version 21 to run the server!
  --version VERSION     Choose a minecraft version e.x 1.20.1, 1.21...
  --package {Forge,Fabric,Paper,Vanilla,Spigot,Pufferfish,Bukkit,Purpur,Neoforge,Quilt}
                        Choose a Modloader-Package e.x Forge, Vanilla...
  --path PATH           Pick a folder were to save/edit the server! It is creating a new folder in it! e.x
                        C:Users/User/Server (Default is User Directory!)
  --port PORT           Choose a Port for the Server! Default is 25565
  --ram RAM             Choose how many RAM the server may use! Default is 2 Gigabyte!
```
- ### Examples
Installs a server with version 1.20.4:
```shell
mc_server_tool --install --version 1.20.4 
```
Installs a server with version 1.20.4 on Paper:
```shell
mc_server_tool --install --version 1.20.4 --package Paper
```
Installs and starts the server with 5G max ram usage:
```shell
mc_server_tool --install --version 1.20.4 --ram 5
```
Installs with the port 27767:
```shell
mc_server_tool --install --version 1.20.4 --port 27767
```
Starts your server again:
```shell
mc_server_tool --start
```
Starts your Forge server if you have multiple servers in one folder:
```shell
mc_server_tool --start --package Forge
```
You can also specify the path on start and installation: 
```shell
mc_server_tool --start --path /home/user/downloads
```
You also let install java 21:
```shell
mc_server_tool --install_java_21
```
### Package Support 
| Supported Packages | Status | Supported Packages | Status                                                                     |
|--------------------|-------|---------------------|----------------------------------------------------------------------------|
| Vanilla            | ✔️    | Forge               | ➖ (installing is fine but <br> starting and configuring <br> may not work) |
| Paper              | ✔️    | Neoforge            | ✔️                                                                         |
| Spigot             | ✔️    | Fabric              | ✔️                                                                         |
| Bukkit             | ✔️    | Pufferfish          | ✔️                                                                         |
| Quilt              | ✔️    | Purpur              | ✔️                                                                         |

### Upcoming Tasks
  - [x] Make Forge work
  - [x] Make Neoforge work
  - [ ] Make starting easier with package and version
  - [ ] Implement more different error messages
  - [ ] Add support for more packages
## Support 
If you see any issues you can open one in github or contact me on discord
with the Username`Tmaster055`!