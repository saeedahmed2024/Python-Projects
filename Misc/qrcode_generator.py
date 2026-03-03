import qrcode

def qrcode_generator_short():
    url_text = input("Enter text or url: ").strip() #removes white spaces
    file_name = input("Enter file name: ").strip()

    img = qrcode.make(url_text)
    img.save(file_name)

    print(f"QRCode saved as {file_name}")

    return

def qrcode_generator_long():
    url_text = input("Enter text or url: ").strip()
    file_name = input("Enter file name: ").strip()

    qr = qrcode.QRCode(box_size=10, border = 4)
    qr.add_data(url_text)

    image = qr.make_image(fill_color = 'black', back_color = 'white')
    image.save(file_name)

    print(f"QRCode saved as {file_name}")
    return

#qrcode_generator_short()
qrcode_generator_long()
