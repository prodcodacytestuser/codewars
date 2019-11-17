#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES

import allure
import unittest
from utils.log_func import print_log
from kyu_5.alphabet_wars_nuclear_strike.alphabet_war import alphabet_war


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Alphabet wars - nuclear strike')
class AlphabetWarTestCase(unittest.TestCase):
	"""
	Testing alphabet_war function
	"""
	def test_alphabet_war(self):
		"""
		Testing alphabet_war function

		Introduction
		There is a war and nobody knows - the alphabet war!
		The letters hide in their nuclear shelters. The
		nuclear strikes hit the battlefield and killed a
		lot of them.

		Task
		Write a function that accepts battlefield string
		and returns letters that survived the nuclear strike.

		1. The battlefield string consists of only small letters, #,[ and ].

		2. The nuclear shelter is represented by square brackets [].
		The letters inside the square brackets represent letters
		inside the shelter.

		3. The # means a place where nuclear strike hit the battlefield.
		If there is at least one # on the battlefield, all letters outside
		of shelter die. When there is no any # on the battlefield, all letters
		survive (but do not expect such scenario too often ;-P ).

		4. The shelters have some durability. When 2 or more # hit close to
		the shelter, the shelter is destroyed and all letters inside evaporate.
		The 'close to the shelter' means on the ground between the shelter and
		the next shelter (or beginning/end of battlefield). The below samples
		make it clear for you.
		:return:
		"""

		allure.dynamic.title("Testing alphabet_war function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Enter test string and verify the output"):

			data = [
				('[a]#[b]#[c]', 'ac'),
				('[a]#b#[c][d]', 'd'),
				('[a][b][c]', 'abc'),
				('##a[a]b[c]#', 'c'),
				('abde[fgh]ijk', 'abdefghijk'),
				('ab#de[fgh]ijk', 'fgh'),
				('ab#de[fgh]ij#k', ''),
				('##abde[fgh]ijk', ''),
				('##abde[fgh]', ''),
				('##abcde[fgh]', ''),
				('abcde[fgh]', 'abcdefgh'),
				('##abde[fgh]ijk[mn]op', 'mn'),
				('#abde[fgh]i#jk[mn]op', 'mn'),
				('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#', 'abijk'),
			]

			for battlefield, expected in data:

				print_log(battlefield=battlefield,
				          expected=expected)

				self.assertEqual(expected,
				                 alphabet_war(battlefield))
