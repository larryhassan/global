friends = ["rat", "sol", "joe", "tit", "git", "qua", "yoo"]
print(friends[-3:-1])

doubled_number = [number * 2 for number in range(10)]
print(doubled_number)

friend_ages = [25, 31, 30, 28, 26, 33]
age_str = [f"My friend is {age} years old." for age in friend_ages]
print(age_str)

friend = input("Enter your friend name: ")
names = ["rol", "bob", "Jen", "Joel", "Erica"]
friend_lower = [name.lower() for name in friend]

if friend.lower() in friend_lower:
  print(f"{friend} is one of your friends.")
