import sys
from family_functionality import *
from family import _family_dict
import unittest


input_file = sys.argv[1]
number_of_new_vertices = sys.argv[2]


class TestFamily(unittest.TestCase):


	def setUp(self):

		self.file = input_file

		self.num_new_vertices = number_of_new_vertices



	def test_Add_Member_Success(self):


		with open(self.file) as f:


			family = Family(len(_family_dict)+ int(self.num_new_vertices))


			for line in f:


				_input = line.split()


				if len(_input) == 0:

					break


				if _input[0] == 'ADD_MEMBER':

					'''
						To add member we search if the numerical representation of the member exists or not
						and if it exists then add the members and establish relation. In this it is must that
						the 1st member is present already in the family.
					'''

					_keys = [k for k,v in _family_dict.items() if v == _input[1]]

					_keys_1 = [k for k,v in _family_dict.items() if v == _input[2]]


					if len(_keys) > 0:

						if len(_keys_1) == 0:

							_family_dict[len(_family_dict)] = _input[2]

						_keys_1 = [k for k,v in _family_dict.items() if v == _input[2]]



						try:
							self.assertIn(family.add_Member(_keys[0], _keys_1[0], _input[3], _input[4]), ["U are trying to add a child. Kindly use function 'add_Child' for it.","Sorry there is a cycle present in the family for which is not allowed...."])


						except:

							self.assertEqual(family.add_Member(_keys[0], _keys_1[0], _input[3], _input[4]), "Member added...")




	def test_ADD_CHILD_Success(self):


		with open(self.file) as f:


			family = Family(len(_family_dict)+ int(self.num_new_vertices))


			for line in f:


				_input = line.split()


				if len(_input) == 0:

					break



				if _input[0] == 'ADD_CHILD':

					'''
						To add child we search if the numerical representation of the mother exists or not
						and if it exists then add the child and establish relation. In this it is must that
						the mother is present already in the family.
					'''

					_keys = [k for k,v in _family_dict.items() if v == _input[1]]

					_keys_1 = [k for k,v in _family_dict.items() if v == _input[2]]


					if len(_keys) > 0:

						if len(_keys_1) == 0:

							_family_dict[len(_family_dict)] = _input[2]


						_keys_1 = [k for k,v in _family_dict.items() if v == _input[2]]

						#print(family.search_Mother(_keys[0]))

						try:

							self.assertEqual(family.add_Child(_keys[0], _keys_1[0], _input[3], _input[4]), "child added...")


						except:

							self.assertIn(family.add_Child(_keys[0], _keys_1[0], _input[3], _input[4]), ["Mother doesnot exist", "Sorry there is a cycle present in the family for which is not allowed...."])




	def test_Find_Member(self):


		with open(self.file) as f:


			family = Family(len(_family_dict)+ int(self.num_new_vertices))


			for line in f:


				_input = line.split()


				if len(_input) == 0:

					break



				if _input[0] == 'GET_RELATIONSHIP':

					_keys = [k for k,v in _family_dict.items() if v == _input[1]]


					try:
						self.assertRaises(IndexError, family.find_Member, _keys[0], _input[2])

					except:
						pass




if __name__ == '__main__':

	unittest.main(argv=['first-arg-is-ignored'], exit=False)
	