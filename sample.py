from wizardbible2html import compile

m=compile()
m.fromPath("1/1.txt")
m.parse()
with open("1.html","w") as f:
  f.write(m.html)
