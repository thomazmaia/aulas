# Métodos GET e POST
## GET
O método GET é usado quando queremos enviar dados pela URL, normalmente para buscar informações. Ele NÃO É seguro para enviar senhas ou dados sensíveis, uma vez que tudo é visto na barra de endereços. Por padrão, quando acessamos uma rota ou enviamos um formulário sem definir o método, o Flask usa o GET.

## POST 
O método POST é usado para enviar dados de forma oculta (sem aparecer na URL). É o mais indicado para formulários de login, cadastro ou envio de mensagens. O Flask acessa os dados enviados pelo ```request.form```