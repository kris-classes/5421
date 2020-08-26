"""
ISCG5421 - UDP Client

Kris Pritchard - August 2020

This is an instructive code example for teaching socket programming.
Run the server, then the client and type:
    send hello

Type exit to exit.
"""

import socket
import cmd


PORT = 1234


class Client(cmd.Cmd):
    """Simple UDP client for sending messages to UDP server"""

    def do_send(self, line):
        """Runs when the 'send' command is typed into the interpreter."""

        # Print the line typed in
        print(f'line: {line}')
        # Add a newline
        msg = line + '\n'
        # Encode the message as UTF-8
        encoded_msg = msg.encode('utf-8')
        # Convert the encoded message to bytes before sending over the network.
        bytes_msg = bytes(encoded_msg)

        # Create the socket - INET: IPv4 & UDP: DGRAM/DATAGRAM.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Send the bytes
        client_socket.sendto(bytes_msg, ('localhost', PORT))
        # Close the socket
        client_socket.close()

        # TODO: Homework exercise. Add functionality to receive and
        # print replies from the server.

    def do_exit(self, line):
        """Runs when the users types 'exit'. """
        print('Exiting.')
        exit()

    def do_EOF(self, line):
        """Runs when the user pressed Ctrl-D (which sends EOF character)."""
        return True



if __name__ == '__main__':
    client = Client()
    client.cmdloop()
