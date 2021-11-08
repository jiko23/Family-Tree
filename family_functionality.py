from collections import defaultdict
from family import _family_dict


"""
	Class Family depicts a family tree. Every member in the family will consist of name,relationship with other member/members and gender. This is a acyclic graph
	as to avoid cycles within a family because there cannot be cycles in a family.
	There will be following functions:

	1) check_Cycle --> Will check the adjacent members of a family member to detect cycles.
	2) cycle --> Will check for a member and then call check_Cycle function to also check the adjacent members or relatives for cycles in the family.
	3) search_Mother --> Will check if mother exists in the family or not if not then while adding a child is not possible through the mother.
	4) add_Member --> Will add members in the family tree and establish relationship between given members but cannot add child using this function.
	5) add_Child --> Will add child only through mother and if mother doesnot exists in the family then cannot insert a child.
	6) find_Member --> Will search for adjacent members to a member based on a relationship. 
"""

class Family:

	def __init__(self, num_vertex):

		'''
			Here two variables has been decleared
			a) vertices --> represents number of new members adding to family.
			b) family --> the family graph.
		'''
		self.vertices = num_vertex

		self.family = defaultdict(list)


	
	def check_Cycle(self, vertex, visited_stack, stack):

		'''
			This function checks for cycles for a member along with related members to that member.
		'''

		visited_stack[vertex] = True

		stack[vertex] = True

		for member in self.family[vertex]:

			if visited_stack[member[0]] == False:

				if self.check_Cycle(member[0], visited_stack, stack) == True:

					return True
			
			elif stack[member[0]] == True:

				return True
		
		stack[vertex] = False

		return False
		
	

	def cycle(self):

		'''
			This function check for cycle by visiting each member of the family and related relatives to the member.
		'''

		visited = [False] * self.vertices

		stack = [False] * self.vertices

		for v in range(self.vertices):

			if visited[v] == False:

				if self.check_Cycle(v, visited, stack) == True:

					return True

		return False
	


	def search_Mother(self,node):

		'''
			This function check if the mother exists in the family or not.
		'''

		for v in range(self.vertices):

			for member in self.family[v]:

				if member[0] == node and member[1] == 'Wife':

					return True
		
		return False



	def add_Member(self, member_1, member_2, relation, sex):

		'''
			This function will add members to the family with details (member_1, member_2, how member_2 is related to member_1, gender of member1.
			The root of the family is King_Shan as there must be a person to whom the family belongs and started with. One cannot add child using
			this function i.e. cannot pass (mother_name, child_name). If after adding a member if a cycle is formed then it will display message
			and the member to be added will not be allowed to join the family.
			Pass (member_1, member_2, relation of member_2 with member_1, gender of member_2).
		'''

		if self.search_Mother(member_1) == True:

			del _family_dict[member_2]

			return "U are trying to add a child. Kindly use function 'add_Child' for it."
		
		else:

			self.family[member_1].append((member_2,relation,sex))


		if self.cycle() == 1:

			return "Sorry there is a cycle present in the family for which is not allowed...."
		
		else:
			
			return "Member added..."




	def add_Child(self, mother, child, relation, sex):

		'''
			This function will be adding a child to the family. In this family a child can only be added through a mother.
			A child can also be added to the family on the basis of relationship i.e. married/Wife, in that case we assumed
			that the couple was expecting for a child and gave birth to child and the child is being added to the family though
			the mother or also if a couple has addapted a child and wants to add the child to the family through mother.
			Pass (mother_name, child_name, relation of the child with the mother, gender of the child).
		'''

		if self.search_Mother(mother) == True:

			self.family[mother].append((child,relation,sex))
		
		else:

			return "Mother doesnot exist"


		if self.cycle() == 1:

			return "Sorry there is a cycle present in the family for which is not allowed...."
		
		else:
			
			return "child added..."


	
	def find_Member(self, member_name, relation):

		'''
			This function will find adjacent or related family members of member in the family on the basis of a relationship.
			
		'''

		visited = [False] * self.vertices

		a = member_name

		q = []

		q.append(member_name)

		visited[0] = True


		while q:

			member_name = q.pop(0)


			for v in self.family[member_name]:

				if visited[v[0]] == False :

					if v[1] == relation:

						q.append(v[0])

						visited[v[0]] = True

			return q


