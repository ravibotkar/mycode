from netmiko import ConnectHandler 
from flask import Flask

app = Flask(__name__)

arista1 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-1', 
    'username': 'admin', 
    'password': 'alta3', 
    } 

arista2 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-2', 
    'username': 'admin', 
    'password': 'alta3', 
    }

@app.route("/aristaswitch/<num>")
def switchcheck(num):

    # using a dictionary to identify which variable we want to use
    switches= {"1": arista1,
               "2": arista2}

    switchdict= switches[num]

    net_connect = ConnectHandler(**switchdict)
    output = net_connect.send_command("show arp")

    return {"show arp": output}


@app.route("/status")
def statuscheck():
    # using a dictionary to identify which variable we want to use
    switches= [arista1, arista2]
    status= {}

    for switch in switches:
        try:
            net_connect = ConnectHandler(**switch)
            x= {switch['host']: 'UP'}
            status.update(x)
        except:
            x= {switch['host']: 'DOWN'}
            status.update(x)

    return status

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

