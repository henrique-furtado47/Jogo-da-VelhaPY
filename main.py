import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        
        self.reiniciar_jogo()
        
    def reiniciar_jogo(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.atual = "X"
        
        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2,
                                  command=lambda i=i, j=j: self.jogar(i, j))
                botao.grid(row=i, column=j)
                linha.append(botao)
            self.botoes.append(linha)

    def jogar(self, i, j):
        index = 3 * i + j
        if self.tabuleiro[index] == " ":
            self.tabuleiro[index] = self.atual
            self.botoes[i][j].config(text=self.atual)
            
            if self.checar_vitoria(self.atual):
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.atual} ganhou!")
                self.reiniciar_jogo()
            elif " " not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.atual = "O" if self.atual == "X" else "X"

    def checar_vitoria(self, jogador):
        vitoria = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
            (0, 4, 8), (2, 4, 6)              # diagonais
        )
        return any(all(self.tabuleiro[i] == jogador for i in linha) for linha in vitoria)

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
