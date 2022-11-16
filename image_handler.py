from tkinter import filedialog
import base64
import requests


def upload_image():
    filename = get_image_filename()
    b64_string = convert_file_to_b64(filename)
    result = upload_b64_to_server(b64_string, "am99", 50)
    #print(result)
    result2 = get_image_from_server("am99", 50)
    print(result2)
    new_filename = get_image_filename()
    convert_base64_to_image(result2[0], new_filename)



def get_image_filename():
    filename = filedialog.askopenfilename()
    return filename


def convert_file_to_b64(filename):
    # Input:
    #    filename: string variable containing the path and name of the image file 
    #                on computer

    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')

    # Output:
    # b64_string: string variable containing the image bytes encoded as a base64 
    # string
    return b64_string


def upload_b64_to_server(b64_string, id, number):
    #uploads base64 string to server
    out_data = {"image": b64_string, "net_id": id, "id_no": number}
    r = requests.post(" http://vcm-21170.vm.duke.edu/add_image", json=out_data)
    return r.text, r.status_code

def get_image_from_server(id, number):
    r = requests.get(f"http://vcm-21170.vm.duke.edu/get_image/{id}/{number}")
    return r.text, r.status_code


def convert_base64_to_image(image_64, new_filename):
    # Input:
    #    b64_string: string variable containing the image bytes encoded as a base64
    #                  string
    b64_string = image_64
    image_bytes = base64.b64decode(b64_string)
    with open(new_filename, "wb") as out_file:
        out_file.write(image_bytes)

    # Output:
    #    an image file on the local computer with the path and name contained in
    #      the new_filename variable
    return image_bytes

if __name__ == "__main__":
    upload_image()
