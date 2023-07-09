#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--i", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--m", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-]Please specify a MAC addr, use --help for more info ")
    else:
        return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_result is not None:
        return mac_result.group(0)
    else:
        print("[-] Couldn't read the MAC address")


options = get_arguments()

current_mac = get_current_mac(options.interface)
if current_mac is not None:
    print("Current MAC = "+str(current_mac))

    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] MAC address was successfully changed to " + current_mac)
    else:
        print("[-] MAC did not get changed")
else:
    print("[-] "+options.interface+" does not have a MAC Address")
