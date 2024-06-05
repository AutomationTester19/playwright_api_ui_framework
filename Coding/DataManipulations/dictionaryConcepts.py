userInfo = {
    "user_name": "kabira",
    "role": "Senior Software Developer In Test"
}

print(userInfo)

print(userInfo.get("role"))
print(userInfo.get("salary"))  # key is not present in userInfo object

# getting keys
for user in userInfo:
    print(user)

print("#####################")
for keys in userInfo.keys():
    print(keys)


print("#####################")
for value in userInfo.values():
    print(value)


for details in userInfo.items():
    print(details)

print(len(userInfo))


