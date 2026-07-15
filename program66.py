import re

pattern = r"[aeiou]"
if re.match(pattern,"apple"):
    print("Matched")
    
pattern = r"[a-z]"
if re.match(pattern,"apple"):
    print("Matched")
    
pattern = r"[A-Z]"
if re.match(pattern,"Apple"):
    print("Matched")
    
pattern = r"[0-9]"
if re.match(pattern,"2apple"):
    print("Matched")
    
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"Ap5"):
    print("Matched")    