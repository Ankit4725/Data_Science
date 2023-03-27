class Human:
  def __init__(self, name, occupation):
    self.name = name
    self.occupation = occupation
  def do_work(self):
    if self.occupation == "actor":
        print(self.name,"shoot film")
    elif self.occupation == "tennis player":
        print(self.name,"plays tennis") 
  def speak(self):
    print(self.name,"How are you")
p1 = Human("Tom cruise", 'actor')
p1.do_work()
p1.speak()
p2 = Human("Maria","tennis player")
p2.do_work()
p2.speak()
