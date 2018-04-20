import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
soc.connect(("127.0.0.1", 12345))

clients_input = input("Введите данные для обработки\n")  
soc.send(clients_input.encode("utf8")) # we must encode the string to bytes  
result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
print(result_bytes)
#result_string = result_bytes.decode("utf8")
#print(result_string)
print("Результат полученныый с сервера {}".format(result_bytes.decode("Windows-1250")))  