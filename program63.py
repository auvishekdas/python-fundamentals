import re
pattern = r"language"
text = "English is an international language"
result = re.search(pattern,text)
if result:
    print(result.start())
    print(result.end())
    print(result.span())
else:
    print("Unavailable")
    

pattern = r"German"
text = "English is an international language"
result = re.search(pattern,text)
if result:
    print(result.start())
    print(result.end())
    print(result.span())
else:
    print("Unavailable")    