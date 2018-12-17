import requests

from config import ms_api_subscription_key as subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
sentiment_api_url = text_analytics_base_url + "sentiment"


def get_sentimet(text: str, lang: str = 'en') -> float:
    """
    method to hit mircrosoft api to get sentiment of a given text blob from
    english language by default, other languages can be specified
    :param text: string blob in english
    :param lang: language of the given text argument
    :return: returns the confidence of positive sentiment, 1 representing highest
    positive sentiment, while 0 representing lowest. returns -1 if there was an
    error encountered when trying to reach api servers
    """
    document = {"documents": [{'id':1, 'language': lang, 'text': text}]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_api_url, headers=headers, json=document)
    if response.status_code == 200:
        return response.json()['documents'][0]['score']
    return -1


