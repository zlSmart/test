import socket

tcp_client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(("127.0.0.1",7880))
tcp_client.send(b"hello")
recv_data = tcp_client.recv(1024)
print(recv_data)
tcp_client.close()