from flask import Flask, request, jsonify
import socket
import subprocess
import sys
app = Flask(__name__)



@app.route('/', methods=['GET'])
def getIP():
    ip = socket.gethostbyname(socket.gethostname())
    return ip
@app.route('/', methods=["POST"])
def stress():
    t = [sys.executable, "stress_cpu.py"]
    #print("here")
    p = subprocess.Popen(t, stdout =subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    '''
     stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)
    print("here")
    '''
   
    return 200
    

if __name__ == '__main__':
    app.run(debug=True)
