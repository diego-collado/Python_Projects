import subprocess

target = 200
up = 0
down = 0

while (target < 255):
        ip = "192.168.1." +str(target)
        output = subprocess.Popen(["ping","-c","1",ip],stdout = subprocess.PIPE).communicate()[0]

        if ('Unreachable' in output):
                print('Host ' + ip + " está offline o unavailable")
                down+= 1
        else:
                print("Host " + ip + " está online")
                up+= 1

        target = target+1


print("Un total de " + str(up+down) + " hosts han sido escaneados.")
print(str(up) + " hosts están activos, y " + str(down) + " hosts están offline/inalcanzables. ")
quit()