# Grok-backdoor

Grok-backdoor is a simple python based backdoor, it uses Ngrok tunnel for the communication and it make backdoor binary using Pyinstaller


## Disclaimer: 

All the code provided on this repository is for educational/research purposes only. Any actions and/or activities related to the material contained within this repository is solely your responsibility. The misuse of the code in this repository can result in criminal charges brought against the persons in question. Author will not be held responsible in the event any criminal charges be brought against any individuals misusing the code in this repository to break the law. 
	
	
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

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/Create-backdoor-linux.PNG "Create backdoor binary")

#### Windows : 

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/Create-backdoor-windows1.PNG "Create backdoor binary")

You can find the output binary in grok-backdoor/dist/ directory:

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/output-linux.PNG "Output")


Run grok-backdoor output binary in victim machine and login to Ngrok.com control panel to see the tunnel URL:

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/ngrok.PNG "Ngrok Tunnel")


Telnet to tunnel URL to get the Bind shell: Enjoy shell :)

![alt text](https://github.com/deepzec/Grok-backdoor/blob/master/screenshots/telnet.PNG "Shell")


### Features:
* Multi platform support(windows,linux,Mac)

* Autheticated bind shell

* Ngrok tunnel for communication

Note: I am not a professional python developer, so please excuse my poor coding style :) 

Report bugs to twitter.com/deepzec 

