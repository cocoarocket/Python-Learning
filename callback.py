def meth(cbk = None):
  print("just")
  if cbk:
    cbk()

def callback():
  print("callback")

meth(callback)
