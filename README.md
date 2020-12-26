# Grok-backdoor

Grok-backdoor is a simple python based backdoor, it uses Ngrok tunnel for the C&C communication. Ngrok-backdoor can generate Windows, Linux and Mac binaries using Pyinstaller.

## How it works:

Ngrok exposes local servers behind NATs and firewalls to the public internet over a secure tunnel.

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/ngrok.jpg "Create backdoor binary")


Ngrok establishes a tunnel between malware local listener port and ngrok server public IP over a unique port number. Attacker can connect Ngrok public IP and unique port to intract with internal malware listener. 




## Disclaimer: 

All the code provided on this repository is for educational/research purposes only. Any actions and/or activities related to the material contained within this repository is solely your responsibility. The misuse of the code in this repository can result in criminal charges brought against the persons in question. Author will not be held responsible in the event any criminal charges be brought against any individuals misusing the code in this repository to break the law. 
	
	
## Dependencies:
Python 2.7

Pyinstaller 3.21

python-pip 9.0.1 


## Installation :
pip install -r requirements.txt


### Usage: 

You need a ngrok.com acccount to use this backdoor, you can provide Ngrok authcode while configuring the grok-backdoor. You will be able to see a new tcp tunnel created in Ngrok status panel after the grok-backdoor server execution on victim machine

Create backdoor binary by running : 

python grok-backdoor.py

#### Linux: 

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/Create-backdoor-linux.PNG "Create backdoor binary")

#### Windows : 

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/Create-backdoor-windows1.PNG "Create backdoor binary")

You can find the output binary in grok-backdoor/dist/ directory:

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/output-linux.PNG "Output")


Run grok-backdoor output binary in victim machine and login to Ngrok.com control panel to see the tunnel URL:

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/ngrok.PNG "Ngrok Tunnel")


Telnet to tunnel URL to get the Bind shell: Enjoy shell :)

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/telnet.PNG "Shell")


### How to embed ngrok binary with the backdoor?

choose No when grok-backdoor ask for "Do you want to download Ngrok binary during execution?". If you choose 'N' it will bind ngrok with the output backdoor binary

### Proxy Blocking ngrok download attempt while backdoor execution?

Choose bind ngrok binary with malware option to bypass proxy blocking.


### Features:
* Multi platform support(windows,linux,Mac) - No cross compiling at the moment, you need to run this code in respective platforms to generate executables for different platforms.
* Autheticated bind shell
* Random output binary
* Ngrok tunnel support to bypass firewall/proxy restrictions.

Report bugs to twitter.com/deepzec & Pull request are always welcome :)

