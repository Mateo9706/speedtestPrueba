#import socket

import socket

from pprint import pprint
#import speedtest
import speedtest

from flask import Flask, request, render_template
import requests
#from speedtest import Speedtest

app = Flask(__name__)


url = "https://ipinfo.io/"
url2 = "https://librespeed.org/"

@app.route('/ip')
def hello_world():


    print("entra aca")
    endpoint = "/json"

    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    #convert = client_ip.split(":")
    #print(convert)
    print(client_ip)
    ifd = get_ip()
    result = gt(ifd)

    print(ifd)
    #response = requests.get(url+client_ip+endpoint)
    #print(response.text)



    return ifd
    #otro()

    #c=prueba()
    #return "prueba" + c
"""
def prueba():
    print("entraaa")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8000))
    s.listen(1)
    # Estas son las variables del cliente
    conn, addr = s.accept()
    clientIP = addr  # Aquí se guarda la IP del cliente
    print(clientIP)
    s.close()
    return 
"""

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
        print(s.getsockname())
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def gt(ipclient):
    threads = 2
    server = [11694]
    source = ipclient
    s = speedtest.Speedtest(source_address=source)
    s.get_servers(server)
    # s = Speedtest()
    # s.get_best_server(s.set_mini_server("https://www.speedtest.net/es"))

    # s.get_servers()

    # s.get_best_server()
    # print(s.get_servers())
    s.download(threads=threads)
    s.upload(threads=threads)
    res = s.results.dict()
    s.results.share()
    results_dict = s.results.dict()
    pprint(results_dict)

    download = round(res["download"] / (10 ** 6), 2)
    upload = round(res["upload"] / (10 ** 6), 2)
    print(download, upload, res["ping"])


    return results_dict



if __name__ == '__main__':
    #hello_world()
    #gt()
    #prueba()
    app.run(host='0.0.0.0')