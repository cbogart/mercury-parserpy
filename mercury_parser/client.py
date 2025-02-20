import requests
import json


API_ENDPOINT = 'https://mercury.postlight.com/parser?url={}'


class MercuryParser(object):
    def __init__(self, api_key, api_endpoint=API_ENDPOINT):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.headers = {'x-api-key': self.api_key}

    def parse_article(self, article_url):
        """
        Parse article URL
        """
        response = requests.get(self.api_endpoint.format(article_url), headers=self.headers)
        return response

    def parse_multiple_articles(self, *urls):
        """
        Parse a list of urls
        return a dict where the key is the article url
        """
        parsed_articles = {}
        session = requests.Session()
        for url in urls:
            response = session.get(self.api_endpoint.format(url), headers=self.headers)
            parsed_articles[url] = response.json()

        response = json.loads(json.dumps(parsed_articles))
        return response
