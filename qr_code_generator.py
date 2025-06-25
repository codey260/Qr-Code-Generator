# Import QRCode from pyqrcode
import pyqrcode

def main():
    # Prompt user for input
    text = input("Type in URL or text to encode: ").strip()
    if not text:
        print("Input cannot be empty. Exiting.")
        return

    # Prompt for output filename
    filename = input("Enter output filename (default: MyQrcode.png): ").strip()
    if not filename:
        filename = "MyQrcode.png"
    if not filename.lower().endswith(".png"):
        filename += ".png"

    try:
        # Generate QR code
        qrcode = pyqrcode.create(text)
        qrcode.png(filename, scale=8)
        print(f"QR code saved as '{filename}' successfully.")
    except Exception as e:
        print(f"Error generating QR code: {e}")

    input("Press Enter to exit: ")

if __name__ == "__main__":
    main()