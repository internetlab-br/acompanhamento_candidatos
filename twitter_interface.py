import tweepy, database

def autentica():
    auth = tweepy.OAuthHandler('', '')
    auth.set_access_token('','')

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                 retry_errors=set([503]))
    return api

def lista_busca(term):

    api = autentica()
    print("  - " + term)
    for tweet in tweepy.Cursor(api.search, q=term, count=100, show_user=True, tweet_mode='extended').items():
        if (database.insere_um(tweet, term) == -1):
            print("end of " + term)
            break
