# Fluxo de Diagnóstico e Regras de Inferência

Este documento detalha o fluxo de perguntas e as regras de inferência para o Sistema Especialista de Diagnóstico de Redes.

## 1. Início
   - **Mensagem:** "Bem-vindo ao assistente de diagnóstico de rede! Vou fazer algumas perguntas para tentar identificar o problema. Por favor, responda com 'sim' ou 'nao'."
   - **Pergunta Inicial:** "Você está sem acesso à internet ou a algum recurso específico da rede?" (Embora o foco seja 'sem internet', esta pergunta abre margem)
   - **Próximo Passo:** Verificar Conexão Física.

## 2. Verificação da Conexão Física
   - **Pergunta 2.1:** "As luzes indicadoras do seu modem e roteador (se separados) parecem normais? (Ex: Luz 'Power' acesa, luz 'Internet'/'WAN' acesa ou piscando, luz 'WLAN'/'Wi-Fi' acesa?)"
     - **SE** 'nao' **ENTÃO** Diagnóstico: Problema físico/energia. Sugestão: "Verifique as conexões de energia do modem/roteador. Se persistir, tente reiniciá-los (desligar da tomada por 30s e ligar novamente). Se ainda assim as luzes não normalizarem, pode haver um problema com o equipamento ou com o sinal da operadora."
     - **SE** 'sim' **ENTÃO** Prosseguir para 2.2.
   - **Pergunta 2.2 (se aplicável):** "Se você usa um cabo de rede, ele está firmemente conectado ao seu computador e ao roteador?"
     - **SE** 'nao' **ENTÃO** Diagnóstico: Cabo desconectado. Sugestão: "Conecte o cabo firmemente nas duas pontas."
     - **SE** 'sim' **ENTÃO** Prosseguir para 2.3.
   - **Pergunta 2.3 (se aplicável):** "Se você usa Wi-Fi, o seu dispositivo indica que está conectado à sua rede Wi-Fi corretamente?"
     - **SE** 'nao' **ENTÃO** Diagnóstico: Problema de conexão Wi-Fi. Sugestão: "Verifique se o Wi-Fi está ativado no seu dispositivo, selecione a rede correta e digite a senha, se necessário. Tente se aproximar do roteador."
     - **SE** 'sim' **ENTÃO** Prosseguir para Verificação de IP.

## 3. Verificação do Endereço IP
   - **Pergunta 3.1:** "Vamos tentar acessar a página de configuração do seu roteador. Abra o navegador e digite o endereço padrão (geralmente http://192.168.0.1 ou http://192.168.1.1). Você conseguiu acessar a página do roteador?"
     - **SE** 'sim' **ENTÃO** Inferência: Conexão local com o roteador está OK. Provavelmente tem IP. Prosseguir para Verificação de Gateway/DNS.
     - **SE** 'nao' **ENTÃO** Diagnóstico: Problema na obtenção de IP ou comunicação com o roteador. Sugestão: "Parece haver um problema na comunicação inicial com o roteador ou na obtenção de um endereço IP. Tente reiniciar seu computador e o roteador. Verifique se o DHCP está ativado nas configurações de rede do seu computador (geralmente é o padrão 'obter IP automaticamente')."

## 4. Verificação de Gateway e DNS
   - **Pergunta 4.1:** "Agora, tente acessar um site diretamente pelo endereço IP. Abra o navegador e digite http://1.1.1.1 (servidor DNS da Cloudflare). Você conseguiu carregar uma página (mesmo que seja de erro ou informação)?"
     - **SE** 'sim' **ENTÃO** Inferência: Conectividade com a internet externa (nível IP) parece funcionar. O problema pode ser o DNS. Prosseguir para 4.2.
     - **SE** 'nao' **ENTÃO** Diagnóstico: Problema de conectividade geral com a internet. Sugestão: "Não foi possível acessar um endereço externo. Isso pode indicar um problema no roteador, no modem ou com o seu provedor de internet (ISP). Reinicie o modem e o roteador. Se não resolver, verifique o status do serviço com seu provedor."
   - **Pergunta 4.2:** "Já que você acessou o IP externo, tente acessar um site comum, como http://www.google.com. Você consegue acessar?"
     - **SE** 'sim' **ENTÃO** Diagnóstico: O problema pode ter sido temporário ou resolvido com os passos anteriores. Sugestão: "Parece que a conexão foi restabelecida. Monitore e veja se o problema retorna."
     - **SE** 'nao' **ENTÃO** Diagnóstico: Problema de DNS. Sugestão: "Você consegue acessar a internet por IP, mas não por nomes (como google.com). Isso indica um problema de DNS. Tente reiniciar o roteador. Se não funcionar, você pode tentar configurar manualmente os servidores DNS no seu computador ou roteador para 1.1.1.1 e 1.0.0.1 (Cloudflare) ou 8.8.8.8 e 8.8.4.4 (Google)."

## 5. Fim
   - Apresentar o diagnóstico final e as sugestões baseadas no caminho percorrido no fluxo.
   - **Mensagem:** "Com base nas suas respostas, o problema mais provável é [Diagnóstico]. Sugiro que você tente [Sugestão]. Se o problema persistir, pode ser necessário contatar o suporte técnico do seu provedor de internet ou um técnico especializado."
