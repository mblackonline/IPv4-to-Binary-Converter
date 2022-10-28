#!/usr/bin/python3

def ipv4_to_binary(ipv4):
    if len(ipv4.split('.')) != 4:  # checking if the user entered the correct number of octets
        raise IndexError  # raising an error if the user entered the wrong number of octets

    else:
        ipv4_split = ipv4.split('.')  # This creates a comma separated list of the 4 octets saved as strings
        binary = []  # This creates an empty list to store the binary conversions

        # Use a for loop to iterate through the "ipv4_split" list and convert each octet into binary
        for octet in ipv4_split:
            binary.append(''.join(f'{int(octet):08b}'))  # creates a comma separated list of the binary converted numbers

        # For the sake of clarity, I created the below variables to store each converted octet
        octet1 = binary[0]
        octet2 = binary[1]
        octet3 = binary[2]
        octet4 = binary[3]

        return f"\nThe binary equivalent of {ipv4_address} is:\n{octet1}.{octet2}.{octet3}.{octet4}\n"

def binary_to_ipv4(binary):
    if len(binary) != 35 or len(binary.split('.')) != 4:
        raise IndexError
    else:
        ip_addr = binary.split('.')  # This creates a comma separated list of the 4 binary numbers saved as strings

        # For the sake of clarity, I created the below variables to store each converted binary number
        binary1 = ip_addr[0]
        binary2 = ip_addr[1]
        binary3 = ip_addr[2]
        binary4 = ip_addr[3]

        return f'\nThe IPv4 equivalent of {binary} is:\n{int(binary1, 2)}.{int(binary2, 2)}.{int(binary3, 2)}.{int(binary4, 2)}'


if __name__ == '__main__':
    # try/except blocks are used to catch errors
    try:
        user_input = input(
            " - To covert an IPv4 address to a binary: Press 1, or \n - To convert a binary IP address to IPv4: Press 2, or \n "
            "- Type Quit to exit \n")

        if user_input == "quit" or user_input == "Quit" or user_input == "QUIT" or user_input == "q" or user_input == "Q":
            print("Exiting...")
            quit()

        elif user_input == "1":
            ipv4_address = input(
                "\nEnter the IPv4 dotted decimal address (e.g., 192.168.1.1) that you want to convert to binary: \n")
            print(ipv4_to_binary(ipv4_address))

        elif user_input == "2":
            bin_address = input('\nEnter the binary IP address that should be converted to dotted decimal, '
                                'using the format "11111111.11111111.11111111.11111111": \n')
            print(binary_to_ipv4(bin_address))

        else:
            raise ValueError

    except ValueError:
        print("\nYou have entered an invalid input. Please execute the script again.\n")

    except IndexError:
        print("\nYou have entered an invalid input. Please execute the script again.\n")
