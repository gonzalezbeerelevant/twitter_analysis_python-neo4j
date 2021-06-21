import re

class TwitterProcessing:

    def __init__(self):
        pass

    def getRTScreenName(self, tweet_text):
        """
            Objetivo: Extrai RT @ScreenName do tweet.
            Parâmetros: Informar o texto (str) do Tweet 
        """
 
        p = re.compile(r'RT @([^\s:]+)')
        response = p.findall(tweet_text)
        
        if len(response): 
            return str(response[0])
        return ''