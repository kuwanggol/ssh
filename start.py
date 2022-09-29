import os,requests,sys

headers={'User-Agent':''}
r = ["2B34TJO1AbZo9TPomFGTjCnyOGV_22cjck77n7VmQND3dv2JY"]
try:
 os.remove("ngrok")
except:
 pass
os.system('wget -O ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip > /dev/null 2>&1')
os.system('unzip ngrok.zip')
for token in r:
 try:
  os.system('./ngrok authtoken {}'.format(token))
  os.system('./ngrok tcp --region us 22 &>/dev/null &')
  os.system('sudo apt update > /dev/null 2>&1')
  os.system('sudo apt install openssh-server > /dev/null 2>&1')
  os.system('mkdir -p /var/run/sshd')
  os.system("echo root:phmikey123 | chpasswd")
  os.system('echo "PermitRootLogin yes" >> /etc/ssh/sshd_config')
  os.system('echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config')
  os.system('echo "LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc')
  os.system('echo "export LD_LIBRARY_PATH" >> /root/.bashrc')
  os.system('sudo service ssh start')
  r = requests.get("http://localhost:4040/api/tunnels")
  port = r.text.split(":")[6].replace('","proto"',"")
  hostname = r.text.split(":")[5].replace("//","")
  datassh = (f"{hostname}:{port}")
  print(datassh)
  sys.stdout.flush()
  break
 except:
  print("Error! may be it's in used")
