import requests
import json
 

recipients = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/am937")
print(recipients.status_code)
print(recipients.text)
recipents_dict = json.loads(recipients.text)

blood_type = {}
for iter in recipents_dict.keys():
    blood_type_get= requests.get(f"http://vcm-7631.vm.duke.edu:5002/get_blood_type/{recipents_dict[iter]}")
    print(blood_type_get.status_code)
    print(blood_type_get.text)
    blood_type[f"{iter}" +" blood type"] = blood_type_get.text

print(blood_type)
print("A- cannot donate to B+")

out_data = {"Name": 'am937',
            "Match": 'No'}
r_add_patient = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",json=out_data)
print(r_add_patient.status_code)
print(r_add_patient.text)