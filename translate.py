import requests

class Translator:
    def __init__(self, source_language, target_language):
        self.source_language = source_language
        self.target_language = target_language
        self.api_url = 'https://libretranslate.com/translate'

    def translate(self, text):
        try:
            response = requests.post(
                self.api_url,
                data={
                    'q': text,
                    'source': self.source_language,
                    'target': self.target_language,
                    'format': 'text'
                }
            )
            response.raise_for_status()
            return response.json()['translatedText']
        except requests.exceptions.RequestException as e:
            print(f'Error occurred: {e}')  
            return None