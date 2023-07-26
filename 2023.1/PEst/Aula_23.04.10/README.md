# Exercícios sobre funções

1. Escreva uma função para verificar um número é par ou ímpar.

    Valores esperados:

    ```eh_par_ou_impar(5)``` $\rightarrow$ ímpar

    ```eh_par_ou_impar(2)``` $\rightarrow$ par

---

2. Escreva uma função que retorne o maior de dois números.

    Valores esperados:

    ```maximo(5, 6)``` $\rightarrow$ 6

    ```maximo(2, 1)``` $\rightarrow$ 2

    ```maximo(7, 7)``` $\rightarrow$ 7

---

3. Escreva uma função que receba dois números e retorne ```True``` se o primeiro número for múltiplo do segundo.

    Valores esperados:

    ```eh_multiplo(8, 4)``` $\rightarrow$ True

    ```eh_multiplo(7, 3)``` $\rightarrow$ False

    ```eh_multiplo(6, 3)``` $\rightarrow$ True

---

4. Escreva uma função que receba o lado de um quadrado e retorne sua área ($A = lado^2$)

    Valores esperados:

    ```calc_area_quadrado(3)``` $\rightarrow$ 9

    ```calc_area_quadrado(10)``` $\rightarrow$ 100

---

5. Escreva uma função que receba a base e a altura de um triângulo e retorne sua área ($A = \frac{base \times altura}{2}$)

    Valores esperados:

    ```calc_area_triangulo(6, 9)``` $\rightarrow$ 27.0

    ```calc_area_triangulo(5, 8)``` $\rightarrow$ 20.0

---

6. Escreva uma função que receba uma lista contendo as notas de um aluno e retorne sua média aritmética.

    Valores esperados:

    ```calc_media([4.5, 9.3, 7.8, 8])``` $\rightarrow$ 7.4

    ```calc_media([10])``` $\rightarrow$ 10

    ```calc_media([7, 7, 4])``` $\rightarrow$ 6

---

7. Escreva uma função que receba uma lista contendo as notas de um aluno e um número que representa o valor da média para ser aprovado. A função deve retornar a situação do aluno: aprovado ou reprovado. Caso o usuário não coloque nenhum número, sua função deve adotar 7 como valor padrão.

    Valores esperados:

    ```verifica_se_passou([10, 6, 8], 6)``` $\rightarrow$ Aprovado

    ```verifica_se_passou([7, 7, 4], 6)``` $\rightarrow$ Aprovado

    ```verifica_se_passou([7, 6, 5, 7])``` $\rightarrow$ Reprovado

    ```verifica_se_passou([4.5, 9.3, 7.8, 8])``` $\rightarrow$ Aprovado    

---

8. Escreva uma função que receba duas listas e retorne a lista com mais elementos

    Valores esperados:

    ```verifica_quem_tem_mais([0, 1, 'dois'], ['zero'])``` $\rightarrow$ [0, 1, 'dois']

    ```verifica_quem_tem_mais([True, False, 'true'], [1, 2, 3, 4, 5])``` $\rightarrow$ [1, 2, 3, 4, 5]

---

9. Escreva uma função que receba uma string e retorne essa string toda minúscula com a última letra maiúscula.

    Valores esperados:

    ```muda_string("TESTE")``` $\rightarrow$ testE

    ```muda_string("aula")``` $\rightarrow$ aulA

---

10. Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e o número máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores máximo e mínimo e, falso, caso contrário

    Valores esperados:

    ```verifica_string("Abacaxi", 1, 10)``` $\rightarrow$ True

    ```verifica_string("será que funciona?", 1, 10)``` $\rightarrow$ False

---

11. Escreva uma função para validar uma senha de um usuário. A senha deve ter entre 6 e 10 caracteres, deve possuir pelo menos 3 letras e pelo menos 3 números. Caso seja uma senha válida, retorne True. Caso contrário, retorne False.

    Valores esperados:

    ```verifica_senha("abc123")``` $\rightarrow$ True

    ```verifica_senha("yufghjb65783nd")``` $\rightarrow$ False

    ```verifica_senha("123456789")``` $\rightarrow$ False

    ```verifica_senha("aWsEG@#$sks^")``` $\rightarrow$ False