d={"set":"put or bring into a specified state.", "loop":"dekhna", "seat":"baithna",
   "hima":{"m":"noyhing", "a":"rice"}}
print(d)
print(d["hima"])
d.update({"dipsikha":"love"})
d["hima"]="food"
print(d)
#d.pop("set")
#print(d.items())
#print(d.get("hima"))
print(d.popitem())
print(d)
del d["loop"]
print(d)
