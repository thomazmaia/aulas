# Fluxo de execução no FLASK:

1. O arquivo principal (``__init__``) importa o Flask e cria as bases do site.
2. As rotas são criadas em um arquivo separado chamado de ``routes.py`` ou ``views.py``.
3. O arquivo principal importa as rotas do arquivo de views e esse precisa importar o ``app`` do ``__init__`` para que a conexao funcione.
4. Para criar um site (visual) o Flask pode renderizar templates HTML. Para isso você divide em duas pastas: ``templates``, onde são armazenados os arquivos HTML, e ``static``, onde são salvos os arquivos estáticos de CSS, JS e outros.
5. Para funcionalidades adicionais, como bancos de dados, você pode usar extensões como o ``Flask-SQLAlchemy``e criar um arquivo ``models.py``para configurar as tabelas. Para formulários, o ``Flask-WTFForms`` é utilizado e um arquivo ``forms.py`` deve ser criado.