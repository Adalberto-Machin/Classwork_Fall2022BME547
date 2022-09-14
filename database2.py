def create_patient_entry(patient_name, 
                        patient_id,patient_age):
    new_patient = [patient_name,patient_id,patient_age,[]]
    return new_patient


def main():
    db = []
    db.append(create_patient_entry("Ann Ables",1,30))
    db.append(create_patient_entry("Bob Boyles",2,34))
    db.append(create_patient_entry("Chris Chou",3,25))
    #print(db)
    return db

def print_db(db):
    for j in db:
        print(f'Patient name is {j[0]},and patient id is: {j[1]}, and patient age is: {j[2]}')

def id_match(db,id_number):
    for j in db:
        if j[1]==id_number:
            print(f'The patient is {j[0]}' )
            return j
    return False

def test_match(db,id):
    patient = id_match(db,id)   #always reuse code you already have 
    test_name = input('The test name is:')
    test_value = float(input('The test value is:'))
    patient[3].append((test_name,test_value))

    return db
            

if __name__=="__main__":
    db = main()
    print_db(db)
    x = id_match(db,6)
    print(x)
    db = test_match(db,2)
    print(db)

    room_list = ['Room1','Room 2', 'Room 3']
    
    for i,patient in enumerate(db):
        print(f"Name = {patient[0]}, Room = {room_list[i]}")

    for patient,room in zip(db,room_list):
        print(f"Name = {patient[0]}, Room = {room}")


