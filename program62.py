import re
pattern = r"language"
if re.match(pattern,"German is a language"):
    print("Match")
else:
    print("Not matched")
    
import re
pattern = r"German"
if re.match(pattern,"German is a language"):
    print("Match")
else:
    print("Not matched")
    
import re
pattern = r"German"
if re.search(pattern,"English is a language"):
    print("Match")
else:
    print("Not matched")
    
import re
pattern = r"German"
if re.match(pattern,"German is a language"):
    print("Match")
else:
    print("Not matched")    
    
import re
pattern = r"Black"
print(re.findall(pattern,"Black is my favorite color"))
