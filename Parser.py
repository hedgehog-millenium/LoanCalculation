import requests as r

class Parser:
    @classmethod
    def Parse(cls,url):
        response = r.get(url)
        return response.content
