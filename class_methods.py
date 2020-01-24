class Fluent:
  @classmethod
  def first(cls):
    print("first")

  @staticmethod
  def second():
    print("second")

  @staticmethod
  def third():
    print("third")

Fluent.first()
Fluent.second()