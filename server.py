## Umid_Saodatov_RCL_SWF4303
#!/usr/bin/env python3

#importing necessary modules and tools
# socket library for network comm over TCP or UDP
import socket
# threading library to operate client threads concurrently
import threading
# sys library to gain access to terminal-based parameters for configuration
import sys

# Configures which protocol to use, either TCP or UDP, based on a user-defined command-line argument.
# If no argument is given, the system defaults to using TCP.
prot_type = sys.argv[1] if len(sys.argv) > 1 else "tcp"

# Specify the port number the server is to listen on.
ser_port_for_requests = 9000

# Configure the size of the reception buffer for client data (in bytes).
data_size_buffer = 1024


# Manage TCP client connector: collect data, deliver reply, and terminate.
def handle_client(client_connection):
    # Capture data from the customer (e.g., a request about a product in e-commerce).
    cl_request = client_connection.recv(data_size_buffer)
    client_connection.sendall(b"OK: " + cl_request)  # echo back
    client_connection.close()                        # terminate


if prot_type == "tcp":
    # Create a TCP server socket.
    ser_sock = socket.socket()
    # Bind the socket to all interfaces at the given port.
    ser_sock.bind(("", ser_port_for_requests))
    ser_sock.listen()                               # awaiting client connections
    print("TCP Server on port", ser_port_for_requests)  # startup confirmation
    while True:
        # Accepting a client connection involves obtaining the client socket and address.
        client_socket, client_addr = ser_sock.accept()
        # Initiate a thread for client management (daemon = auto-cleanup).
        threading.Thread(target=handle_client,
                         args=(client_socket,),
                         daemon=True).start()

else:
    # Make a UDP server socket.
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ser_sock.bind(("", ser_port_for_requests))
    print("UDP Server on port", ser_port_for_requests)   # startup confirmation
    while True:
        # Gather information and the customer's address.
        received_data, cl_addr = ser_sock.recvfrom(data_size_buffer)
        ser_sock.sendto(b"OK: " + received_data, cl_addr)   # echo back
