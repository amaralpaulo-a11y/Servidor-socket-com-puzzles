import tkinter as tk
import random
import time

def numpuz():

    tempo_demorado = 0
    inicio = time.time()

    root = tk.Tk()
    root.title("Numpuz 3x3")

    # estado inicial embaralhado
    numeros = list(range(1, 9)) + [0]  # 0 = espaço vazio

    def embaralhar():
        while True:
            random.shuffle(numeros)
            if solucionavel(numeros):
                break

    def solucionavel(seq):
        inv = 0
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                if seq[i] and seq[j] and seq[i] > seq[j]:
                    inv += 1
        return inv % 2 == 0

    embaralhar()

    botoes = []

    def atualizar():
        for i in range(9):
            valor = numeros[i]
            if valor == 0:
                botoes[i]["text"] = ""
                botoes[i]["bg"] = "black"
            else:
                botoes[i]["text"] = str(valor)
                botoes[i]["bg"] = "lightgray"

    def encontrar_vazio():
        return numeros.index(0)

    def mover(i):
        vazio = encontrar_vazio()
        if (i % 3 == vazio % 3 and abs(i - vazio) == 3) or \
           (i // 3 == vazio // 3 and abs(i - vazio) == 1):
            numeros[vazio], numeros[i] = numeros[i], numeros[vazio]
            atualizar()
            verificar_vitoria()

    def verificar_vitoria():
        nonlocal tempo_demorado
        if numeros == [1,2,3,4,5,6,7,8,0]:
            tempo_demorado = time.time() - inicio
            label["text"] = f"Resolvido em {tempo_demorado:.2f} s"
            root.after(2000, root.destroy)

    # interface
    frame = tk.Frame(root)
    frame.pack()

    for i in range(9):
        btn = tk.Button(frame, text="", width=6, height=3,
                        command=lambda i=i: mover(i))
        btn.grid(row=i//3, column=i%3)
        botoes.append(btn)

    label = tk.Label(root, text="Resolva o puzzle!")
    label.pack()

    atualizar()
    root.mainloop()

    return tempo_demorado




