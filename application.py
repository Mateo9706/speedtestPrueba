#import socket

#import speedtest
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
    convert = client_ip.split(":")
    print(convert)
    print(client_ip)
    response = requests.get(url+convert[0]+endpoint)
    print(response.text)

    """
    source = "0.0.0.0"
    s = speedtest.Speedtest(source_address=source)
    # s = Speedtest()
    # s.get_best_server(s.set_mini_server("https://www.speedtest.net/es"))

    # s.get_servers()

    # s.get_best_server()
    # print(s.get_servers())
    s.download()
    s.upload()
    res = s.results.dict()
    print(res["download"], res["upload"], res["ping"])
    download = round(res["download"] / (10 ** 8), 2)
    upload = round(res["upload"] / (10 ** 8), 2)
    """
    return "yaa" + convert[0]
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


#if __name__ == '__main__':
    #prueba()
#    app.run(host='0.0.0.0')