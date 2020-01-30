import random
import ssl
import xml.etree.ElementTree as ET
from httplib2 import Http, ProxyInfo, socks
import urllib3


def without_proxy(inp_url):
    http = Http()
    response, content = http.request(
        uri=inp_url, method="GET")
    return ET.fromstring(content)


def get_proxies():
    with open("proxylist.txt", "r") as f:
        return f.readlines()


def select_proxy():
    return proxy_list[random.randint(1, len(proxy_list))].replace("\n", "")


def remove_proxy(proxy):
    proxy_list.remove(proxy + "\n")
    with open("proxylist.txt", "w") as f:
        f.writelines(proxy_list)


def with_proxy(inp_url):
    while True:
        try:
            proxy = select_proxy()
            # proxy = "54.161.89.147:8888"
            print(proxy)
            proxy_info = ProxyInfo(proxy_type=socks.PROXY_TYPE_HTTP, proxy_host=proxy.split(":")[0],
                                   proxy_port=int(proxy.split(":")[1]))
            http = Http(proxy_info=proxy_info)
            response, content = http.request(
                uri=inp_url, method="GET")
            print(content)
            return ET.fromstring(content)
        except (socks.Socks5Error, TimeoutError, ssl.SSLCertVerificationError,socks.GeneralProxyError) as e:
            print(e)
            remove_proxy(proxy)
            print("Removed ",proxy)
            continue
        except ET.ParseError as e:
            print(e)
            remove_proxy(proxy)
            print("Removed ",proxy)
            continue

def verify_phishing_url(root):
    if root[1][0].tag == "errortext":
        print(root[1][0].text)
    else:
        if root[1][0][1].text == "true":
            if root[1][0][4].text == "true":
                if root[1][0][6].text == "true":
                    print("URL is Phishing URL")
                else:
                    print("URL is Not Phishing URL")
            else:
                print("URL is not varified by PhishTank community")
        else:
            print("URL is not in PhishTank Database")


proxy_list = get_proxies()
url = input("Enter URL: ")
url = urllib3.util.parse_url(f"http://checkurl.phishtank.com/checkurl/index.php?url={url}").url
try:
    choice = int(input("1. With Proxy\n2. Without Proxy\nEnter Your choice: "))
    if choice == 1:
        root = with_proxy(url)
    elif choice == 2:
        root = without_proxy(url)
    else:
        print("Enter Valid Choice")
        raise ValueError
    print("URL= ", url)
    verify_phishing_url(root)
except ValueError:
    print("Enter Valid Number")
