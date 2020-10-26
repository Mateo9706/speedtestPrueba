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
    print("entra hello")

    print("entra aca")
    endpoint = "/json"

    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    #convert = client_ip.split(":")
    #print(convert)
    print(client_ip)
    #ifd = get_ip()
    result = gt()

    #print(ifd)
    #response = requests.get(url+client_ip+endpoint)
    #print(response.text)

    return result

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("entra socket")
    try:
        # doesn't even have to be reachable
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
        print(s.getsockname())
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def gt():
    threads = 2
    server = [11694]
    #source = ipclient
    s = speedtest.Speedtest()
    #s.get_servers(server)

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

    app.run(host='0.0.0.0')