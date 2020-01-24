from fluent.lib import *

class Fluent(FluentPrototype):
  def query(self, arg):
    return self.proto_query(arg, self)

  def run(self):
    self.proto_run()

Fluent().run()
Fluent().query("SELECT").filter("cool").query("2")