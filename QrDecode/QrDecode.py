from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode("utf-8") if decoded_objects else None

if __name__ == "__main__":
    image_path = input("Enter the path to the QR code image: ")
    decoded_text = decode_qr_code(image_path)
    if decoded_text:
        print("Decoded QR code:", decoded_text)
    else:
        print("Computer says no")
