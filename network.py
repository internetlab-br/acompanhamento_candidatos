import database
import re
import csv
from collections import Counter

db = database.conecta_banco()
cursor = db.cursor()

sql = "SELECT * FROM bolso_tweets.Tweets where query = \" \";" # adicione qualquer query usada na captura

cursor.execute(sql)

lista = cursor.fetchall()
db.close()

with open('retweets.csv', 'w', newline="\n") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["source", "target", "start", "end"])

    for tweet in lista:
        result = re.search('RT @(.*?):', tweet[1])
        if result:
            spamwriter.writerow([tweet[3], result.group(1), tweet[2], tweet[2]])
