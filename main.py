"""
"""

import codecs
from theaters.yesplanet import YesPlanet

def main():
	yp = YesPlanet()
	for theater in yp.theaters():
		print theater
		# with codecs.open("%s.txt", "wb", encoding="utf8") as f:
		# 	for showtime in theater.showtimes():
		# 		f.write(showtime)

if __name__ == "__main__":
	main()