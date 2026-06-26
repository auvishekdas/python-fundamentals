def voter(age):
    if age < 18:
        raise ValueError("Invalid voter")
    return("You are allowed")
try:
    print(voter(25))
    print(voter(15))
except ValueError as error:
    print(error)