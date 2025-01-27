import barcode

def logic(name, b):
    ean = barcode.get('code128', name)
    file = ean.save(f'{b}.png', options={"write_text": False})
    return file

