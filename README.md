# SWE4303 Socket-Programming Demo  
*(Regent College London – Computing Infrastructure Portfolio)*

This repo contains two lightweight Python scripts that demonstrate a raw client–server
echo service in both TCP and UDP modes (Task 2 of the brief).


| `server.py` | Starts an echo server (`python3 server.py tcp` or `udp`) |


| `client.py` | Spawns N parallel clients to hit the server   |



## Start on the VM - backend ecomerce server
*Server  (TCP on port 9000)*
python3 server.py tcp


*Another terminal – 10 clients hit the server:*
python3 client.py 127.0.0.1 tcp 10 "Hello server"
