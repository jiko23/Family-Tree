# Family-Tree

This program consists of total three python scripts. These are:

	1) family.py --> This dictionary holds the numerical representaions of the family members
			for the ease of building and functioning of the family. If any new member 
			is added to the family then the numerical representaion of the member will
			be also present in this dictionary.

	2) family_functionality.py -->  Class Family depicts a family tree. Every member in the family will consist of name,relationship with other member/members and gender. This is a acyclic graph
					as to avoid cycles within a family because there cannot be cycles in a family.
					There will be following functions:

						1) check_Cycle --> Will check the adjacent members of a family member to detect cycles.
						2) cycle --> Will check for a member and then call check_Cycle function to also check the adjacent members or relatives for cycles in the family.
						3) search_Mother --> Will check if mother exists in the family or not if not then while adding a child is not possible through the mother.
						4) add_Member --> Will add members in the family tree and establish relationship between given members but cannot add child using this function.
						5) add_Child --> Will add child only through mother and if mother doesnot exists in the family then cannot insert a child.
						6) find_Member --> Will search for adjacent members to a member based on a relationship.


	3) geektrust.py --> This is the main file. It is for the purpose of accepting the input.txt file and the number of new members to be included in the family. In the input.txt the commands
			to be accepted are as follows:
				a) To add a member: ADD_MEMBER Member_1 Member_2 Relation_of_Member_2_with_Member_1 Gender_of_Member_2 . Remember not to try to add child with it i.e. do not mention mother name in 1st
				or else by default it will assume that user is trying to add a child.

				b) To add a child: ADD_CHILD MotherName ChildName Relationship_to_Mother Child_Gender . Mother must exist in the family.

				c) To get relationship: GET_RELATIONSHIP Member Relationship . To get relatives of a member based on a relationship.


Environment Requirement: Kindly Install Anaconda for Python. Python version > 3 or 3.5. Follow this link: https://docs.anaconda.com/anaconda/install/index.html

Running the Program: To run the program kindly run the main program i.e. geektrust.py. Remember that all program scripts, input file must be in the same location or else kindly put location while running
		the program.

			run command on anaconda powershell prompt --> python -m geektrust input.txt number_of_new_member_tobe_added_to_family

			to check the unittest coverage: (a) coverage run -m geektrust input.txt number_of_new_member_tobe_added_to_family

							(b) coverage report -m

			to get the html of the coverage report: coverage html
