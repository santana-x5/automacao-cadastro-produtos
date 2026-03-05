# Automação de Cadastro de Produtos

Este projeto foi desenvolvido para automatizar o processo de cadastro de produtos em um sistema web. Utilizando scripts em Python, o sistema lê um arquivo CSV contendo os dados dos produtos e realiza o preenchimento automático dos campos no navegador, economizando tempo e reduzindo erros manuais.

## 📋 Funcionalidades

* **Leitura de Dados:** Processamento de planilhas de produtos (`produtos.csv`) utilizando Pandas.
* **Automação de Interface:** Uso do `PyAutoGUI` para simular cliques, digitação e navegação no navegador.
* **Agilidade:** Cadastro em massa automatizado, permitindo que o usuário apenas acompanhe o processo.

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Pandas**: Manipulação da base de dados.
* **PyAutoGUI**: Automação de eventos de teclado e mouse.

## 🚀 Como Executar

1. **Pré-requisitos:**
   - Instale as bibliotecas necessárias: `pip install pyautogui pandas`.
   - Certifique-se de ter o arquivo `produtos.csv` no diretório raiz.

2. **Ajuste de Coordenadas (Muito Importante):**
   - O script `automacao.py` utiliza coordenadas específicas de clique (`x`, `y`) baseadas na resolução da minha tela.
   - **Como ajustar:**
     1. Execute o script `teste.py`.
     2. Você terá 5 segundos para mover o seu mouse até o campo onde deseja clicar no navegador.
     3. O script irá imprimir no terminal a posição atual (`Point(x=..., y=...)`).
     4. Substitua os valores de `x` e `y` no seu arquivo `automacao.py` pelas coordenadas encontradas na sua máquina.

3. **Execução:**
   - Feche outras janelas desnecessárias, execute o script: `python automacao.py` e **não mova o mouse** durante o processo.

## 👤 Autor

* **[Klinger felix xavier santana]**
    * [www.linkedin.com/in/klinger-santana-8357723a8/]
    * [Github.com/santana-x5]

## 📝 Licença

Este projeto está sob a licença [Escolha uma licença, ex: MIT].