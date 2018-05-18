import socket

def get_baidu():
    url = 'www.baidu.com'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url, 80))
    s.send(b'GET / HTTP/1.0\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    response = get_response_str(s)
    print(response)

def get_response_str(s):
    buffer = []
    len = 1024
    while True:
        d = s.recv(len)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    return data.decode('utf-8')

get_baidu()