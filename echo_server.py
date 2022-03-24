import remote_pb2
import socket


if __name__ == "__main__":
    host = ''
    port = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    print(host, port)

    s.listen(1)
    conn, addr = s.accept()

    while True:
        try:
            data = conn.recv(4096)

            d = remote_pb2.RemoteData()
            d.ParseFromString(data)

            print("Received Data")
            print(d)

            d.gripAngle *= 2
            d.x *= 3.14

            conn.sendall(d.SerializeToString())

        except socket.error as e:
            print(e)
            break

    conn.close