with open(r'C:\Users\student\Downloads\a.tif', 'rb') as file:
    binary_data = file.read()
with open('c.tif', 'wb') as f:
    f.write(binary_data)
    f.close()