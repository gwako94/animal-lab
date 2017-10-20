class Mammalia(object):

	def __init__(self, name, group, limbs):
		self.name = name
		self.group = group

	def can_speak(self):
		if self.group == "primate" and self.name == "man":
			return True
		return False


class Primate(Mammalia):
	def __init__(self, name, group, limbs, behaviour):
		super().__init__(name, group, limbs)
		self.behaviour = behaviour


class Canis(Mammalia):

	def __init__(self,name, group, limbs, behaviour):
		super().__init__(name, group, limbs)
		self.behaviour = behaviour


man = Primate("man", "primate", 2, "Intelligent")
print (man.can_speak())
dog = Canis("dog", "canis", 4, "friendly to man")
print (dog.behaviour)
print (dog.can_speak())