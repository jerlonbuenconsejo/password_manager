from cryptography.fernet import Fernet

def load_key():
	file = open("key.key", "rb")
	key = file.read()
	file.close()
	return key

key = load_key()
fer = Fernet(key)
"""def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)"""

def view():
	with open('password.txt', 'r') as r: 
		for l in r.readlines():
			data = l.rstrip() #to remove extra new lines when viewing the contents
			user, pw = data.split("|")
			print("User:", user, "| Password:",fer.decrypt(pw.encode()).decode())
def add():
	name = input("Account: ")
	pwd = input("Password: ")

	with open('password.txt', 'a') as f: 
		f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True: 
	action = input("Enter action View/Add: ").lower()
	if action =="q":
		break

	if action == "view":
		view()

	elif action == "add":
		add()