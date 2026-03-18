import socket
import modulo_numpuz
import modulo_resta1

HOST = 'Endereço ip da rede'
PORT = 8095

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Conectado ao servidor!")
print('-'*30)
print('1 - Numpuz / 2 - Resta um')
print('-'*30)
while True:
    msg = input("Cliente: ")
    s.send(msg.encode())

    if msg == "1":
        saida = modulo_numpuz.numpuz()

        data = s.recv(1024).decode()
        print(f"Servidor: {data}")

        resultado = f"RESULTADO CLIENTE: {round(saida)} segundos"
        s.send(resultado.encode())
        continue

    elif msg == "2":
        saida = modulo_resta1.resta1()

        data = s.recv(1024).decode()
        print(f"Servidor: {data}")

        resultado = f"RESULTADO CLIENTE:restaram {saida} pontos no tabuleiro"
        s.send(resultado.encode())
        continue

    data = s.recv(1024).decode()
    print(f"Servidor: {data}")

    if data == "1":
        saida = modulo_numpuz.numpuz()

        resultado = f"RESULTADO CLIENTE:{round(saida)} segundos"
        s.send(resultado.encode())

        data = s.recv(1024).decode()
        print(f"Servidor: {data}")

    elif data == "2":
        saida = modulo_resta1.resta1()

        resultado = f"RESULTADO CLIENTE:restaram {saida} pontos no tabuleiro"
        s.send(resultado.encode())

        data = s.recv(1024).decode()
        print(f"Servidor: {data}")

s.close()
