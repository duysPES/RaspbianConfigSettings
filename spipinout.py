import colorama
from colorama import Fore, Back, Style

if __name__ == "__main__":
    colorama.init()
    rst = Style.RESET_ALL
    string = \
f"""
{Back.GREEN + Fore.BLUE}SPI PINOUT:{rst}

{Back.WHITE+Fore.BLUE}MOSI{rst}\tBLUE
{Fore.WHITE}MISO{rst}\tWHITE
{Fore.YELLOW}SCLK{rst}\tYELLOW
{Fore.GREEN}CS/RST{rst}\tGREEN
{Fore.RED}VCC{rst}\tRED
{Back.WHITE+Fore.BLACK}GND{rst}\tBLACK
"""
    print(string)

