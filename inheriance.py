class One:
  def first(self):
    print("first")

class Two(One):
  def second(self):
    print("second")

c = Two()
c.first()