# -*- coding: utf-8 -*-
"""
Sistema Especialista para Diagnóstico de Problemas em Redes

Este script implementa um sistema especialista baseado em regras para
ajudar usuários a diagnosticar problemas comuns de conectividade de rede,
guiando-os através de uma sequência de perguntas.
"""

def ask_question(question):
    """Faz uma pergunta ao usuário e retorna a resposta normalizada (sim/nao)."""
    while True:
        try:
            answer = input(f"\n{question} (sim/nao): ").strip().lower()
            if answer in ["sim", "s"]:
                return "sim"
            elif answer in ["nao", "n"]:
                return "nao"
            else:
                print("Por favor, responda apenas com 'sim' ou 'nao'.")
        except EOFError:
            print("\nEntrada inesperada. Saindo.")
            return "nao" # Assume nao em caso de erro de entrada
        except KeyboardInterrupt:
            print("\nDiagnóstico interrompido pelo usuário. Saindo.")
            exit()

def provide_diagnosis(reason, suggestion):
    """Apresenta o diagnóstico final e a sugestão."""
    print("\n--- Diagnóstico Final ---")
    print(f"Causa Provável: {reason}")
    print(f"Sugestão: {suggestion}")
    print("\nSe o problema persistir, pode ser necessário contatar o suporte técnico do seu provedor de internet ou um técnico especializado.")

def diagnose():
    """Executa o fluxo principal de diagnóstico."""
    print("Bem-vindo ao assistente de diagnóstico de rede!")
    print("Vou fazer algumas perguntas para tentar identificar o problema.")
    print("Por favor, responda com 'sim' ou 'nao'.")

    # --- 1. Início (Implícito) ---

    # --- 2. Verificação da Conexão Física ---
    print("\n--- Verificando Conexões Físicas ---")
    lights_ok = ask_question("As luzes indicadoras do seu modem e roteador (se separados) parecem normais? (Ex: Luz 'Power' acesa, luz 'Internet'/'WAN' acesa ou piscando, luz 'WLAN'/'Wi-Fi' acesa?)")

    if lights_ok == "nao":
        provide_diagnosis(
            "Problema físico/energia no modem/roteador.",
            "Verifique as conexões de energia do modem/roteador. Se persistir, tente reiniciá-los (desligar da tomada por 30s e ligar novamente). Se ainda assim as luzes não normalizarem, pode haver um problema com o equipamento ou com o sinal da operadora."
        )
        return

    # Assumindo que o usuário verifica o tipo de conexão relevante para ele
    connection_physical_ok = ask_question("A conexão física entre seu dispositivo e o roteador está correta? (Cabo de rede bem conectado OU conectado à rede Wi-Fi correta com sinal bom?)")
    if connection_physical_ok == "nao":
         provide_diagnosis(
            "Problema na conexão física local (Cabo ou Wi-Fi).",
            "Se usa cabo, verifique se está bem conectado nas duas pontas. Se usa Wi-Fi, confira se está conectado à rede correta, com a senha certa e se o sinal está bom. Tente reiniciar o dispositivo e o roteador."
        )
         return

    print("\nVerificações físicas básicas parecem OK. Prosseguindo...")

    # --- 3. Verificação do Endereço IP / Conexão com Roteador ---
    print("\n--- Verificando Conexão com o Roteador ---")
    router_page_accessible = ask_question("Tente acessar a página de configuração do seu roteador. Abra o navegador e digite o endereço padrão (geralmente http://192.168.0.1 ou http://192.168.1.1). Você conseguiu acessar a página do roteador (mesmo que peça senha)?")

    if router_page_accessible == "nao":
        provide_diagnosis(
            "Problema na comunicação com o roteador ou na obtenção de endereço IP.",
            "Parece haver um problema na comunicação inicial com o roteador ou na obtenção de um endereço IP válido. Tente reiniciar seu computador/dispositivo e o roteador. Verifique se as configurações de rede do seu dispositivo estão para obter IP automaticamente (DHCP)."
        )
        return

    print("\nConexão com o roteador parece OK. Prosseguindo para teste de internet...")

    # --- 4. Verificação de Gateway e DNS ---
    print("\n--- Verificando Conectividade Externa e DNS ---")
    external_ip_accessible = ask_question("Agora, tente acessar um site diretamente pelo endereço IP. Abra o navegador e digite http://1.1.1.1 (servidor DNS da Cloudflare). Você conseguiu carregar alguma página (mesmo que de erro/informação, diferente de 'não encontrado')? ")

    if external_ip_accessible == "nao":
        provide_diagnosis(
            "Problema de conectividade geral com a internet.",
            "Não foi possível acessar um endereço IP externo diretamente. Isso pode indicar um problema no roteador, no modem ou com o seu provedor de internet (ISP). Reinicie o modem e o roteador (desligue da tomada por 30s). Se não resolver, verifique o status do serviço com seu provedor."
        )
        return

    # Se chegou aqui, consegue acessar IP externo, testar DNS
    print("\nConectividade externa (nível IP) parece funcionar. Testando resolução de nomes (DNS)...")
    common_site_accessible = ask_question("Já que você acessou o IP externo, tente acessar um site comum pelo nome, como http://www.google.com. Você consegue acessar?" )

    if common_site_accessible == "sim":
        provide_diagnosis(
            "Conexão parece normal ou problema foi resolvido.",
            "Parece que a conexão com a internet foi restabelecida e a resolução de nomes (DNS) está funcionando. O problema pode ter sido temporário. Monitore a conexão."
        )
        return
    else:
        provide_diagnosis(
            "Problema de DNS (Resolução de Nomes).",
            "Você consegue acessar a internet por IP, mas não por nomes (como google.com). Isso indica um problema de DNS. Tente reiniciar o roteador. Se não funcionar, você pode tentar configurar manualmente os servidores DNS no seu computador ou roteador para 1.1.1.1 e 1.0.0.1 (Cloudflare) ou 8.8.8.8 e 8.8.4.4 (Google). Consulte o manual do seu sistema operacional ou roteador para saber como fazer isso."
        )
        return

# Ponto de entrada do script
if __name__ == "__main__":
    diagnose()

