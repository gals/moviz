# -*- coding: utf-8 -*-
"""
"""

from theaters import Operator, Theater
from utils.html import parse_html

import requests

class YesPlanetTheater(Theater):
	"""
	"""

	def __init__(self, name, location_id, venue_type_id):
		"""
		"""
		super(YesPlanetTheater, self).__init__(name)
		self.location_id = location_id
		self.venue_type_id = venue_type_id

	def showtimes(self, date=None):
		"""
		"""
		return []

class YesPlanet(Operator):
	"""
	"""

	_theaters = []

	def __init__(self):
		"""
		"""
		super(YesPlanet, self).__init__("YesPlanet")

	def _fetch_theaters(self, http, html_parser):
		"""
		"""
		theaters = []

		response = http.get("http://www.yesplanet.co.il/scheduleInfo")
		html = response.content

		parsed_html = html_parser(html)
		select = parsed_html.select(".scheduleInfoSelect select")[0]
		for option in select.find_all("option"):
			name = option.text
			location_id, venue_type_id = option["value"].split("_")

			theater = YesPlanetTheater(
				name,
				location_id=int(location_id),
				venue_type_id=int(venue_type_id))
			theaters.append(theater)

		return theaters

	def theaters(self, http=requests, html_parser=parse_html):
		"""
		"""
		if not self._theaters:
			self._theaters = self._fetch_theaters(http, html_parser)

		return self._theaters

