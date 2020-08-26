"""
ISCG5421 - UDP Server

Kris Pritchard - August 2020

Run the server, then the client and send messages to it.
See client docs for details.

Send an 'exit' message from the client to exit.
"""

import socket
import sys
import time


# Program entry point
if __name__ == '__main__':

    # Extract optional port number from arguments.
    # Useful if program crashed and the port is still in use.
    print(f'Program arguments: {sys.argv}')

    # Set the default port
    port = 1234
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass  # Do nothing and use default port if the conversion to int failed.

    # Setup the server
    # Create the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket on localhost & port
    server_socket.bind( ('localhost', port) )
    # Listen for connections
    server_socket.listen()

    print(f'TCP Server listening on localhost:{port}')
    # Loop forever
    while True:
        # 'Accept' data and extract the client and address.
        client, addr = server_socket.accept()

        # Print both of them
        print(f'Client: {client} --- Addr: {addr}')

        # Get the message from the client
        bytes_msg = client.recv(1024)  # Buffer size = 1024 bytes
        # Convert the message from bytes
        decoded_message = bytes_msg.decode('utf-8')
        # Strip newline character
        msg = decoded_message.strip()

        # If the message
        if msg == 'exit':  # Not a good idea to let clients tell your server to exit
            # Print that we're exiting
            print('Exiting!')
            # Tell the client that we're exiting
            client.send(b'exiting!\n')
            # Close the client socket
            client.close()
            # Close the server socket
            server_socket.close()
            # Exit
            sys.exit()
        else:
            # Display the message received
            print(f'Message received: {msg}. Replying')
            # Send a reply
            client.send(b'pong!\n')

            # TODO: Homework exercise:
            # Merge the UDP client and server into a single program.
            # Then add the following:
            # - Create a local server socket with a random port
            # - Display the port chosen
            # - Allow the client to connect to another port
            # - Display any messages sent from the other server to your port.

        # Sleep for 2 seconds and do it again.
        print('Waiting')
        time.sleep(2)



