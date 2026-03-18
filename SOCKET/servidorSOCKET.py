import socket
import modulo_numpuz
import modulo_resta1


hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 8095

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print(f"Servidor iniciado em {HOST}:{PORT}")
conn, addr = s.accept()
print(f"Conectado por {addr}")
print('-'*30)
print('1 - Numpuz / 2 - Resta um')
print('-'*30)
while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    print(f"Cliente: {data}")

    if data == "1":
        saida = modulo_numpuz.numpuz()
        resultado = f"RESULTADO: tempo do servidor = {saida}"
        conn.send(resultado.encode())

        data = conn.recv(1024).decode()
        print(f"Cliente: {data}")
        continue

    elif data == "2":
        saida = modulo_resta1.resta1()
        resultado = f"RESULTADO SERVIDOR: restaram {saida} pontos no tabuleiro"
        conn.send(resultado.encode())

        data = conn.recv(1024).decode()
        print(f"Cliente: {data}")
        continue

    msg = input("Servidor: ")
    conn.send(msg.encode())

    if msg == "1":
        saida = modulo_numpuz.numpuz()
        resultado = f"RESULTADO SERVIDOR: {round(saida)} segundos"
        conn.send(resultado.encode())

        data = conn.recv(1024).decode()
        print(f"Cliente: {data}")

    elif msg == "2":
        saida = modulo_resta1.resta1()
        resultado = f"RESULTADO SERVIDOR: restaram {saida} pontos no tabuleiro"
        conn.send(resultado.encode())

        data = conn.recv(1024).decode()
        print(f"Cliente: {data}")

conn.close()