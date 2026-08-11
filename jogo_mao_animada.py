import random
import tkinter as tk
from tkinter import font

# AP2 - Pedra, Papel e Tesoura COM MÃO ANIMADA EM PYTHON
# Algoritmo e Lógica de Programação II

class Jogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Pedra, Papel e Tesoura - AP2")
        self.root.geometry("500x600")
        self.root.configure(bg="#1a1a2e")

        self.vitorias_usuario = 0
        self.vitorias_pc = 0
        self.empates = 0
        self.opcoes = ["pedra", "papel", "tesoura"]
        
        # Emojis das mãos - igual humano
        self.mao_emoji = {
            "pedra": "✊\n\nMÃO FECHADA\nPEDRA",
            "papel": "🖐️\n\nMÃO ABERTA\nPAPEL", 
            "tesoura": "✌️\n\n2 DEDOS\nTESOURA"
        }
        self.mao_simples = {"pedra": "✊", "papel": "🖐️", "tesoura": "✌️"}

        # TÍTULO
        tk.Label(root, text="PEDRA, PAPEL E TESOURA", font=("Arial", 18, "bold"), 
                 bg="#1a1a2e", fg="white").pack(pady=15)

        # PLACAR
        self.placar_label = tk.Label(root, text="Você: 0 | Empates: 0 | PC: 0", 
                                     font=("Arial", 14), bg="#16213e", fg="white", padx=20, pady=10)
        self.placar_label.pack(pady=10)

        # ÁREA DA MÃO DO PC
        self.frame_pc = tk.Frame(root, bg="#0f3460", width=300, height=250)
        self.frame_pc.pack(pady=20)
        self.frame_pc.pack_propagate(False)
        
        tk.Label(self.frame_pc, text="COMPUTADOR", font=("Arial", 10), 
                 bg="#0f3460", fg="#e94560").pack()
        
        self.mao_pc_label = tk.Label(self.frame_pc, text="🤜\n\nESPERANDO...", 
                                     font=("Arial", 40), bg="#0f3460", fg="white", justify="center")
        self.mao_pc_label.pack(expand=True)

        # RESULTADO
        self.resultado_label = tk.Label(root, text="Escolha sua jogada!", 
                                        font=("Arial", 16, "bold"), bg="#1a1a2e", fg="#f5f5f5")
        self.resultado_label.pack(pady=10)

        # SUA JOGADA
        self.sua_jogada_label = tk.Label(root, text="", font=("Arial", 12), 
                                         bg="#1a1a2e", fg="white")
        self.sua_jogada_label.pack()

        # BOTÕES
        frame_botoes = tk.Frame(root, bg="#1a1a2e")
        frame_botoes.pack(pady=20)

        btn_style = {"font": ("Arial", 30), "width": 3, "height": 1, 
                     "bg": "#e94560", "fg": "white", "bd": 0, "cursor": "hand2"}

        tk.Button(frame_botoes, text="✊", command=lambda: self.jogar("pedra"), **btn_style).grid(row=0, column=0, padx=15)
        tk.Button(frame_botoes, text="🖐️", command=lambda: self.jogar("papel"), **btn_style).grid(row=0, column=1, padx=15)
        tk.Button(frame_botoes, text="✌️", command=lambda: self.jogar("tesoura"), **btn_style).grid(row=0, column=2, padx=15)

        frame_legenda = tk.Frame(root, bg="#1a1a2e")
        frame_legenda.pack()
        tk.Label(frame_legenda, text="PEDRA", font=("Arial", 10, "bold"), bg="#1a1a2e", fg="white").grid(row=0, column=0, padx=35)
        tk.Label(frame_legenda, text="PAPEL", font=("Arial", 10, "bold"), bg="#1a1a2e", fg="white").grid(row=0, column=1, padx=35)
        tk.Label(frame_legenda, text="TESOURA", font=("Arial", 10, "bold"), bg="#1a1a2e", fg="white").grid(row=0, column=2, padx=35)

    def animar_mao(self, cont=0):
        # Animação da mão balançando tipo jo-ken-po
        if cont < 6:
            texto = "✊" if cont % 2 == 0 else "🤜"
            self.mao_pc_label.config(text=f"{texto}\n\nJO-KEN-PO!")
            self.root.after(150, lambda: self.animar_mao(cont+1))
        else:
            self.mostrar_resultado_animado()

    def jogar(self, escolha_usuario):
        self.escolha_usuario = escolha_usuario
        self.escolha_pc = random.choice(self.opcoes)
        self.sua_jogada_label.config(text=f"Você escolheu: {self.mao_simples[escolha_usuario]} {escolha_usuario.upper()}")
        self.resultado_label.config(text="JO-KEN-PO!!!")
        # Começa animação
        self.animar_mao(0)

    def mostrar_resultado_animado(self):
        # Mostra a mão do PC
        self.mao_pc_label.config(text=self.mao_emoji[self.escolha_pc])

        # Lógica do jogo
        if self.escolha_usuario == self.escolha_pc:
            resultado = "EMPATE! 🤝"
            cor = "#fca311"
            self.empates += 1
        elif (self.escolha_usuario == "pedra" and self.escolha_pc == "tesoura") or \
             (self.escolha_usuario == "papel" and self.escolha_pc == "pedra") or \
             (self.escolha_usuario == "tesoura" and self.escolha_pc == "papel"):
            resultado = "VOCÊ VENCEU! 🎉"
            cor = "#06d6a0"
            self.vitorias_usuario += 1
        else:
            resultado = "PC VENCEU! 🤖"
            cor = "#ef476f"
            self.vitorias_pc += 1

        self.resultado_label.config(text=resultado, fg=cor)
        self.placar_label.config(text=f"Você: {self.vitorias_usuario} | Empates: {self.empates} | PC: {self.vitorias_pc}")

# Iniciar
if __name__ == "__main__":
    root = tk.Tk()
    app = Jogo(root)
    root.mainloop()