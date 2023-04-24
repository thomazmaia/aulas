# Plataforma de estudo de conjuntos

### O seu projeto consiste em criar uma plataforma de estudo de conjuntos matemáticos para alunos. A plataforma deve permitir que o aluno crie conjuntos e realize operações com eles.

**Requisitos e funcionalidades:**
- O usuário pode criar quantos conjuntos quiser. Cada conjunto terá um $id$ (identificador único iniciado em "1").
- O programa deve possuir uma interface ("menu"), pelo qual o usuário vai escolher o que fazer conforme as funções abaixo descritas. As opções do menu devem ser:
    - Digite "1" para criar um novo conjunto vazio.
    - Digite "2" para adicionar um elemento a um conjunto existente.
    - Digite "3" para remover um elemento de um conjunto existente.
    - Digite "4" para encontrar a união entre conjuntos distintos.
    - Digite "5" para encontrar a interseção entre conjuntos distintos.
    - Digite "6" para mostrar um conjunto específico.
    - Digite qualquer outra tecla para sair.
- Ao digitar 1, o usuário verá o id do conjunto que foi criado.
- Ao digitar 2, o usuário deve informar, de uma só vez (em uma única linha), o id do conjunto seguido do(s) elemento(s) que ele quer adicionar. Não deve ser possível adicionar elementos em um conjunto que não existe.

> ex:
>
> [programa] Digite o conjunto e o(s) elemento(s) que deseja adicionar:
>
> [usuário] 2 abacaxi 1 @ #
>> *Nesse caso, o programa deve adicionar os elementos "abacaxi", "1", "@" e "#" ao conjunto 2.*

- Ao digitar 3, o usuário deve informar, de uma só vez (em uma única linha), o id do conjunto seguido do(s) elemento(s) que ele quer remover. Não deve ser possível remover elementos em um conjunto que não existe e nem remover elementos inexistentes no conjunto.
- Ao digitar 4, o usuário deve informar, de uma só vez (em uma única linha), os ids dos conjuntos que ele quer ver a união.

*OBS: A união entre conjuntos corresponde a junção dos elementos dos conjuntos dados, ou seja, é o conjunto formado pelos elementos de um conjunto mais os elementos dos outros conjuntos.*

- Ao digitar 5, o usuário deve informar, de uma só vez (em uma única linha), os ids dos conjuntos que ele quer ver a interseção.

*OBS: A interseção entre conjuntos aos elementos que se repetem nos conjuntos dados, ou seja, é o conjunto formado pelos elementos de um conjunto que também estão nos outros conjuntos.*

- Ao digitar 6, o usuário deve informar o id de qual conjunto ele quer ver os elementos.
- Sempre que o usuário adicinar ou remover um elemento, deve ser mostrado, após a operação, como ficou o conjunto.

- Deve possuir as seguintes funções (mas não se limite a apenas elas):
    - ```criar_conjunto()``` $\rightarrow$ essa função deve criar e **retornar** um conjunto vazio (sem elementos).
    - ```add_elemento(id, elemento)``` $\rightarrow$ o usuário informará o conjunto, através do id, e qual(is) elemento(s) quer adicionar. Pode ser adicionado mais de um elemento por vez.
    - ```del_elemento(id, elemento)``` $\rightarrow$ o usuário informará o conjunto, através do id, e qual(is) elemento(s) quer deletar. Pode ser deletado mais de um elemento por vez.
    - ```mostrar_conjunto(id)``` $\rightarrow$ essa função mostrará os elementos de um conjunto específico (a partir do seu id).
    - ```uniao(ids)``` $\rightarrow$ essa função receberá uma **lista** de ids representando vários conjuntos e **retornará** a união desses conjuntos.
    - ```intersecao(ids)``` $\rightarrow$ essa função receberá uma **lista** de ids representando vários conjuntos e **retornará** a interseção desses conjuntos.


**NOTA**: Este projeto pode ser feito em dupla e deve ser mostrado em sala de aula e enviado pelo SUAP posteriormente (não adianta enviar pelo SUAP sem ter mostrado em sala). A dupla deve estar ciente do funcionamento do código por completo para poder ser arguída. Só serão aceitos os conceitos vistos em sala de aula (if, else, while, for, listas e funções). A nota será composta por:
- 1 ponto por cada função (acima) criada corretamente
- 2 pontos pelos nomes das variáveis e funções
- 2 pontos pela documentação do código
