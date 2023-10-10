from rembg import remove

input_path = './images/me.jpeg'
output_path = './images/removedBackgroundme.jpeg'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        # Remove the background using rembg
        print("Removing the background...")
        output = remove(input)

        o.write(output)
        print(f"Image with removed background saved to {output_path}")
