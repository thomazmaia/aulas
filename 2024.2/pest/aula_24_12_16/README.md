# Lista de Exercícios - Strings

1. **Função de Primeira e Última Letra**  
   Escreva uma função chamada `primeiro_e_ultimo` que receba uma string como entrada e retorne uma nova string contendo apenas o primeiro e o último caractere da string original.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: "Python"  
   Saída: "Pn"
   ```

2. **Substring por Índices**  
   Crie uma função chamada `intervalo` que receba uma string e dois índices inteiros. A função deve retornar a substring que está entre esses dois índices, incluindo o caractere no primeiro índice, mas excluindo o do último.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: intervalo("Python", 1, 4)  
   Saída: "yth"
   ```

3. **Reverter String**  
   Escreva uma função chamada `reverter` que aceite uma string como entrada e retorne a string invertida.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: reverter("Python")  
   Saída: "nohtyP"
   ```

4. **Repetir Palavra**  
   Crie uma função chamada `repetir_palavra` que receba uma string e um número inteiro `n` e retorne a string repetida `n` vezes.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: repetir_palavra("Oi", 3)  
   Saída: "OiOiOi"
   ```

5. **Primeiros N Caracteres**  
   Escreva uma função chamada `primeiros_n` que receba uma string e um número inteiro `n` e retorne os primeiros `n` caracteres da string.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: primeiros_n("Programar", 5)  
   Saída: "Progr"
   ```

6. **Últimos N Caracteres**  
   Crie uma função chamada `ultimos_n` que receba uma string e um número inteiro `n` e retorne os últimos `n` caracteres da string.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: ultimos_n("Programar", 4)  
   Saída: "amar"
   ```

7. **Substituir Primeira Letra**  
   Escreva uma função chamada `trocar_primeira_letra` que receba uma string e substitua o primeiro caractere por um `#`.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: trocar_primeira_letra("Python")  
   Saída: "#ython"
   ```

8. **Caracteres Intercalados**  
   Crie uma função chamada `intercalados` que receba uma string e retorne apenas os caracteres nas posições pares da string.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: intercalados("abcdef")  
   Saída: "ace"
   ```

9. **Contar Comprimento**  
   Escreva uma função chamada `comprimento_string` que receba uma string como entrada e retorne o número de caracteres da string.

   **Exemplo de funcionamento:**  
   ```python
   Entrada: comprimento_string("Python")  
   Saída: 6
   ```

10. **Palíndromo Simples**  
    Crie uma função chamada `palindromo_simples` que verifique se uma string é igual à sua reversa. Retorne `True` ou `False`.

    **Exemplo de funcionamento:**  
    ```python
    Entrada: palindromo_simples("arara")  
    Saída: True
    ```

11. **String Sem Espaços**  
    Escreva uma função chamada `remover_espacos` que remova os espaços do início e do fim de uma string usando fatiamento.

    **Exemplo de funcionamento:**  
    ```python
    Entrada: remover_espacos("  Python ")  
    Saída: "Python"
    ```

12. **Duplicar Primeira Metade**  
    Crie uma função chamada `duplicar_metade` que receba uma string e retorne a primeira metade da string duplicada.

    **Exemplo de funcionamento:**  
    ```python
    Entrada: duplicar_metade("Programar")  
    Saída: "ProPro"
    ```

13. **Trocar Metades**  
    Escreva uma função chamada `trocar_metades` que troque a primeira metade de uma string pela segunda metade e retorne a nova string.

    **Exemplo de funcionamento:**  
    ```python
    Entrada: trocar_metades("Pythonista")  
    Saída: "istaPython"
    ```

14. **Inverter Metade Direita**  
    Crie uma função chamada `inverter_direita` que receba uma string e inverta apenas a segunda metade dela.

    **Exemplo de funcionamento:**  
    ```python
    Entrada: inverter_direita("Pythonista")  
    Saída: "Pythontsni"
    ```

15. **Letra Central**  
    Escreva uma função chamada `letra_central` que receba uma string de tamanho ímpar e retorne o caractere central.

    **Exemplo de funcionamento:**  
    ```python
    Entrada: letra_central("Python")  
    Saída: "h"
    ```

