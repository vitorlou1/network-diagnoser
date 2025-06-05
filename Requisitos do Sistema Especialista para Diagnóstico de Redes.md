# Requisitos do Sistema Especialista para Diagnóstico de Redes

## 1. Objetivo
Desenvolver um sistema especialista baseado em regras para auxiliar usuários leigos a diagnosticar problemas comuns de conectividade em redes domésticas ou de pequeno escritório.

## 2. Escopo do Diagnóstico
O sistema deverá ser capaz de identificar e sugerir soluções para os seguintes problemas:
    - **Falha na obtenção de endereço IP:** Verificar se o dispositivo possui um endereço IP válido (via DHCP ou configuração estática).
    - **Problemas de DNS:** Verificar se o dispositivo consegue resolver nomes de domínio.
    - **Problemas de Conectividade com o Roteador:** Verificar se o dispositivo consegue se comunicar com o gateway padrão (roteador).
    - **Problemas Físicos Básicos:** Incluir verificações simples de conexão física (cabos, status do Wi-Fi, luzes do roteador).

## 3. Interação com o Usuário
    - **Interface:** Baseada em texto, via console (linha de comando).
    - **Fluxo:** Guiado por perguntas sequenciais (Sim/Não, múltipla escolha).
    - **Inferência:** Passo a passo, explicando o raciocínio e os testes sugeridos.
    - **Instruções:** O sistema poderá solicitar ao usuário que verifique indicadores físicos (luzes do modem/roteador) ou execute comandos simples (como `ping`, se aplicável e seguro no contexto do usuário).

## 4. Base de Conhecimento
    - **Formato:** Regras IF-THEN.
    - **Exemplos de Regras:**
        - SE não há conectividade com a internet E não há endereço IP VÁLIDO ENTÃO o problema pode ser DHCP ou conexão física com o roteador.
        - SE há endereço IP VÁLIDO E não consegue acessar websites MAS consegue pingar um IP externo (ex: 8.8.8.8) ENTÃO o problema provavelmente é DNS.
        - SE não consegue pingar o gateway padrão ENTÃO o problema pode ser conexão física/Wi-Fi com o roteador ou o roteador em si.

## 5. Plataforma e Entrega
    - **Linguagem:** Python 3.
    - **Entrega:** Código-fonte (.py) comentado e este documento de requisitos.

## 6. Suposições
    - O usuário tem acesso ao dispositivo com problema de rede.
    - O usuário consegue seguir instruções simples e responder às perguntas do sistema.
    - O sistema não executará comandos de rede automaticamente, apenas guiará o usuário.

## 7. Próximos Passos (Plano)
    - Planejar o fluxo detalhado de diagnóstico e as regras de inferência.
    - Implementar a interface de usuário.
    - Desenvolver o motor de inferência.
    - Validar com casos de teste.
    - Entregar o sistema.
