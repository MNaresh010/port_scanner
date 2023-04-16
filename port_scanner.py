import socket 
import sys 
import time 
import threading 
user_input = "YOU NEED TO ENTER:::python3 port_scan.py target start_port end_port" 
 
print("*"*60) 
print("python simple port sacnner") 
print("*"*60) 
 
if(len(sys.argv))!=4: 
    print(user_input) 
    sys.exit() 
 
try: 
    target = socket.gethostbyname(sys.argv[1]) 
except socket.gaierror: 
    print("Name Resolution error") 
    sys.exit() 
start_port = int(sys.argv[2]) 
end_port = int(sys.argv[3]) 
 
print("scanning target:",target) 
def scan_port(port): 
    print("scanning port:",port) 
    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
    server.settimeout(2) 
    conn = server.connect_ex((target,port)) #is there any error occure that port will terminate then continue to another port 
    if conn == 0: 
        print("port {} is OPEN",format(port)) 
    server.close() 
 
for port in range(start_port , end_port+1): 
    thread = threading.Thread (target = scan_port , args = (port,)).start() 
    #thread.start()
