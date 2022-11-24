import telebot

CHAVE_API = "5970660691:AAGxGt90_sw8Jk3vLmCRJh6fa6lBU_eEX2A"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["hatch"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "O Carro Hatch é um modelo de carro mais econômico e compacto, que garante"
                                       "as famílias um melhor custo de benefício, principalmente para quem não ter"
                                       "dor de cabeças com gastos exorbitantes.")

    bot.send_message(mensagem.chat.id, "O carro já se encontra a disposição do seu uso "
                                       "Obrigado!!")


@bot.message_handler(commands=["sedan"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "O carro sedan é aquele que possui uma carroceria dividida em três volumes:"
                                       " área do motor, espaço destinado ao motorista e aos passageiros e porta-malas."
                                       " É um modelo comprido, com espaço interno amplo e bagageiro mais volumoso")

    bot.send_message(mensagem.chat.id, "O carro já se encontra a disposição do seu uso "
                                       "Obrigado!!")


@bot.message_handler(commands=["suv"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Infelizmente ")
    bot.send_message(mensagem.chat.id, "Não temos este modelo disponíveis,")
    bot.send_message(mensagem.chat.id, "clique aqui para iniciar: /iniciar")



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
       Escolhe o seu modelo? (Clique em uma opção)
       /hatch Hatch
       /sedan Sedan
       /suv Suv"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@agencarro.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! AgenCarro mandou um abraço de volta")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Ola! Eu sou o "Sidney", assistente Virtual de atendimento da Locadora AgenCarro
    
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Fazer um pedido
     /opcao2 Reclamar de um pedido
     /opcao3 Mandar um abraço pro AgenCarro
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()