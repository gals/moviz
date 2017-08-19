"""
"""

import codecs
from theaters.yesplanet import YesPlanet

def main():
	yp = YesPlanet()
	with codecs.open("cinemas.txt", "wb", encoding="utf8") as f:
		for theater in yp.theaters():
			f.write(theater.name + "\n")

if __name__ == "__main__":
	main()