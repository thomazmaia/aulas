**Jogo da Forca**: Crie um jogo da forca em Python utilizando apenas conceitos de: if/else/elif, while, for e strings. O programa irá selecionar aleatoriamente uma palavra a partir de uma lista de palavras predefinidas e exibir o número de letras da palavra na tela (um traço para cada letra). O jogo deve mostrar quando o usuário acertar a letra e quando ele errar. O jogo não deve aceitar (nem computar) uma letra já utilizada (seja ela minúscula ou maiúscula). O jogo deve, ainda, "desenhar" a forca se formando a cada erro do usuário conforme desenho abaixo. Se o jogador adivinhar a palavra antes do boneco estar completo, ele ganha o jogo.

- Funcionamento do programa:
1. Selecionar aleatoriamente uma palavra de uma lista de palavras predefinidas.
2. Exibir o número de letras da palavra na tela, representado por um traço para cada letra.
3. Pedir ao jogador para adivinhar uma letra.
4. Verificar se a letra está na palavra secreta.
5. Se a letra estiver na palavra, exibir a letra na posição correspondente.
6. Se a letra não estiver na palavra, desenhar uma parte do boneco da forca.
7. Continuar pedindo ao jogador para adivinhar letras até que ele adivinhe a palavra ou o
boneco esteja completo.
8. Exibir uma mensagem de vitória ou derrota na tela.

- Requisitos técnicos:
1. O programa deve usar listas e strings para selecionar aleatoriamente uma palavra e
exibir o número de letras.
2. O programa deve ter uma interface de usuário simples e intuitiva.
3. O programa deve permitir que o jogador adivinhe uma letra por vez.
4. O programa deve desenhar o boneco da forca à medida que o jogador erra as letras.
5. O programa deve permitir que o jogador jogue novamente após vencer ou perder.

*Nota: Este projeto pode ser feito em equipe de até 4 pessoas e enviado pelo SUAP. Cada membro da equipe deve contribuir com a implementação do programa e com a documentação do projeto. **A nota será baseada na qualidade do código (organização, nome de variáveis, lógica utilizada, etc), na funcionalidade do programa e na documentação do projeto.***

- Desenho da forca:
```
 ----
 |  |
 |  o
 | /|\
 | / \
_|_
```