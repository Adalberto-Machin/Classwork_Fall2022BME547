import requests 

r = requests.get("https://api.github.com/repos/Adalberto-Machin/Classwork_Fall2022BME547/branches")
print(r)
print(type(r))
print(r.text)
answer = r.json()
print(type(answer))
for branch in answer:
        print(branch["name"])