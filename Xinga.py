import random
import os
import tweepy                                                          #Biblioteca para acessar a API do twitter.

auth = tweepy.OAuthHandler("SeuConsumerKey","SeuConsumerSecret")       #Codigo de acesso OAuth CONSUMER
auth.set_access_token("TokenChaveDeAcesso","TokenSegredo")             #Codigo Token OAuth KEY
api = tweepy.API(auth) 

complemento = random.choice(open('Adjetivos.txt').read().splitlines()) #Pega uma linha aleatória da lista de Adjetivos 
tuite = "O @jairbolsonaro é um %s"%complemento                         #adiciona o adjetivo na frase
print (tuite) 

api.update_status(tuite)                                               #cria um novo tweet com a frase
