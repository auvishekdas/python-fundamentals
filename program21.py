subjects = [2,4,6,8,10]
print(len(subjects))

subjects = ["Python","Practice","Learning"]
subjects.append("Programming")
print(subjects)

subjects = ["Bangladesh","India","Germany"]
subjects.insert(1,"China")
print(subjects)

subjects = ["English","German","Hindi","Bangla"]
subjects.remove("Hindi")
print(subjects)

subjects = [5,4,1,3,2]
subjects.sort()
print(subjects)

subjects = [25,42,10,8]
subjects.reverse()
print(subjects)

subjects = [800,255,325,991]
subjects.pop()
print(subjects)

subjects = [25,42,85,95]
subjects.clear()
print(subjects)

subjects = [18,900,47]
subject2 = subjects.copy()
print(subject2)

subjects = [98,92,100,96]
pos = subjects.index(92)
print(pos)

subjects = [14,18,18,25]
pos = subjects.count(18)
print(pos)