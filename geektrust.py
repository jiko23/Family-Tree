import sys
from family_functionality import *
from family import _family_dict


if __name__ == "__main__":


	input_file = sys.argv[1] #the file name

	number_of_new_vertices = sys.argv[2] #number of new members to be added to the family.
	
	

	with open(input_file) as f:

		obj = Family(len(_family_dict)+ int(number_of_new_vertices)) ####the number of family members to be is recent number of members + new members

		for i in f:

			_query = i.split()


			if len(_query) == 0:

				break


			if _query[0] == 'ADD_MEMBER':

				'''
					To add member we search if the numerical representation of the member exists or not
					and if it exists then add the members and establish relation. In this it is must that
					the 1st member is present already in the family.
				'''

				_keys = [k for k,v in _family_dict.items() if v == _query[1]]

				_keys_1 = [k for k,v in _family_dict.items() if v == _query[2]]

				if len(_keys) > 0:

					if len(_keys_1) == 0:

						_family_dict[len(_family_dict)] = _query[2]

					_keys_1 = [k for k,v in _family_dict.items() if v == _query[2]]

					print(obj.add_Member(_keys[0], _keys_1[0], _query[3], _query[4]))

					

			elif _query[0] == 'ADD_CHILD':

				'''
					To add child we search if the numerical representation of the mother exists or not
					and if it exists then add the child and establish relation. In this it is must that
					the mother is present already in the family.
				'''

				_keys = [k for k,v in _family_dict.items() if v == _query[1]]

				_keys_1 = [k for k,v in _family_dict.items() if v == _query[2]]


				if len(_keys) > 0:

					if len(_keys_1) == 0:

						_family_dict[len(_family_dict)] = _query[2]


					_keys_1 = [k for k,v in _family_dict.items() if v == _query[2]]

					#print(obj.search_Mother(_keys[0]))

					print(obj.add_Child(_keys[0], _keys_1[0], _query[3], _query[4]))




			elif _query[0] == 'GET_RELATIONSHIP':

				'''
					Here we find relatives of a member based on a relationship with the
					member. 
				'''

				_keys = [k for k,v in _family_dict.items() if v == _query[1]]


				try:

					member = obj.find_Member(_keys[0], _query[2])

					output = [_family_dict[i] for i in member]

					print(*output, sep=' ')


				except:

					print("No such person...")
