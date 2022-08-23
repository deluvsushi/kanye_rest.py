from requests import get


class KanyeRest:
	def __init__(self):
		self.api = "https://api.kanye.rest"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_random_quote(self):
		return get(
			self.api, headers=self.headers).json()

	def get_random_quote_as_text(self):
		return get(
			f"{self.api}/text",
			headers=self.headers).text

	def get_all_quotes(self):
		return get(
			"https://raw.githubusercontent.com/ajzbc/kanye.rest/master/quotes.json",
			headers=self.headers).json()
