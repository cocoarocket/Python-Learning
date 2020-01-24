class Counter():
  count = 5
  
  def reset(self):
    self.count = 6

  def __call__(self):
    print(self.count)
    self.count += 1

a = Counter()
a()
a()
a.reset()
a()
a()
