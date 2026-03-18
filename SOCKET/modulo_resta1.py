import tkinter as tk

def resta1():
   

    # Tabuleiro 7x7 
    tabuleiro = [
        [None, None, 1, 1, 1, None, None],
        [None, None, 1, 1, 1, None, None],
        [1,    1,    1, 1, 1,    1,    1],
        [1,    1,    1, 0, 1,    1,    1],
        [1,    1,    1, 1, 1,    1,    1],
        [None, None, 1, 1, 1, None, None],
        [None, None, 1, 1, 1, None, None],
    ]

    root = tk.Tk()
    root.title("Resta 1")

    botoes = [[None]*7 for _ in range(7)]
    selecionado = [None]

    def atualizar():
        for i in range(7):
            for j in range(7):
                if tabuleiro[i][j] is None:
                    botoes[i][j]["text"] = ""
                    botoes[i][j]["bg"] = "gray"
                elif tabuleiro[i][j] == 1:
                    botoes[i][j]["text"] = "●"
                    botoes[i][j]["bg"] = "blue"
                else:
                    botoes[i][j]["text"] = ""
                    botoes[i][j]["bg"] = "white"

    def clicar(i, j):
        if tabuleiro[i][j] == 1:
            selecionado[0] = (i, j)
        elif tabuleiro[i][j] == 0 and selecionado[0]:
            si, sj = selecionado[0]
            di, dj = i - si, j - sj

            # movimento válido (2 casas)
            if (abs(di) == 2 and dj == 0) or (abs(dj) == 2 and di == 0):
                mi, mj = si + di//2, sj + dj//2
                if tabuleiro[mi][mj] == 1:
                    tabuleiro[si][sj] = 0
                    tabuleiro[mi][mj] = 0
                    tabuleiro[i][j] = 1
                    selecionado[0] = None
                    atualizar()
                    verificar_fim()

    def verificar_fim():
        if not movimentos_possiveis():
            root.after(1000, root.destroy)

    def movimentos_possiveis():
        for i in range(7):
            for j in range(7):
                if tabuleiro[i][j] == 1:
                    for di, dj in [(2,0),(-2,0),(0,2),(0,-2)]:
                        ni, nj = i+di, j+dj
                        mi, mj = i+di//2, j+dj//2
                        if 0 <= ni < 7 and 0 <= nj < 7:
                            if tabuleiro[ni][nj] == 0 and tabuleiro[mi][mj] == 1:
                                return True
        return False

    for i in range(7):
        for j in range(7):
            btn = tk.Button(root, width=4, height=2,
                            command=lambda i=i, j=j: clicar(i, j))
            btn.grid(row=i, column=j)
            botoes[i][j] = btn

    atualizar()
    root.mainloop()

    # conta pinos restantes
    pinos_sobraram = sum(
        1 for i in range(7) for j in range(7) if tabuleiro[i][j] == 1
    )

    return pinos_sobraram