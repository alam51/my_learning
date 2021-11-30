import socket
import time
import traceback

from IPy import IP


# ipaddress = 'https://mail.pgcb.gov.bd/'
# ipaddress = '43.229.13.211'
# ipaddress = '147.91.19.26'
# port = 800


def check_ip(ip):
    try:
        a = IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(_ipaddress, _port, time_out):
    try:
        sock = socket.socket()
        # sock.settimeout(0.5)
        sock.settimeout(time_out)
        sock.connect((_ipaddress, _port))
        print(f'port {_port} is open')
        try:
            banner = sock.recv(1024)
            print(str(banner.decode().strip('\n')))
        except:
            print('Receive unsuccessful')
        sock.close()

    except:
        # print(f'Port {_port} is closed')
        pass


# ipaddress = '147.91.19.26'
# ipaddress = 'facebook.com'
# ipaddress = 'testphp.vulnweb.com'
# ipaddress = '10.16.100.244'
# ipaddress = 'ois.pgcb.gov.bd'

while True:
    try:
        ipaddress = input('Ip /url:  ')
        valid_ipaddress = check_ip(ipaddress)

        print(f'input ip address/ web url = {ipaddress}')
        print(f'valid ip address = {valid_ipaddress}')

        initial_port = int(input('Initial port:  '))
        final_port = int(input('Final port:  '))
        time_out = float(input('Timeout [seconds]:  '))

        for port in range(initial_port, final_port):
            scan_port(valid_ipaddress, port, time_out)

        a = input('Want to run again [y/n]? ')
        if a.lower() == 'n':
            break
        else:
            print('\n')
    except Exception:
        print(traceback.format_exc())
        time.sleep(1)

