import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
 .----------------.  .----------------. 
| .--------------. || .--------------. |
| |     _____    | || |    ______    | |
| |    |_   _|   | || |   / ____ `.  | |
| |      | |     | || |   `'  __) |  | |
| |      | |     | || |   _  |__ '.  | |
| |     _| |_    | || |  | \____) |  | |
| |    |_____|   | || |   \______.'  | |
| |              | || |              | |
| '--------------' || '--------------' |
 '----------------'  '----------------' 
"""

def menu():
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("Desea instalar i3, Polybar, Picom, Rofi, Kitty y Scripts?")

    option = input("\n [y/n] >: ")

    if option.casefold() == "y":
        req()
        i3()
        polybar()
    if option.casefold() == "n":
        exit()

def req():
    green()
    print("[+] Instalando requerimientos...\n")

    # Instalando Requerimientos
    os.system("sudo apt-get update -y")
    os.system("sudo apt install net-tools libuv1-dev build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev xte -y")
    os.system("sudo apt install bindsym i3 i3-gaps i3lock-fancy rofi caja feh kitty imagemagick scrot neovim xclip tmux acpi scrub bat fzf wmname dconf-editor -y")

    time.sleep(2)
    print("[+] Requerimientos instalados correctamente.")

def i3():
    green()

    # Create folder for i3  inside of ~/.config
    os.system("cp -r tool/i3 ~/.config/")
    time.sleep(2)
    print("\n[+] Bspwm instalado correctamente")

def polybar():
    green()

    # Install polybar
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.chdir("polybar/")
    os.system("cmake .")
    os.system("make -j$(nproc)")
    os.system("sudo make install")
    os.chdir("..")
    os.system("sudo rm -rf polybar/")

    # Install picom
    os.system("git clone https://github.com/ibhagwan/picom")
    os.chdir("picom/")
    os.system("git submodule update --init --recursive")
    os.system("meson --buildtype=release . build")
    os.system("ninja -C build")
    os.system("sudo ninja -C build install")
    os.chdir("..")
    os.system("sudo rm -rf picom/")

    # Añade el wallpaper
    os.system("mkdir ~/.wallpapers")
    os.system("cp tools/wallpaper.jpg ~/.wallpapers")

    # Configure picom
    os.system("mkdir ~/.config/picom")

    expback = input("\nDesea usear los experimental-backends en picom? Si no se activa se puede detectar lentitud en el equipo al no disponer de una buena GPU. [y/n] -> ")

    if expback.casefold() == "y":
        os.system("cp tools/picom.conf ~/.config/picom")

    if expback.casefold() == "n":
        os.system("cp tools/picom-blur.conf ~/.config/picom/picom.conf")


    # Config for battery.sh ethernet_status.sh hackthebox.sh target_to_hack.sh inside of ~/.config/bin
    os.chdir("tools/bin/")
    os.system("chmod +x *.sh")
    os.system("cp -r bin/ ~/.config/")
    os.system("echo '' > ~/.config/bin/target")
    os.chdir("..")

     # Configure rofi
    os.system("rm -rf ~/.config/rofi")
    os.system("mkdir ~/.config/rofi")
    os.system("mkdir ~/.config/rofi/themes")
    os.system("cp tools/nord.rasi ~/.config/rofi/themes")
    os.system("echo 'rofi.theme: .config/rofi/themes/nord.rasi' > ~/.config/rofi/config")

    # Config for target
    os.system("sudo cp -r tools/scripts/* /bin")
    os.system("sudo chmod +x /bin/settarget")
    os.system("sudo chmod +x /bin/cleartarget")

    # Config for kitty
    os.system("rm -rf ~/.config/kitty")
    os.system("mkdir ~/.config/kitty")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/kitty/kitty.conf -O ~/.config/kitty/kitty.conf")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/kitty/color.ini -O ~/.config/kitty/color.ini")

    # Install Hack Nerd Fonts
    os.system("unzip tools/Hack.zip")
    os.system("sudo mv *.ttf /usr/share/fonts")

    # Config nvim
    os.system("rm -rf ~/.config/nvim/")
    os.system("mkdir ~/.config/nvim")
    os.system("mkdir ~/.config/nvim/colors")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/init.vim -O ~/.config/nvim/init.vim")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/lotus.vim -O ~/.config/nvim/lotus.vim")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/lotusbar.vim -O ~/.config/nvim/lotusbar.vim")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/colors/nord.vim -O ~/.config/nvim/colors/nord.vim")

    # alias & functions
    os.system("cp tools/alias ~/.alias")
    os.system("cp tools/functions ~/.functions")

    # Install lsd
    os.system("sudo dpkg -i tools/lsd.deb")

    # Install oh-my-zsh
    os.system("rm -rf ~/.zshrc")
    os.system("sudo apt install zsh -y")
    os.system("sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\" \"\" --unattended")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions")
    os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-syntax-highlighting")
    os.system("cp tools/zshrc ~/.zshrc")

    # Configure default manager
    os.system("dconf write /org/mate/desktop/session/required-components-list \"['windowmanager', 'dock']\"")
    os.system("dconf write /org/mate/desktop/session/required-components/windowmanager \"'i3'\"")

    time.sleep(2)
    print("\n[+] Polybar instalado correctamente.")
    print("Presione cualquier tecla para cerrar la sesión.")

    input()
    os.system("sudo kill -9 -1")

if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        red()
        print()
        print("[!] No se deber configurar sobre el usuario root")
        print()
    else:
        menu()
