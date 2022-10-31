
arrive_alice = "10-01"
depart_alice = "10-31"

arrive_bob = "10-25"
depart_bob = "11-31"


arrive_array_alice = arrive_alice.split("-")
depart_array_alice = depart_alice.split("-")
x = int(arrive_array_alice[1])
y = int(depart_array_alice[1])

a = int(arrive_array_alice[0])
b = int(depart_array_alice[0])

result_array = []
arrive_array_bob= arrive_bob.split("-")
depart_array_bob = depart_bob.split("-")
m = int(arrive_array_bob[1])
n = int(depart_array_bob[1])
c = int(arrive_array_bob[0])
d = int(depart_array_bob[0])

days_array_alice = []
for day in range(x, y + 1):
    days_array_alice.append(day)
print(days_array_alice)

days_array_bob= []
for day in range(m, n + 1):
    days_array_bob.append(day)
print(days_array_bob)

if c == a:
    result_array = set(days_array_alice).intersection(set(days_array_bob))
    print(len(list(set(result_array))))
else:
    print(0)



