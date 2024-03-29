import telebot
import os
from functionalities.maximum import *
from functionalities.sum_ import *
from functionalities.mean_ import *
from functionalities.comparision import *
from functionalities.time_series import *



# Chave da API que o bot foi criado.
CHAVE_API = "geovanne"

bot = telebot.TeleBot(CHAVE_API)

photo_path = '/PANDAS/imgs/return.png'

def next_action(mensagem):

    texto = f"""
    O que voce deseja fazer agora (Clique no item):
     /opcao1 Prever vendas
     /opcao2 Informações da loja
     /novaLoja Informações sobre uma nova loja
"""
    bot.send_message(mensagem.chat.id, texto)

def send_img(mensagem):

    with open(photo_path, 'rb') as photo_file:
        bot.send_photo(chat_id=mensagem.chat.id, photo=photo_file)

    os.remove(photo_path)
        


# Informações da loja
@bot.message_handler(commands=["maximo"])
def maximo(mensagem):

    bot.send_message(mensagem.chat.id, "Máximo de vendas mês:")
    maxSales(store_id)

    send_img(mensagem)

    bot.send_message(mensagem.chat.id, "Máximo de clientes mês:")
    maxCustomers(store_id)

    send_img(mensagem)
    next_action(mensagem)


@bot.message_handler(commands=["media"])
def media(mensagem):
    bot.send_message(mensagem.chat.id, "Média de vendas mês:")
    meanSales(store_id)

    send_img(mensagem)

    bot.send_message(mensagem.chat.id, "Média de clientes mês:")
    meanCustomers(store_id)

    send_img(mensagem)
    next_action(mensagem)


@bot.message_handler(commands=["total"])
def total(mensagem):
    bot.send_message(mensagem.chat.id, "Total de vendas por mês:")
    sumSales(store_id)

    send_img(mensagem)

    bot.send_message(mensagem.chat.id, "Total de clientes mês:")
    sumCustomers(store_id)

    send_img(mensagem)
    next_action(mensagem)


@bot.message_handler(commands=["comparacao"])
def comparacao(mensagem):
    bot.send_message(mensagem.chat.id, "Comparação de vendas por mês com lojas do mesmo tipo:")
    compareMeanSales(store_id)

    send_img(mensagem)
    next_action(mensagem)



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = f"""
    Previsão de vendas nos próximos 30 dias para a Loja {store_id}
    """
    bot.send_message(mensagem.chat.id, texto)

    total, mean, (max_day, max_sale) = predict_sales(store_id)
    texto = f"""Total de Vendas: US$ {total:.0f}\nMédia de Vendas: US$ {mean:.2f}\nDia de Maior Venda: {max_day}(US$ {max_sale:.0f})"""
    bot.send_message(mensagem.chat.id, texto)

    send_img(mensagem)
    next_action(mensagem)



@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /maximo Max de Vendas e Clientes
    /media Media de Vendas e Clientes
    /total Total de Vendas e Clientes
    /comparacao Comparação da sua loja com outras (Vendas)"""
    bot.send_message(mensagem.chat.id, texto)



def verificar(mensagem):
    return True

@bot.message_handler(commands=["prosseguir"])
def responder(mensagem):
    texto = f"""
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Prever vendas
     /opcao2 Informações de uma loja
"""
    bot.send_message(mensagem.chat.id, texto)


def pass_handler(mensagem):
    password = mensagem.text

    if password == store_id:
        bot.send_message(mensagem.chat.id, f"Senha correta. Clique em /prosseguir")
    else:
        bot.send_message(mensagem.chat.id, f"Senha incorreta. Clique em /iniciar")



def store_handler(mensagem):

    global store_id 

    store_id = mensagem.text

    if int(store_id) > 1115:
        bot.send_message(mensagem.chat.id, f"A loja {store_id} não está em nosso sistema. Clique em /iniciar")

        return 

    sent_msg = bot.send_message(mensagem.chat.id, f"Qual a senha para acessar as informações da loja {store_id}")
    bot.register_next_step_handler(sent_msg, pass_handler) #Next message will call the age_handler function




@bot.message_handler(func=verificar)
def autenticate(mensagem):
    texto = """
        Olá, tudo bem? Digite a loja sobre a qual você deseja se informar
"""
    sent_msg = bot.reply_to(mensagem, texto)
    bot.register_next_step_handler(sent_msg, store_handler) #Next message will call the name_handler function


bot.polling()
