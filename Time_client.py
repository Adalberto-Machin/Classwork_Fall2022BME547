import requests

time = requests.get("http://127.0.0.1:5000/time")
print(time.status_code)
print("Time:")
print(time.text)

date = requests.get("http://127.0.0.1:5000/date")
print(date.status_code)
print("Date:")
print(date.text)

input_age = {'date': "11/20/1998", 'units': "years"}
age_diff = requests.post("http://127.0.0.1:5000/age", json = input_age)
print(age_diff.status_code)
print("Age:")
print(f"{age_diff.text} years")
