import database
from collections import Counter

db = database.conecta_banco()
cursor = db.cursor()

sql = "SELECT * FROM bolso_tweets.Tweets where query = \" \";" # adicione qualquer query usada na captura

cursor.execute(sql)

lista = cursor.fetchall()
db.close()


lista_organizada = []
for tweet in lista:
    lista_organizada.append( str(tweet[2])[:-3] )

lista_organizada.sort(reverse=True)

c=Counter(lista_organizada)
for x in c.keys():
    print (str(x) +"\t" + str(c[x]))
