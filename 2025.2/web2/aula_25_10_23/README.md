# Templates e Static no Flask

### Estrutura de pastas:
- ```controllers```: onde ficam as rotas (funções) da aplicação
- ```templates```: onde ficam os arquivos HTML que serão renderizados plo Flask
- ```static```: onde ficam os arquivos estáticos (CSS, JS, imagens, etc)

### Por que separar HTML, CSS e JS em pastas diferentes?
1. Organização do projeto
- Cada tipo de arquivo tem seu lugar definido
- Fica mais fácil encontrar e alterar apenas aquilo que se quer
- Em projetos maiores, essa organização evita bagunça e perda de tempo
2. Separação de responsabilidades
- HTML: estrutura de conteúdo da página
- CSS: aparência (cores, estilos, posicionamento, etc)
- JavaScript: comportamento e interatividade
3. Reuso e manutenção
- Um mesmo CSS pode ser usado em várias páginas
- Se precisar alterar o estilo, basta mudar em um único arquivo
- Isso reduz erros e facilita correções
4. Padrões de mercado
- Frameworks e equipes profissionais seguem essa mesma lógica
- São boas práticas da área
5. Escalabilidade
- Se o projeto crescer a estrutura continua funcionando
- É possível adicionar novas páginas, novos títulos ou scripts "sem misturar tudo". 

### O que são Templates no Flask?
- São modelos de página HTML que podem ser reutilizados
- O flask usar o motor de templates Jinja2

### Exemplos de uso:
```
<h1> Olá, {{ var }}! </h1>
```


```
<ul>
    {% for item in lista %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

```
{% if usuario_logado %}
    <p>Bem-vindo de volta!</p>
{% else %}
    <p>Faça login para continuar.</p>
{% endif %}
```