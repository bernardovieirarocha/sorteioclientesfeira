# Sorteio de Clientes Feira

Este projeto foi desenvolvido para realizar um sorteio de prêmios personalizado para um evento específico, permitindo que cada participante seja registrado e um sorteio seja realizado ao final do evento.
Funcionalidades:

    CRUD Simples: O projeto apresenta um CRUD básico (criar, ler, atualizar, deletar) para gerenciar os participantes do evento.

    Dashboard: Exibe um painel com informações úteis, como a média de idade dos participantes e outros parâmetros relevantes.

## Instruções de Instalação:

Para executar o projeto localmente, siga as seguintes etapas:

    Clone o repositório:

    bash

git clone https://github.com/seu-usuario/sorteioclientsfeira.git

Instale as dependências listadas no arquivo requirements-dev.txt:

pip install -r requirements-dev.txt

Execute o script generate_secrete_key.py e copie o resultado gerado. Cole o resultado dentro do arquivo gestao_clientes/settings.py, na variável SECRET_KEY.

Execute as migrações para criar o banco de dados:

python manage.py makemigrations
python manage.py migrate

Inicie o servidor local:

    python manage.py runserver

    Acesse o projeto localmente em localhost:8000.

Agora você está pronto para utilizar o Sorteio de Clientes Feira! Divirta-se e bom evento! 🎉🎁
