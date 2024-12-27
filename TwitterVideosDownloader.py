import os
import shutil
import time
from datetime import datetime
import yt_dlp

# Define o diretório de trabalho como o local onde o script está sendo executado
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cores para mensagens no terminal
RED = "\033[31m"  # Cor vermelha para erros
RESET = "\033[0m"  # Resetando a cor do terminal

# Função para baixar o conteúdo do Twitter
def download_twitter_video(url):
    # Obtém a data e hora atual para nomear a pasta
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    download_folder = os.path.join(os.getcwd(), current_time)

    # Cria o diretório para salvar o conteúdo
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Configurações do yt-dlp para o download
    ydl_opts = {
        'format': 'best',  # Baixar o conteúdo com a melhor qualidade disponível
        'outtmpl': os.path.join(download_folder, '%(id)s.%(ext)s'),  # Nome do arquivo de saída
        'quiet': True,  # Suprime os logs detalhados
        'logtostderr': False,  # Impede que os logs apareçam no terminal
    }

    try:
        # Cria uma instância do yt-dlp e baixa o conteúdo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Download concluído com sucesso!")
        print(f"O conteúdo foi salvo em: {download_folder}")

    except yt_dlp.utils.DownloadError as e:
        # Mensagem de erro em vermelho se ocorrer algum erro durante o download
        print(f"{RED}Erro ao tentar baixar o vídeo: {e}{RESET}")
        # Se ocorrer erro, remove a pasta criada
        if os.path.exists(download_folder):
            shutil.rmtree(download_folder)

    except Exception as e:
        # Captura qualquer outro erro e exibe a mensagem
        print(f"{RED}Erro geral: {e}{RESET}")
        # Se ocorrer erro, remove a pasta criada
        if os.path.exists(download_folder):
            shutil.rmtree(download_folder)

# Solicita ao usuário a URL do tweet
tweet_url = input("Digite o link do tweet com o vídeo: ")

# Pausa para evitar solicitações muito rápidas
time.sleep(2)

# Chama a função para baixar o conteúdo
download_twitter_video(tweet_url)
