import socket
import ssl
def parsed_url(url):
    """
    解析 url 返回 (protocol host port path)
    有的时候有的函数, 它本身就美不起来, 你要做的就是老老实实写
    """
    # 检查协议
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        # '://' 定位 然后取第一个 / 的位置来切片
        u = url

    # 检查默认 path
    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    # 检查端口
    port_dict = {
        'http': 80,
        'https': 443,
    }
    # 默认端口
    port = port_dict[protocol]
    if host.find(':') != -1:
        h = host.split(':')
        host = h[0]
        port = int(h[1])
    return protocol, host, port, path

def get(url):
    protocol, host, port, path = parsed_url(url)
    s = socket_by_protocol(protocol)
    s.connect((host, port))
    request = "GET {} HTTP/1.1\r\nhost: {}\r\nConnection: close\r\n\r\n".format(path, host)
    encoding = "utf-8"
    s.send(request.encode(encoding))
    response = recv_by_socket(s)
    response_str = response.decode(encoding)
    status_code, headers, body = parsed_response(response_str)
    #print(status_code, "\n\n", headers, "\n\n", body)
    print("字符串格式的响应：\n ", response_str)

def parsed_response(r):
    """
    把 response 解析出 状态码 headers body 返回
    状态码是 int
    headers 是 dict
    body 是 str
    """
    header, body = r.split('\r\n\r\n', 1)
    h = header.split('\r\n')
    status_code = h[0].split()[1]   #split 为空表示按空格切片
    status_code = int(status_code)

    headers = {}
    for line in h[1:]:
        k, v = line.split(': ')
        headers[k] = v
    return status_code, headers, body



def recv_by_socket(s):
    buffer_size = 1024
    response = b''
    while True:
        r = s.recv(buffer_size)
        if len(r) == 0:
            break
        else:
            response += r
    return response


def socket_by_protocol(protocol):
    """
    根据协议返回一个 socket 实例
    """
    if protocol == 'http':
        s = socket.socket()
    else:
        # HTTPS 协议需要使用 ssl.wrap_socket 包装一下原始的 socket
        # 除此之外无其他差别
        s = ssl.wrap_socket(socket.socket())
    return s


def test_parse_url():
    url = 'http://localhost:8080/login.html'
    url_info =  parsed_url(url)
    for item in url_info:
        print(item)

def test_get():
    url = "g.cn"
    get(url)

test_get()