# Plataforma de estudo de conjuntos

### O seu projeto consiste em iniciar a criação de uma plataforma de estudo de conjuntos matemáticos para alunos. A plataforma deve permitir que o aluno crie conjuntos e realize operações com eles.

**Requisitos e funcionalidades:**
-  O usuário pode criar quantos conjuntos quiser. Cada conjunto terá um $id$ (identificador único iniciado em "1").
- O programa deve possuir uma interface ("menu"), pelo qual o usuário vai escolher o que fazer (criar conjunto, adicionar elemento, remover elemento e mostrar conjuntos).
- Deve possuir as seguintes funções (mas não se limite a apenas elas):
    - ```menu()``` $\rightarrow$ essa função deve criar um menu e **retornar** a opção que o usuário escolher no menu.
    - ```criar_conjunto()``` $\rightarrow$ essa função deve criar e **retornar** um conjunto vazio (sem elementos).
    - ```add_elemento(id, elemento)``` $\rightarrow$ o usuário informará o conjunto, através do id, e qual elemento quer adicionar. Será adicionado apenas um por vez. 
    - ```del_elemento(id, elemento)``` $\rightarrow$ o usuário informará o conjunto, através do id, e qual elemento quer deletar. Será apagado apenas um por vez. 
    - ```mostrar_conjunto(id)``` $\rightarrow$ essa função mostrará os elementos de um conjunto específico (a partir do seu id).

**NOTA**: Este projeto pode ser feito em dupla e ser mostrado em sala de aula e enviado pelo SUAP posteriormente (não adianta enviar pelo SUAP sem ter mostrado em sala). A dupla deve estar ciente do funcionamento do código por completo para poder ser arguída. Só serão aceitos os conceitos vistos em sala de aula (if, else, while, for, listas e funções). A nota será composta por:
- 1 ponto por cada função (solicitada acima) criada corretamente (total: 5 pontos).
- 1 ponto pela lógica utilizada.
- 1 ponto pelas proteções implementadas.
- 1 ponto pela organização, documentação e nomenclatura das variáveis e funções.
- 2 pontos pelos recursos utilizados no código (estritamente o que foi visto em sala de aula).

*OBS: esse último é mandatório e declassificatório. Ou seja, só use o que foi visto em sala de aula*
