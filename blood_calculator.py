print('This is the blood_calculator.py module')
print(f"Pythin thinks this is called {__name__}")


def interface():
    print("My Program")
    print("Options:")
    keep_running = True
    while keep_running:
        print("9 - Quit")
        print("1 - Start Program")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            driver()


def inputfunction():
    HDL_input = input('Enter HDL value:')
    LDL_input = input('Enter LDL value:')
    TC_input = input('Enter Total Cholesterol(TC) value:')
    return int(HDL_input), int(LDL_input), int(TC_input)


def check(HDL_number):
    if HDL_number >= 60:
        return "Normal"
    elif HDL_number >= 40 and HDL_number < 60:
        return "Borderline Low"
    else:
        return "Low"


def checkLDL(LDL_number):
    if LDL_number < 130:
        return "Normal"
    elif LDL_number >= 130 and LDL_number < 159:
        return "Borderline High"
    elif 160 <= LDL_number <= 189:
        return 'High'
    else:
        return "Very High"


def check_TC(TC_number):

    if TC_number < 200:
        return 'Normal'
    elif 200 <= TC_number <= 239:
        return 'Borderline High'
    else:
        return 'High'


def driver():
    (HDL_number, LDL_number, TC_number) = inputfunction()
    answerHDL = check(HDL_number)
    answerLDL = checkLDL(LDL_number)
    answerTC = check_TC(TC_number)
    output_result(HDL_number, answerHDL,
                  LDL_number, answerLDL, TC_number, answerTC)


def output_result(HDL_number, answerHDL,
                  LDL_number, answerLDL, TC_number, answerTC):
    print(f"The results for an HDL value of {HDL_number} are {answerHDL}")
    print(f"The results for an LDL value of {LDL_number} are {answerLDL}")
    print(f"The results for an LDL value of {TC_number} are {answerTC}")


if __name__ == "__main__":
    interface()
