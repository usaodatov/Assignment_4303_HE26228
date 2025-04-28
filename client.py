## Umid_Saodatov_RCL_SWF4303
#!/usr/bin/env python3

#importing necessary modules and tools
import socket # socket library for network comm over TCP or UDP
import threading # threading library to operate client threads concurrently
import sys # sys library to gain access to terminal-based parameters for configuration
import time # time library to insert pauses before initiation of each thread

# First command-line argument to determine the host address of the server
serv_host_bend = sys.argv[1]

# Second command-line argument, determine communication protocol TCP or UDP, default to TCP.
protocol_type = sys.argv[2] if len(sys.argv) > 2 else "tcp"

# Third command-line argument, instruct number client threads to create, default = 1.
client_num = int(sys.argv[3]) if len(sys.argv) > 3 else 1

# Fourth command-line argument; if not specified, default = "Knock-Knock server"
outgoing_query = sys.argv[4] if len(sys.argv) > 4 else "Knock-Knock server"

# Set port number (9000) where the server listens for incoming connections
listening_port = 9000

# Set receive response buffer size from server =  1,024 bytes
responce_packet_size = 1024

# Func. Executes client instance using an index to identify each thread
def run_client(client_index: int):
    # if TCP, then manage the operations that are specific to TCP
    if protocol_type == "tcp":

        sock = socket.socket()

        sock.connect((serv_host_bend, listening_port))  # host and port, connect this socket to server

        sock.sendall(outgoing_query.encode()) #Encode + send the server the outgoing message.

        reply = sock.recv(responce_packet_size).decode() # Accept the server's reply/convert to a string format

        print(f"[{client_index}] TCP Response: ", reply) # Print the TCP response + index of the thread

        sock.close() #finish the connection/ close the TCP socket

    # If protocol in use not TCP, use UDP for communicating
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP socket to send datagrams to the server

        sock.sendto(outgoing_query.encode(), (serv_host_bend, listening_port))  #send the server the outgoing message

        reply, _ = sock.recvfrom(responce_packet_size) #server's response

        print(f"[{client_index}] UDP Response: ", reply.decode()) # Output UDP response + thread index

        sock.close() # close the UDP socket / release resource

# Create list to hold thread objects for client instances.
threads = []  #must be empty @start

#Iterate through clients in order - establish the threads
for i in range(client_num):

    #For every client: a thread that calls the run_client func. with thread index (i+1)
    thr_t = threading.Thread(target=run_client, args=(i + 1,))

    thr_t.start()      # Initialize threads perform client func.

    threads.append(thr_t)     # record every thread in the list to subsequent handling

    time.sleep(0.05) # prevent the server from excessive number of simultaneous conn. short delay = 50ms.

# threads to complete their tasks before the program can terminate
for thr_t in threads:
    #each thread to complete execution - by joining it
    thr_t.join()