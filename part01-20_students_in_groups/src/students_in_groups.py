stud = int(input("How many students on the course? "))
gs = int(input("Desired group size? "))

groups = (stud + gs - 1) // gs

print(f"Number of groups formed: {groups}")