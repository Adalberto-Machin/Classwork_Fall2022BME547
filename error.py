def function_name():
    x = 2+3
    c = "a"
    d = c+x
    

def main():
    try :
        function_name()
    except TypeError:
        print('make both of your inputs the same data type')




if __name__ == "__main__":
    main()