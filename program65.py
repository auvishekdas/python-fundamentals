import re

pattern = r"Hab.b"
if re.match(pattern,"Habib"):
    print("matched")
    
pattern = r"^Hab.b$"
if re.match(pattern,"Habib"):
    print("matched")
    
pattern = r"Z*"
if re.match(pattern,"Habib"):
    print("matched")
    
pattern = r"(Hb)*"
if re.match(pattern,"Habib"):
    print("matched")
    
pattern = r"H*a"
if re.match(pattern,"Habib"):
    print("matched")    
    
pattern = r"H+a"
if re.match(pattern,"Habib"):
    print("matched")
    
pattern = r"Habib(-)?Zaman"
if re.match(pattern,"Habib-Zaman"):
    print("matched")
    
pattern = r"Z{1,4}$"
if re.match(pattern,"ZZ"):
    print("matched")    
    