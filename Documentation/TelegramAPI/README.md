## **Criando um Bot com Python**

Antes de começarmos, é necessário instalar uma biblioteca que facilitará esse processo. Utilizaremos a biblioteca **`pytelegrambotapi`**, que integra a API do Telegram ao Python, permitindo a criação do nosso bot.

**Instalação da Biblioteca:**

```bash
pip install pytelegrambotapi

```

Após a instalação, podemos começar a criar nosso bot. Utilizaremos o BotFather, um bot do próprio Telegram, para nos auxiliar na configuração do bot.

### **Conversando com o BotFather**

1. Inicie uma conversa com o BotFather no Telegram.
2. Digite **`/newbot`** para criar um novo bot.
3. Escolha um nome para o bot e, em seguida, um nome de usuário que termine com "Bot" (sem espaços).
4. Após a criação, o BotFather fornecerá uma chave API. Guarde essa chave, pois será usada para controlar o bot.

### **Exemplo de Código Python**

Aqui está um exemplo de código Python para o bot, utilizando a biblioteca **`telebot`**:

```python
import telebot

# Insira sua chave API fornecida pelo BotFather
CHAVE_API = "COLOQUE AQUI SUA CHAVE API"
bot = telebot.TeleBot(CHAVE_API)

# Funções que respondem a comandos específicos
@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza pra sua casa: Tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")

# ... (outras funções de comando)

# Função para verificar mensagens e responder com opções
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço pro Lira
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

# Mantém o bot em execução
bot.polling()

```

Este código cria um bot que responde a comandos específicos e oferece opções quando o usuário envia qualquer mensagem. Lembre-se de substituir **`"COLOQUE AQUI SUA CHAVE API"`** pela chave fornecida pelo BotFather.

### **Conclusão**

Com este tutorial, você aprendeu a integrar Python com o Telegram para criar um bot personalizado. Agora você pode personalizar comandos, mensagens e funcionalidades conforme suas necessidades. Consulte a documentação do Telegram Bot API para explorar mais recursos e possibilidades. Aproveite a criação do seu próprio bot e automatize interações no Telegram!
