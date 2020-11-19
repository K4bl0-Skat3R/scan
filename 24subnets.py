#Subnet Scanner by lonov
import socket
ip=input("IP x.x.x > ")
port=int(input("Port > "))

checked=[]
def sock(ip,port):
	s=socket.socket()
	try:
		s.settimeout(0.1)
		s.connect((ip,port))

		res=1
		s.close
	except:
		res=0
		s.close()
	return res

for i in range(1,255):
	thip=ip+"."+str(i)
	print("[INFO] Checking "+thip+"...")
	if sock(thip,port) == 1:
		print("\n[FOUND] "+thip+"\n")
		checked.append(thip)

print("DONE!!! Found:")
for i in checked:
	print(str(i))

input("")
