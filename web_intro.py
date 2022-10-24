from regex import R
import requests 

# r = requests.get("https://api.github.com/repos/Adalberto-Machin/Classwork_Fall2022BME547/branches")
# print(r)
# print(type(r))
# print(r.text)
# if r.status_code == 200:
#         answer = r.json()
#         print(type(answer))
#         for branch in answer:
#                 print(branch["name"])
# else:
#         print(f"Bad request {r.text} ")

# output_info = {"name": "Adalberto Machin",
#                         "net_id": "am937",
#                         "e-mail": "adalberto.machin@duke.edu"}
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                   json = output_info)
# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)

# send message to partner code 

output_info = {"user":"machoman", "message": "Pray that we finish this BME 547 HW on time"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                   json = output_info)

#t = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/machoman")
#print(t.text)