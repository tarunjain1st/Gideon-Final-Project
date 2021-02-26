import cv2,socket,pickle,struct
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_address = ('192.168.137.99',9999)
server_socket.bind(socket_address)
server_socket.listen(5)

def streamVideo():
    while True:
        client_socket,addr = server_socket.accept()
        try:
            if client_socket:
                vid = cv2.VideoCapture(0)
                while(vid.isOpened()):
                    img,frame = vid.read()
                    frame = cv2.resize(frame,(320,240))
                    a = pickle.dumps(frame)
                    message = struct.pack("Q",len(a))+a
                    client_socket.sendall(message)
        except:
            pass
