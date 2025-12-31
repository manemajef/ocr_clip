import pytesseract
from PIL import ImageGrab
import pyperclip

def main():
    img = ImageGrab.grabclipboard()
    if not img:
        print("no img")
        return
    res = pytesseract.image_to_string(img, "heb+eng")
    pyperclip.copy(res)
    print("done! check your clipboard")

if __name__ == "__main__":
    main()





