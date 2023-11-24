import requests
import socket

def rd():
    proxies = []
    with open('proxies.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                proxies.append(line)
    return proxies

def check(proxy):
    ip, port = proxy.split(':')
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    try:
        response = requests.get('https://ipv4.games/claim?name=SimpleProxyChecker', proxies=proxies, timeout=10)
        if response.status_code == 200:
            return True
    except Exception as e:
        pass
    return False

def check2():
    proxies = rd()
    good_proxies = []
    for proxy in proxies:
        if check(proxy):
            good_proxies.append(proxy)
            print(f'{proxy} is good.')
    return good_proxies

def save(good_proxies):
    with open('good.txt', 'w') as file:
        for proxy in good_proxies:
            file.write(f'{proxy}\n')

def main():
    good_proxies = check2()
    save(good_proxies)

if __name__ == '__main__':
    main()
