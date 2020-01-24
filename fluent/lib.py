class Filter:
  def __init__(self, inst):
    self.inst = inst

  def filter(self, arg):
    print("filter %s" % arg)
    return self.inst

class FluentPrototype:
  run_open = False
  query_open = True

  def proto_query(self, arg, inst):
    if self.query_open:
      print("query %s" % arg)
      self.query_open = False
      self.run_open = True
      return Filter(inst)
    else:
      print("query already")
  
  def proto_run(self):
    if self.run_open:
      print("run")
    else:
      print("run not posible, because Query not builded")