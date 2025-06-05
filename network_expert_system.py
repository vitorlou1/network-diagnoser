# -*- coding: utf-8 -*-
"""
Sistema Especialista para Diagnóstico de Problemas em Redes (GUI)

Este script implementa uma Interface Gráfica de Usuário (GUI) com Tkinter
para o sistema especialista de diagnóstico de rede.
"""

import tkinter as tk
from tkinter import scrolledtext

class NetworkDiagnosisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistente de Diagnóstico de Rede")
        self.root.geometry("500x400") # Ajuste de altura para melhor visualização
        self.root.resizable(False, False) # Impede redimensionamento

        # Variável para armazenar o estado atual do diagnóstico (índice da pergunta/passo)
        self.current_step_index = -1 # -1 indica estado inicial
        # Dicionário para armazenar as perguntas e a lógica de fluxo
        # A chave é o índice do passo, o valor é uma tupla: 
        # (texto_da_pergunta, indice_se_sim, indice_se_nao, eh_diagnostico_final)
        # Índices negativos indicam diagnósticos finais (chave no self.diagnoses)
        self.steps = {}
        self.diagnoses = {}

        # --- Widgets --- 
        self.question_label = tk.Label(root, text="Bem-vindo! Clique em 'Iniciar'.", wraplength=480, justify="center", font=("Arial", 12), height=4)
        self.question_label.pack(pady=(20, 10), padx=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.yes_button = tk.Button(self.button_frame, text="Sim", width=10, command=self.handle_yes, state=tk.DISABLED)
        self.yes_button.pack(side=tk.LEFT, padx=10)

        self.no_button = tk.Button(self.button_frame, text="Não", width=10, command=self.handle_no, state=tk.DISABLED)
        self.no_button.pack(side=tk.LEFT, padx=10)

        self.diagnosis_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=8, width=60, state=tk.DISABLED, font=("Arial", 10))
        self.diagnosis_text.pack(pady=10, padx=10)

        self.restart_button = tk.Button(root, text="Iniciar Diagnóstico", width=20, command=self.start_diagnosis)
        self.restart_button.pack(pady=(5, 15))

        # --- Preencher Lógica (Será feito na Integração - Passo 004) ---
        self.populate_steps() # Método placeholder por enquanto

    def populate_steps(self):
        """Preenche a estrutura de passos e diagnósticos (Placeholder)."""
        # Esta função será preenchida no passo 004 com a lógica real
        self.steps = {
            0: ("As luzes do modem/roteador parecem normais?", 1, -1, False), # -1 -> Diagnóstico 1
            1: ("A conexão física (cabo/Wi-Fi) está correta?", 2, -2, False), # -2 -> Diagnóstico 2
            2: ("Consegue acessar a página do roteador (ex: 192.168.0.1)?", 3, -3, False), # -3 -> Diagnóstico 3
            3: ("Consegue acessar um IP externo (ex: 1.1.1.1)?", 4, -4, False), # -4 -> Diagnóstico 4
            4: ("Consegue acessar um site pelo nome (ex: google.com)?", -5, -6, False) # -5 -> Diagnóstico 5, -6 -> Diagnóstico 6
        }
        self.diagnoses = {
            -1: ("Problema físico/energia no modem/roteador.", "Verifique as conexões de energia e reinicie os aparelhos. Se persistir, contate o provedor ou verifique o equipamento."),
            -2: ("Problema na conexão física local (Cabo ou Wi-Fi).", "Verifique cabos, conexão Wi-Fi, senha e sinal. Reinicie o dispositivo e o roteador."),
            -3: ("Problema de IP ou comunicação com o roteador.", "Reinicie o dispositivo e o roteador. Verifique se o DHCP está ativo (obter IP automaticamente)."),
            -4: ("Problema de conectividade geral com a internet.", "Reinicie modem e roteador. Verifique o status do serviço com seu provedor."),
            -5: ("Conexão parece normal ou problema resolvido.", "Aparentemente tudo está funcionando. Monitore a conexão."),
            -6: ("Problema de DNS (Resolução de Nomes).", "Reinicie o roteador. Considere configurar DNS manualmente (ex: 1.1.1.1 ou 8.8.8.8) no dispositivo ou roteador.")
        }
        print("Estrutura de passos e diagnósticos carregada (placeholder).") # Log para desenvolvimento

    def update_ui(self, question=None, diagnosis_tuple=None, show_buttons=True, show_restart=False):
        """Atualiza a interface com a nova pergunta ou diagnóstico."""
        if question:
            self.question_label.config(text=question)
        else:
             self.question_label.config(text="") # Limpa se não houver pergunta

        self.diagnosis_text.config(state=tk.NORMAL)
        self.diagnosis_text.delete('1.0', tk.END)
        if diagnosis_tuple:
            reason, suggestion = diagnosis_tuple
            self.question_label.config(text="Diagnóstico Final:") # Atualiza label principal
            full_diagnosis = f"Causa Provável: {reason}\n\nSugestão: {suggestion}\n\nSe o problema persistir, contate o suporte."
            self.diagnosis_text.insert(tk.END, full_diagnosis)
        self.diagnosis_text.config(state=tk.DISABLED)

        if show_buttons:
            self.yes_button.config(state=tk.NORMAL)
            self.no_button.config(state=tk.NORMAL)
        else:
            self.yes_button.config(state=tk.DISABLED)
            self.no_button.config(state=tk.DISABLED)

        if show_restart:
            self.restart_button.config(text="Reiniciar Diagnóstico", state=tk.NORMAL)
        else:
            # Mantém o botão iniciar/reiniciar, mas pode desabilitá-lo durante o processo
             self.restart_button.config(state=tk.DISABLED)

    def show_step(self, step_index):
        """Exibe a pergunta ou o diagnóstico correspondente ao índice."""
        self.current_step_index = step_index

        if step_index >= 0: # É uma pergunta
            if step_index in self.steps:
                question_text, _, _, _ = self.steps[step_index]
                self.update_ui(question=question_text, show_buttons=True, show_restart=False)
            else:
                # Fallback para erro inesperado no fluxo
                self.show_final_diagnosis(-99) # Índice de erro
        else: # É um diagnóstico final
            self.show_final_diagnosis(step_index)

    def show_final_diagnosis(self, diagnosis_index):
        """Exibe o diagnóstico final na interface."""
        if diagnosis_index in self.diagnoses:
            diagnosis_tuple = self.diagnoses[diagnosis_index]
            self.update_ui(diagnosis_tuple=diagnosis_tuple, show_buttons=False, show_restart=True)
        else:
             # Diagnóstico de erro não encontrado
             error_tuple = ("Erro no fluxo de diagnóstico.", "Ocorreu um erro inesperado. Tente reiniciar.")
             self.update_ui(diagnosis_tuple=error_tuple, show_buttons=False, show_restart=True)

    def handle_yes(self):
        """Processa a resposta 'Sim'."""
        if self.current_step_index in self.steps:
            _, next_step_if_yes, _, _ = self.steps[self.current_step_index]
            self.show_step(next_step_if_yes)
        else:
            print(f"Erro: Tentativa de 'Sim' em estado inválido {self.current_step_index}")
            self.show_final_diagnosis(-99) # Erro

    def handle_no(self):
        """Processa a resposta 'Não'."""
        if self.current_step_index in self.steps:
            _, _, next_step_if_no, _ = self.steps[self.current_step_index]
            self.show_step(next_step_if_no)
        else:
            print(f"Erro: Tentativa de 'Não' em estado inválido {self.current_step_index}")
            self.show_final_diagnosis(-99) # Erro

    def start_diagnosis(self):
        """Inicia ou reinicia o processo de diagnóstico."""
        print("Iniciando/Reiniciando diagnóstico...")
        self.show_step(0) # Começa do passo 0

# --- Ponto de Entrada --- 
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkDiagnosisApp(root)
    root.mainloop()