# Casos de Teste para o Sistema Especialista de Diagnóstico de Redes

Este documento descreve os casos de teste para validar o sistema especialista.

**Metodologia:** Simulação manual das respostas do usuário no script `network_expert_system.py` e verificação do diagnóstico final.

**Script Testado:** `network_expert_system.py` (versão após passo 004)

---

**Caso 1: Problema Físico (Luzes Anormais)**
*   **Objetivo:** Validar o diagnóstico quando as luzes do modem/roteador estão anormais.
*   **Respostas Simuladas:**
    1.  Luzes normais? `nao`
*   **Diagnóstico Esperado:** "Problema físico/energia no modem/roteador."
*   **Resultado:** Conforme esperado. O script termina após a primeira pergunta com o diagnóstico correto.

---

**Caso 2: Problema Físico (Conexão Local Incorreta)**
*   **Objetivo:** Validar o diagnóstico quando há problema na conexão física local (cabo ou Wi-Fi).
*   **Respostas Simuladas:**
    1.  Luzes normais? `sim`
    2.  Conexão física OK (Cabo/Wi-Fi)? `nao`
*   **Diagnóstico Esperado:** "Problema na conexão física local (Cabo ou Wi-Fi)."
*   **Resultado:** Conforme esperado. O script termina após a segunda pergunta com o diagnóstico correto.

---

**Caso 3: Problema de IP/Comunicação com Roteador**
*   **Objetivo:** Validar o diagnóstico quando não é possível acessar a página do roteador.
*   **Respostas Simuladas:**
    1.  Luzes normais? `sim`
    2.  Conexão física OK? `sim`
    3.  Acessou página do roteador (192.168...)? `nao`
*   **Diagnóstico Esperado:** "Problema na comunicação com o roteador ou na obtenção de endereço IP."
*   **Resultado:** Conforme esperado. O script termina após a terceira pergunta com o diagnóstico correto.

---

**Caso 4: Problema de Conectividade Geral (ISP/Modem/Roteador)**
*   **Objetivo:** Validar o diagnóstico quando não há acesso a IPs externos.
*   **Respostas Simuladas:**
    1.  Luzes normais? `sim`
    2.  Conexão física OK? `sim`
    3.  Acessou página do roteador? `sim`
    4.  Acessou IP externo (1.1.1.1)? `nao`
*   **Diagnóstico Esperado:** "Problema de conectividade geral com a internet."
*   **Resultado:** Conforme esperado. O script termina após a quarta pergunta com o diagnóstico correto.

---

**Caso 5: Problema de DNS**
*   **Objetivo:** Validar o diagnóstico quando há acesso a IP externo, mas não a nomes de domínio.
*   **Respostas Simuladas:**
    1.  Luzes normais? `sim`
    2.  Conexão física OK? `sim`
    3.  Acessou página do roteador? `sim`
    4.  Acessou IP externo (1.1.1.1)? `sim`
    5.  Acessou site por nome (google.com)? `nao`
*   **Diagnóstico Esperado:** "Problema de DNS (Resolução de Nomes)."
*   **Resultado:** Conforme esperado. O script termina após a quinta pergunta com o diagnóstico correto.

---

**Caso 6: Tudo OK**
*   **Objetivo:** Validar o fluxo quando não há problemas aparentes.
*   **Respostas Simuladas:**
    1.  Luzes normais? `sim`
    2.  Conexão física OK? `sim`
    3.  Acessou página do roteador? `sim`
    4.  Acessou IP externo (1.1.1.1)? `sim`
    5.  Acessou site por nome (google.com)? `sim`
*   **Diagnóstico Esperado:** "Conexão parece normal ou problema foi resolvido."
*   **Resultado:** Conforme esperado. O script percorre todas as perguntas e fornece o diagnóstico final indicando normalidade.

---

**Conclusão da Validação:** O sistema especialista se comportou conforme o esperado em todos os casos de teste simulados, cobrindo os principais cenários de diagnóstico definidos no fluxo. A lógica de inferência está funcionando corretamente para direcionar o usuário ao diagnóstico apropriado com base nas respostas.
