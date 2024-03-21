import pyautogui
import socket

# 服务器端
def server():
    host = '0.0.0.0'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print("等待连接...")
    conn, addr = s.accept()
    print("连接来自: ", addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        pyautogui.typewrite(data)
    
    conn.close()

# 客户端
def client(server_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, 12345))

    while True:
        command = input("请输入要发送到服务器的指令: ")
        s.send(command.encode())

if __name__ == "__main__":
    role = input("选择角色（server/client）：")
    
    if role == "server":
        server()
    elif role == "client":
        server_ip = input("请输入服务器IP地址: ")
        client(server_ip)
    else:
        print("无效的角色选择")




