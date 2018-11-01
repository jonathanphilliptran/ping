import os 
inventory = ['google.com', 'yahoo.com', 'reddit.com']
for item in inventory:
	print(os.system('ping -c 1 ' + item))
