import pymysql
import re


def conecta_banco():
    db = pymysql.connect("", "", "", "")
    return db

def insere_um(tweet, term):
    db = conecta_banco()
    cursor = db.cursor()

    line = re.sub('"', '', tweet.full_text)
    line = re.sub("'", "", line)
    sql = "INSERT INTO `acompanhamento`.`Tweets` (`idTweets`, `plain text`, `timestamp_tw`, `handle`, `retweets`, `favs`, `query`) VALUES (" \
          ""+tweet.id_str+", \""+ line +"\",\""+str(tweet.created_at)+"\" , \""+tweet.user.screen_name+"\", "+str(tweet.retweet_count)+", "+str(tweet.favorite_count)+", \""+term+"\");"
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except Exception as e:
        print (e)
        db.close()
        return -1
