import socket

web = socket.socket()
web.connect(('google.com', 80))

msg = """GET / HTTP/1.1
Host: www.google.com

"""

web.send(msg.encode())
response = web.recv(1024).decode()

print(response)
