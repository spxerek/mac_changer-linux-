# mac_changer-linux-

This Python script is designed to change the MAC address of a network interface on a Linux system. The MAC address is a unique identifier assigned to network devices.

The script accepts two command-line arguments:
- `-i` or `--interface`: Specifies the network interface for which the MAC address should be changed.
- `-m` or `--new_mac`: Specifies the new MAC address that will replace the current MAC address.

Here's how the script works:

1. It imports the necessary modules and libraries.
2. The `get_arguments()` function parses the command-line arguments provided by the user. It ensures that both the interface and new MAC address are specified. If any of them is missing, an error message is displayed.
3. The `change_mac()` function is responsible for changing the MAC address. It takes the interface and new MAC address as arguments and uses the `subprocess` module to execute the necessary commands (`ifconfig`) to bring down the interface, set the new MAC address, and bring the interface back up.
4. The `get_current_mac()` function retrieves the current MAC address of the specified interface. It uses the `subprocess` module to execute the `ifconfig` command and searches for a MAC address pattern in the output.
5. The `options` variable stores the command-line arguments provided by the user.
6. The current MAC address is obtained using the `get_current_mac()` function and displayed.
7. The `change_mac()` function is called to change the MAC address to the new MAC address provided by the user.
8. The current MAC address is obtained again using `get_current_mac()`.
9. If the current MAC address matches the new MAC address provided by the user, a success message is displayed. Otherwise, an error message is displayed.

This script can be useful for various purposes such as network troubleshooting, privacy protection, or network security testing. It provides a straightforward way to change the MAC address of a network interface using Python on a Linux system.
