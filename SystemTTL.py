#!/usr/bin/python3

#by @M4lal0

import subprocess,re,sys


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARKCYAN = '\033[36m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


def get_value_ttl(address):
    proc = subprocess.Popen(["ping -c 1 %s" % address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.split()
    out = out[12].decode('utf-8')

    ttl = re.findall(r"\d{1,3}", out)[0]

    return ttl


if __name__ == '__main__':
    address = sys.argv[1]

    ttl_value = get_value_ttl(address)
    ttl_value = int(ttl_value)

    if ttl_value >= 0 and ttl_value <= 64:
        print(bcolors.GREEN + "\n%s -> Linux " % address + bcolors.ENDC)
    elif ttl_value >= 65 and ttl_value <= 128:
        print(bcolors.GREEN + "\n%s -> Windows " % address + bcolors.ENDC)
    else:
        print(bcolors.GREEN + "\n%s -> Solaris/AIX" %address + bcolors.ENDC)