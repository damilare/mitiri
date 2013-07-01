import requests
from BeautifulSoup import BeautifulSoup, Tag

from crawler import Base

class Nairaland(Base):
	BASE_ENDPOINT = 'http://www.nairaland.com'

	def _fetch(self, url):
		resp = requests.get(url)
		if resp.status_code == 200:
			return resp.content

	def _parse_link(self, link):
		""" extract url from link returns a pair """
		if isinstance(link, Tag) and link.name == 'a':
			return (link.get('href', None), getattr(link, 'text', None))

	def _parse_content(self, content):
		""" extract urls from page """
		soup = BeautifulSoup(content)
		links = [tag for tag in soup.find("td", {"class": "featured w"}) \
										if getattr(tag, 'name', None) == 'a']

		return links

	def _save_source(self):
		pass

	def update_feed(self):
		content = self._fetch(self.BASE_ENDPOINT)
		links = self._parse_content(content)
		return links
		