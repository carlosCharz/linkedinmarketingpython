import sys
import os

def main():
	filepath = 'people.in'

	if not os.path.isfile(filepath):
		print("File path {} does not exist. Exiting...".format(filepath))
		sys.exit()

	people = []

	# 1 READ FILE
	with open(filepath) as fp:
		line = fp.readline()
		while line:
			#print("{}".format(line.strip())) # just for testing purposes
			process_line(line.strip(), people)
			line = fp.readline()

	# 2 SORT ITEMS
	people.sort(key=lambda person: person.score, reverse = True)

	# 3 BUILD OUTPUT
	for person in people[:10]:
		print("Id: {} Name: {} Score: {}".format(person.person_id, person.name, person.score)) # just for testing purposes
	output = open('people.out','w')
	for person in people[:10]:
		output.write(person.person_id + '\n')
	output.close()


def process_line(line, people):
	words = line.strip().split('|')
	# just for testing purposes
	#for word in words:
	#	print("word: {}".format(word.strip()))
	person = Person(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7])
	people.append(person)

class Person:
	person_id = ''
	name = ''
	last_name = ''
	current_role = ''
	country = ''
	industry = ''
	recommendations_qty = 0
	connections_qty = 0
	score = 0.0

	def __init__(self, person_id, name, last_name, current_role, country, industry, recommendations_qty, connections_qty):
		self.person_id = person_id.strip()
		self.name = name.strip()
		self.last_name = last_name.strip()
		self.current_role = current_role.strip()
		self.country = country.strip()
		self.industry = industry.strip()
		self.recommendations_qty = int(recommendations_qty.strip() or 0)
		self.connections_qty = int(connections_qty.strip() or 0)
		self.score = ((self.recommendations_qty - 5) / 2.0 * 7.0 + (self.connections_qty - 300) / 50.0 * 3.0) / 10.0

if __name__ == '__main__':
	main()