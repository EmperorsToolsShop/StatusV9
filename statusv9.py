import requests
import urllib3
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor
import platform
import subprocess
import os
from urllib.parse import urlparse
import ctypes
import random
from art import text2art
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    os.mkdir("Results")
except:
    pass


def clear():
    if platform.system() == "Windows":
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


def ansci_banner3():
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + text2art("EmperorsToolsShop", "random")]
    return ''.join(colored_chars) + Style.RESET_ALL


geel = Fore.YELLOW
blauw = Fore.BLUE
groen = Fore.GREEN
reset = Style.RESET_ALL
cyan = Fore.CYAN
rood = Fore.RED


class StatusChecker:
    def __init__(self):
        self.amount = len(lijst)
        self.current = 0
        self.goods = 0
        self.maybes = 0
        self.errors = 0

    def ERROR(self, star, domain):
        try:
            self.errors += 1
            print(f'\r[{reset}{cyan}*{reset}] {rood}Target: {geel}{domain}{reset}')
            self.schijven_(star=star, types="ERRORS")
            self.keep_tracks()
            return True
        except:
            return False

    def MAYBES(self, star, domain, status_code):
        try:
            star = self.get_redirect_url(url=star)
            self.maybes += 1
            print(f'\r[{reset}{cyan}*{reset}] {groen}Target: {blauw}{domain}{reset} {geel}STATUS CODE: {groen}{status_code}{reset}')
            self.schijven_(star=star, types="BAD_STATUS")
            self.keep_tracks()
            return True
        except:
            return False

    def GOODIES(self, star, domain, status_code):
        try:
            self.goods += 1
            print(f'\r[{reset}{cyan}*{reset}] {groen}Target: {blauw}{domain}{reset} {geel}STATUS CODE: {groen}{status_code}{reset}')
            self.schijven_(star=star, types="GOOD_STATUS")
            self.keep_tracks()
            return True
        except:
            return False

    def keep_tracks(self):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(
                ' EmperorsToolsShop StatusV3 | good_ips: {} | maybe_good_ips: {} | exceptions: {} | total: {}/{}'.format(
                    self.goods,
                    self.maybes,
                    self.errors,
                    self.current,
                    self.amount
                ))
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_redirect_url(url):
        try:
            scheme, netlock, path, _, _, _ = urlparse(url)
            domain = scheme + "://" + netlock
            return domain
        except:
            return False

    @staticmethod
    def get_domain(url):
        if "://" in url:
            url = url.split("://")[1]
        if ":" in url:
            url = url.split(":")[0]
        return url

    @staticmethod
    def get_default(url):
        if "://" not in url:
            url = "http://" + url
        return url

    @staticmethod
    def schijven_(star, types='GOOD_STATUS'):
        schrijven = open(f"Results/{types}_IPS.txt", "a", errors='ignore')
        schrijven.write(star + "\n")
        schrijven.close()

    @staticmethod
    def send_data(star, allow_redirects=False):
        try:
            with requests.get(star, allow_redirects=allow_redirects, verify=False, timeout=time_out) as check_if_up:
                check_if_up.close()
                return check_if_up.status_code
        except requests.RequestException:
            return False

    def is_up(self, star, allow_redirects=False):
        star = star.strip().replace("\n", "").replace("\r", "").replace(" ", "").strip()
        self.current += 1
        self.keep_tracks()
        if check_custom_port == "y" or check_custom_port == "yes":
            domain = self.get_domain(url=star)
            star = f"{schems}://{domain}:{port}"
        else:
            domain = self.get_domain(url=star)
            star = self.get_default(url=star)
        try:
            status_code = self.send_data(star=star, allow_redirects=allow_redirects)
            if status_code is False:
                return self.ERROR(star=star, domain=domain)
            if status_code == 200:
                return self.GOODIES(star=star, domain=domain, status_code=status_code)
            elif status_code == 301 or status_code == 302 or status_code == 304 or status_code == 307:
                status_code2 = self.send_data(star=star, allow_redirects=allow_redirects)
                if status_code2 is False:
                    return self.ERROR(star=star, domain=domain)
                elif status_code2 == 200:
                    return self.GOODIES(star=star, domain=domain, status_code=status_code2)
                else:
                    return self.MAYBES(star=star, domain=domain, status_code=status_code2)
            else:
                return self.MAYBES(star=star, domain=domain, status_code=status_code)
        except Exception as e:
            print(e)
            return self.ERROR(star=star, domain=domain)


if __name__ == '__main__':
    clear()
    print(ansci_banner3())
    print(f"{geel}EMPERORSTOOLSSHOP LEGACY{reset}\n{groen}https://t.me/officialEmeporsToolsShop{reset}\n{geel}"
          f"@EmperorsToolsOfficial{reset}\n{blauw}FAST MASS PORT SCANNER V9{reset}")
    try:
        lijst = open(input(f"{groen}Your list Domain Please{reset} ?: "), errors='ignore').readlines()
        check_custom_port = input(f"{geel}Are We checking A custom Port{reset}? {groen}(yes or no):{reset} ")
        if check_custom_port == "y" or check_custom_port == "yes":
            port = input(f"{geel}What port are you looking at today{reset}? {groen}:{reset} ")
            schems = input(f"{geel}is This HTTP or HTTPS{reset}? {groen}:{reset} ")
        time_out = int(input(f"{groen}How Seconds Timeout You wish to use{reset} ? {geel}:{reset} "))
        maximume_threads = int(input(f"{groen}How Many Threads You wish to use{reset} ? {geel}:{reset} "))
        clear()
        ansci_banner3()
        tools = StatusChecker()
        with ThreadPoolExecutor(max_workers=maximume_threads) as pool:
            pool.map(tools.is_up, lijst)
    except KeyboardInterrupt:
        print(f"{rood} WTF ARE YOU DOING BROTHER")
        exit()
    except Exception as e:
        print(f"{rood} STOP PLAYING BRO!! FILE NOT FOUND")
        exit()
