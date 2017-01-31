class country(object):
	def __init__(self, name, population):
		self.name = name
		self.population = population
		self.regions = {}
	
	

class region(object):
	def __init__(self, name , population):
		self.name = name
		self.population = population
		self.cities = {}

class city(object):
	def __init__(self, name, population):
		self.name = name
		self.population = population
		self.companies = {}
		
class business(object):
	def __init__(self, name):
		self.name = name

atlas = business("Atlas")
unitedstates = country("United States", 0)
utah = region("Utah", 0)
layton = city("Layton", 0)
world = {"United States" : country("United States", 0)}
world["United States"].regions = {"Utah" : region("Utah", 0)}
world["United States"].regions["Utah"].cities = {"Layton" : city("Layton", 100)}
world["United States"].regions["Utah"].cities["Layton"].companies = {"Atlas" : atlas}

print atlas.name
print layton.population
for x in world["United States"].regions["Utah"].cities["Layton"].companies.iterkeys():
	print x
print world["United States"].name
print world["United States"].regions["Utah"].name
		
print world["United States"].regions["Utah"].population