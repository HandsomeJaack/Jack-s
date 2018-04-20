def input_processing(input_string):
    from Tone import chistka
    print("Doing some process...")
    return chistka(input_string)

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):

    # ввод получаем в байтах, далее декодируем его
    input_bytes = conn.recv(MAX_BUFFER_SIZE)

    # MAX_BUFFER_SIZE определяет максимальный размер сообщения

    import sys
    siz = sys.getsizeof(input_bytes)
    if siz >= MAX_BUFFER_SIZE:
        print("Длина ввода возможно слишком велика {}".format(siz))

    # декодируем ввод и конец строки 
    input_decoded = input_bytes.decode("utf8").strip()

    res = input_processing(input_decoded)
    print("Результат обработки {} : {}".format(input_decoded, res))

    vysl = res.tostring()
    print(vysl) # перекодировка результата
    conn.sendall(vysl)
    conn.close()
    print("Соединение " + ip + ":" + port + " завершено")

def start_server():

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Соединение создано')

    try:
        soc.bind(("127.0.0.1", 12345))
        print('Установка соединения завершена')
    except socket.error as msg:
        import sys
        print('Соединение преравано. Ошибка : ' + str(sys.exc_info()))
        sys.exit()

    soc.listen(10)
    print("Ожидание запроса")

    from threading import Thread

    while True:
        conn, addr = soc.accept()
        ip, port = addr[0], str(addr[1])
        print("Установка соединения от " + str(ip) + ":" + str(port))
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()
       
    soc.close()

start_server()





