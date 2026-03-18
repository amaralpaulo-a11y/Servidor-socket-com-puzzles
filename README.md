
# Projeto SOCKET - Jogos em Rede com Python

##  Estrutura do Projeto

```
SOCKET/
│
├── clienteSOCKET.py      # Cliente
├── servidorSOCKET.py     # Servidor
├── modulo_resta1.py      # Jogo "Resta 1"
└── modulo_numpuz.py      # Jogo "Numpuz"
```

---

##  Descrição

Este projeto implementa uma comunicação cliente-servidor usando **sockets TCP em Python**, permitindo:

* Conversa (chat) entre cliente e servidor
* Execução de jogos sob demanda
* Troca de resultados entre os dois lados

---

##  Jogos Disponíveis

* `1` → Numpuz (quebra-cabeça)
* `2` → Resta Um

---

##  Como Executar

### 1. Rodar o servidor

```
python servidorSOCKET.py
```

O terminal exibirá o endereço ip da máquina:




### 2. Configurar o cliente

No arquivo `clienteSOCKET.py`, altere a variável:

```python
HOST = 'SEU_IP_AQUI'
```

Substitua pelo IP exibido no servidor.

---

### 3. Rodar o cliente

```
python clienteSOCKET.py
```

---

##  Como Usar

Após a conexão:

```
1 - Numpuz / 2 - Resta um
```

* Digite `1` ou `2` para iniciar um jogo
* Ou digite qualquer mensagem para usar o chat

---

##  Funcionamento

### Chat

* Cliente e servidor podem trocar mensagens livremente

### Jogos

Quando um dos lados escolhe `1` ou `2`:

1. Ambos executam o jogo localmente
2. O servidor envia seu resultado
3. O cliente envia seu resultado
4. Os resultados são exibidos no terminal

---

##  Observações

* Suporta apenas **1 cliente por vez**
* Funciona em **rede local (mesma Wi-Fi)**
---

##  Melhorias Futuras

* Sistema de pontuação
* Criptografia de mensagens

---

##  Tecnologias

* Python
* Biblioteca `socket`

---

##  Objetivo

Projeto desenvolvido para estudo de:

* Redes de computadores
* Comunicação cliente-servidor
* Programação com sockets

---

##  Licença

Uso livre para fins educacionais.
