import os
import time
import datetime

while 1==1:                                         #loop
	horagora = time.localtime()                 #pega a hora/data etc...
	if horagora.tm_hour == 5:                   #Verifica se a hora atual é igual a 5
		print ("opa ta mandando")           
		os.system('python3 Xinga.py')       #Chama o programa pra postar o tweet
		while horagora.tm_hour == 5:        #Espera passar de 5h
			horagora = time.localtime() #confere a hora novamente pra saber se passou
			time.sleep(1200)            #aguarda um tempinho pra nao sobrecarregar CPU
	else:
		time.sleep(1200) 

