#!/usr/bin/python3

#by @M4lal0

import subprocess, re, sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def return_ttl_number(address):
    try:
        proc = subprocess.Popen(["ping %s -c 1" % address, ""], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out = out.decode("utf-8").split()
        out[13] = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", out[12])
        return float(out[13][0])
    except Exception:
        pass


def return_ttl_os_name(ttl_numer):
    ttl = ttl_numer
    if ttl:
        if ttl >= 0 and ttl <=64:
            return (bcolors.OKGREEN + 'linux-ttl=%s' % ttl + bcolors.ENDC)
        elif ttl >= 65 and ttl <=128:
            return (bcolors.OKGREEN + 'Windows-ttl=%s' % ttl + bcolors.ENDC)
        elif ttl >= 128 and ttl <=254:
            return (bcolors.OKGREEN + 'Solaris/AIX-ttl=%s' % ttl + bcolors.ENDC)
        else:
            return (bcolors.FAIL + 'unknown=%s' % ttl + bcolors.ENDC)
    else:
        pass


if len(sys.argv) !=2:
    print(bcolors.WARNING + "\n[!]" + bcolors.ENDC + " Uso: " + bcolors.BOLD + sys.argv[0] + " <ip-address>\n" + bcolors.ENDC)
    sys.exit(1)

addr = sys.argv[1]
ttl = return_ttl_number(addr)

print('\n%s -> %s' % (addr,return_ttl_os_name(ttl)))