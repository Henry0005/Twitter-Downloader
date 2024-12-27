# Twitter Videos Downloader

Este projeto permite que você baixe vídeos de posts do Twitter (X). O script utiliza a biblioteca yt-dlp para realizar o download e organiza os arquivos em uma pasta única baseada na data e hora do download.

## Funcionalidade

- Baixa vídeos de posts do Twitter (X) usando a URL fornecida.
- Cria um diretório único para cada download, baseado na data e hora atual, para evitar sobreposição de arquivos.
- Em caso de erro, remove a pasta criada durante o processo de download.

## Requisitos

Este projeto requer as seguintes dependências para funcionar corretamente:

-  `yt-dlp`: Para baixar o conteúdo do Twitter.
- Você pode instalar todas as dependências utilizando o arquivo `requirements.txt`.

## Como Usar

1. Clone ou baixe o repositório para o seu computador.
2. Abra o terminal no diretório onde o projeto foi salvo.
3. Instale as dependências utilizando o arquivo `requirements.txt`.

````
pip install -r requirements.txt
````

4. Execute o script e forneça o link do tweet com o vídeo para realizar o download.

5. O script irá baixar o vídeo e salvá-lo em uma pasta com o nome baseado na data e hora do download.

## Possíveis Erros

- Se o tweet não for encontrado ou ocorrer algum erro na requisição, o script exibirá uma mensagem de erro e removerá a pasta criada durante o processo.

- Certifique-se de que o link fornecido seja válido e esteja acessível.

## Tecnologias Utilizadas

### **Python**

Descrição: Linguagem de programação de alto nível, amplamente utilizada para scripts e automação, bem como para desenvolvimento de aplicações web e análise de dados.

### **yt-dlp**

Descrição: Biblioteca Python utilizada para baixar vídeos de várias plataformas, incluindo o Twitter (X). No meu projeto, ela é usada para baixar vídeos de tweets a partir da URL fornecida pelo usuário.

Link: [yt-dlp no GitHub](https://github.com/yt-dlp/yt-dlp)

### **os**

Descrição: Módulo integrado do Python que fornece funções para interagir com o sistema operacional, como manipulação de arquivos e diretórios.

Link: [os no Python Docs](https://docs.python.org/3/library/os.html)

### **shutil**

Descrição: Módulo integrado do Python que fornece funções para manipulação de arquivos e operações de cópia, movimentação e remoção de arquivos.

Link: [shutil no Python Docs](https://docs.python.org/3/library/shutil.html)

### **datetime**

Descrição: Módulo integrado do Python que oferece classes para manipulação de datas e horas.

Link: [datetime no Python Docs](https://docs.python.org/3/library/datetime.html)
