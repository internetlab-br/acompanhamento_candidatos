import time
import twitter
import database
from multiprocessing import Pool

db = database.conecta_banco()
api = twitter.autentica()

queries = [] # adicione aqui as tags a serem acompanhadas pelo código

while True:
    with Pool(7) as p:
        p.map(twitter.lista_busca, queries)
    print ("recomeçando a busca em 5 minutos... ") #captura novos resultados depois de 5 minutos de intervalo
    time.sleep(300)
