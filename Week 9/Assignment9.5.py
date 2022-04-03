inp = input("Please Enter File Name:")
fhand = open(inp)
domain_names = dict()

for line in fhand:
    words = line.split()

    if len(words) < 3 or words[0] != 'From'  : continue

    indv_email = words[1]
    'print(indv_email)'

    domains = indv_email.split('@')
    'print(domains)'

    if domains[1] not in domain_names:
        domain_names[domains[1]] = 1
    else:
        domain_names[domains[1]] += 1

print(domain_names)
