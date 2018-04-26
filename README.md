# Grok-backdoor

Grok-backdoor is a simple python based backdoor, it uses Ngrok tunnel for the communication and it make backdoor binary using Pyinstaller


Disclaimer: This program is for educational purposes only.
	I am not responsible for how you use this program
	
	
## Dependencies:
Python 2.7

Pyinstaller 3.21

python-pip 9.0.1 


## Installation :
pip install -r requirements.txt


### Usage: 

You need to register an acccount in ngrok.com to use this backdoor, provide Ngrok authcode while configuring the grok-backdoor. You will see a new tcp tunnel created in Ngrok status panel after the grok-backdoor server execution in victim machine

Create backdoor binary binary running : 

python grok-backdoor.py

#### Linux: 

![alt text](https://github.com/deepzec/grok-backdoor/blob/new/screenshots/Create-backdoor-linux.PNG "Create backdoor binary")

#### Windows : 

![alt text](https://github.com/deepzec/grok-backdoor/blob/new/screenshots/Create-backdoor-windows1.PNG "Create backdoor binary")

You can find the output binary in grok-backdoor/dist/ directory:

![alt text](https://github.com/deepzec/grok-backdoor/blob/new/screenshots/output-linux.PNG "Output")


Run grok-backdoor output binary in victim machine and login to Ngrok.com control panel to see the tunnel URL:

![alt text](https://github.com/deepzec/grok-backdoor/blob/new/screenshots/ngrok.PNG "Ngrok Tunnel")


Telnet to tunnel URL to get the Bind shell: Enjoy shell :)

![alt text](https://github.com/deepzec/grok-backdoor/blob/new/screenshots/telnet.PNG? "Shell")


### Features:
* Multi platform support(windows,linux,Mac)

* Autheticated bind shell

* Ngrok tunnel for communication

