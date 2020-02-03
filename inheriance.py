class One:
  def first(self):
    print("One first")

  def second(self):
    print("One second")

class Two(One):
  def second(self):
    print("Two second")

  def first(self):
    print("Two first")
    self.second()
    super().first()
    super().second()

c = Two()
c.first()