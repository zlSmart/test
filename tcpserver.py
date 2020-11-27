import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server.bind(("",7880))
tcp_server.listen(128)
new_socket,client_addr = tcp_server.accept()
print(client_addr)

recv_data = new_socket.recv(1024)
print(recv_data)
new_socket.send(b"byebye")
new_socket.close()
tcp_server.close()
