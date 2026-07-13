import re
pattern = r"Ger"
text1 = "Ger is a language."
text2 = re.sub(pattern,"German",text1)
print(text2)
