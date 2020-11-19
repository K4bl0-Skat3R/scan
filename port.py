#Port Scanner by lonov
import socket
ip=input("IP x.x.x.x > ")

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

for i in range(1,65535):
	print("[INFO] Checking "+str(i)+"...")
	if sock(ip,i) == 1:
		print("\n[FOUND] "+str(i)+"\n")
		checked.append(i)

print("DONE!!! Found:")
for i in checked:
	print(str(i))
input("")
	
