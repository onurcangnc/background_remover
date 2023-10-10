from rembg import remove

input_path = './images/me.jpeg'
output_path = './images/removedBackgroundme.jpeg'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
