# Documentação do Sistema Especialista para Diagnóstico de Problemas em Redes
## Introdução

Este projeto foi desenvolvido como parte da disciplina de Inteligência Computacional I, ministrada no curso de Ciência da Computação da Universidade do Estado do Rio de Janeiro (UERJ). O trabalho foi realizado por um grupo de alunos com o objetivo de aplicar os conceitos teóricos estudados na construção de um sistema especialista funcional e relevante.

### Integrantes do grupo

- Douglas Alexsander Ferreira Corrêa
- Gabriel André de Lima Silva
- João Pedro Valério Corrêa    
- Mateus Mathias da Silva
- Vitor José Lou da Costa    

## 1. Visão Geral

Este projeto consiste em um sistema especialista desenvolvido em Python, cujo objetivo principal é auxiliar usuários leigos a diagnosticarem problemas comuns de conectividade em redes domésticas. A ferramenta simula um atendente técnico virtual que conduz o usuário por uma sequência lógica de verificações, realizando um diagnóstico com base nas respostas fornecidas. A lógica é estruturada como uma árvore de decisão, oferecendo diferentes conclusões conforme o caminho percorrido.

## 2. Objetivo

O objetivo desta aplicação é oferecer uma solução simples, funcional e acessível que permita identificar falhas frequentes em redes locais, como ausência de sinal, problemas de conexão com o roteador, falhas na resolução de nomes (DNS), entre outras. A intenção é reduzir a necessidade de suporte técnico humano em casos triviais, oferecendo recomendações básicas e eficazes para usuários comuns que enfrentam dificuldades de conexão.

## 3. Tecnologias Utilizadas

A aplicação foi desenvolvida em Python 3, utilizando apenas a biblioteca padrão. O paradigma adotado é o de programação baseada em regras, característico de sistemas especialistas. A interface é realizada por meio do terminal, sendo totalmente baseada em texto, com interação simples, por perguntas e respostas.

## 4. Requisitos Funcionais

O sistema realiza uma série de verificações com base nas respostas do usuário. Inicialmente, ele pergunta sobre o status das luzes do modem e do roteador. Em seguida, avalia a integridade da conexão física entre o computador e a rede, seja por cabo ou Wi-Fi. Prossegue verificando se o usuário consegue acessar a página de configuração do roteador, o que indica se há comunicação com a rede local. Depois, testa a conectividade externa acessando um IP público diretamente. Por fim, verifica se o DNS está funcionando ao tentar acessar um site pelo nome. Com base nessas informações, o sistema apresenta um diagnóstico textual com sugestões de ação.

## 5. Requisitos Não Funcionais

Entre os requisitos não funcionais, destaca-se a necessidade de que o sistema funcione de forma totalmente local, sem necessidade de conexão com a internet. A linguagem utilizada nas interações deve ser clara e acessível, permitindo que pessoas sem conhecimento técnico consigam utilizar o assistente. As respostas aceitas devem seguir um padrão binário simples, respondendo apenas com "sim" ou "nao", de modo a facilitar a lógica de verificação e evitar ambiguidade.

## 6. Arquitetura e Funcionamento

O sistema segue uma lógica de decisão sequencial. Ele inicia verificando se o equipamento está ligado corretamente, por meio da observação das luzes do modem/roteador. Se estiver tudo normal, passa para a verificação da conexão física entre o computador e o ponto de acesso, observando se os cabos estão conectados ou se há sinal Wi-Fi. Em seguida, verifica a comunicação local acessando a página do roteador, depois testa a comunicação com a internet acessando um IP público (como 1.1.1.1) e, finalmente, valida o funcionamento do DNS ao tentar acessar um site comum (como [www.google.com](http://www.google.com)). Cada falha em uma dessas etapas leva a um diagnóstico diferente, permitindo identificar com precisão onde está o problema.

## 7. Fluxograma do Diagnóstico

O fluxo de decisão segue a seguinte ordem:

1. Se as luzes do modem ou roteador não estão normais, o problema provavelmente está relacionado a falhas físicas, como energia ou funcionamento do equipamento.
    
2. Se a conexão física entre o computador e a rede estiver com defeito, como um cabo mal encaixado ou sinal Wi-Fi fraco, a causa do problema está nesse ponto.
    
3. Caso a página do roteador não possa ser acessada, há uma indicação de que o dispositivo pode estar com o IP incorreto ou fora da rede local.
    
4. Se o roteador estiver acessível, mas não for possível acessar um IP externo, a falha pode estar relacionada ao provedor de internet (ISP) ou à configuração do modem.
    
5. Se for possível acessar um IP, mas não um site pelo nome, então há uma falha nos servidores de DNS, e a recomendação é alterar as configurações DNS manualmente.
    

Esse encadeamento garante que, ao final do processo, o usuário receba um diagnóstico específico, associado a orientações práticas de resolução.

## 8. Casos de Teste

Foram realizados testes para validar a eficácia do sistema frente a diferentes cenários de falha. No primeiro teste, em que as luzes do modem estavam desligadas, o diagnóstico indicou problema físico com sugestão de verificar a energia. Em outro teste, em que a conexão física não estava correta, o sistema identificou falha de cabo ou Wi-Fi. No terceiro cenário, a página do roteador estava inacessível, indicando problema de IP ou configuração de rede. Quando o IP externo era inacessível, o sistema sugeriu que o problema estava no modem ou provedor. Em um quinto cenário, o IP externo era acessível, mas não era possível acessar sites por nome, o que levou à identificação de problema de DNS. Por fim, no caso em que todas as etapas foram concluídas com sucesso, o sistema concluiu que a conexão estava normal ou que o problema já havia sido resolvido.

## 9. Código-Fonte Principal (Resumo)

A seguir, apresentamos um resumo do código principal da aplicação:

```Python
def diagnose():
	print("Bem-vindo ao assistente de diagnóstico de rede!")
	print("Responda com 'sim' ou 'nao'.")

	if ask_question("As luzes do seu modem/roteador estão normais?") == "nao":
		provide_diagnosis("Problema físico/energia", "Verifique energia ou reinicie.")
		return
		
	if ask_question("A conexão física (cabo/Wi-Fi) está correta?") == "nao":
		provide_diagnosis("Problema local (Cabo/Wi-Fi)", "Verifique cabos, Wi-Fi e reinicie.")
		return
		
	if ask_question("Você consegue acessar a página do roteador?") == "nao":         provide_diagnosis("Problema de IP", "Verifique DHCP ou reinicie roteador.")
		return
		
	if ask_question("Você consegue acessar http://1.1.1.1?") == "nao":         provide_diagnosis("Problema de conectividade geral", "Reinicie o modem/roteador.")
		return
		
		if ask_question("Você consegue acessar http://www.google.com?") == "sim":         provide_diagnosis("Conexão normal", "Monitorar. Problema pode ter sido resolvido.")
		else:
		provide_diagnosis("Problema de DNS", "Configure DNS manualmente ou reinicie.")
```

## 10. Conclusão
    
O sistema desenvolvido apresentou resultados satisfatórios durante os testes, sendo capaz de diagnosticar corretamente falhas simples de rede. Sua lógica baseada em regras o torna ideal para ser expandido ou integrado a interfaces mais avançadas. A linguagem acessível e a simplicidade da interação o tornam útil para pessoas com pouco conhecimento técnico. Além disso, pode servir como base para aplicações futuras, que automatizem testes em segundo plano ou que incluam interfaces mais modernas, como web ou aplicativos móveis.