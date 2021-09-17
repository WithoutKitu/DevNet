file = open(".\\devices.txt", "a")

while True:
	device = input("Podaj nazwe urzadzenia: ")
	if device == "exit":
		break
	else:
		file.write(device + "\n")

