#import socket
#from flask_socketio import SocketIO
from flask import Flask, request, render_template
import requests

#async_mode = None
app = Flask(__name__)
#socket_ = SocketIO(app, async_mode=async_mode)

url = "https://ipinfo.io/"
url2 = "https://librespeed.org/"

@app.route('/ip')
def hello_world():
    endpoint = "/json"
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    print(client_ip)
    #response = requests.get(url+client_ip+endpoint)
    #print(response.text)
    #otro()
    return "ya"+" "+client_ip

#def otro():
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.bind(('0.0.0.0', 5500))
    #s.listen(1)
    # Estas son las variables del cliente
    #conn, addr = s.accept()
    #clientIP = addr  # Aquí se guarda la IP del cliente
    #s.close()

if __name__ == '__main__':
    #socket_.run(app)
    app.run(host='0.0.0.0')