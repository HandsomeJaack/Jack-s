def send_to_server(clients_input):
	import socket

	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	soc.connect(("127.0.0.1", 12345))

	#сlients_input = input("Введите данные для обработки\n")  
	soc.send(clients_input.encode("utf8"))
	result_bytes = soc.recv(4096) 
	print(result_bytes)
	result_string = result_bytes.decode("utf8")
	print("Результат полученныый с сервера {}".format(result_string)) 
	return result_string; 

#send_to_server(input("Введите данные для обработки\n"))