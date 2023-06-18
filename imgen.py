#from runtime import img_url
#import os
import io
import requests
from PIL import Image
#import tempfile

img_url = 'https://tm.ibxk.com.br/2023/06/15/15090304237019.jpg?ims=1120x420'
filename1 = 'Posts Automation/Design Templates/teste01.png'


filepath = f'{img_url}.jpg'


def get_img(img_url):
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        background = Image.open(io.BytesIO(r.content))
        
        # Do something with image

        #RESIZING
        baseheight = 1080
        wpercent = (baseheight/float(background.size[1]))
        basesize = int((float(background.size[0])*float(wpercent)))
        background = background.resize((basesize,baseheight), Image.Resampling.LANCZOS) 
        
        width, height = background.size
        left = (width - 1080)/2
        top = (height - 1080)/2
        right = (width + 1080)/2
        bottom = (height + 1080)/2
        background = background.crop((left, top, right, bottom))

        frontImage = Image.open(filename1)
        
        
        
        
        datas = frontImage.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:  # finding white colour by its RGB value
                # storing a transparent value when we find a white colour
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)  # other colours remain unchanged

        frontImage.putdata(newData)

        # Convert imag to RGBA
        background = background.convert("RGBA")
        # Calculate width to be at the center
        width = (background.width - frontImage.width) // 2
        # Calculate height to be at the center
        height = (background.height - frontImage.height) // 2
        # Paste the frontImage at (width, height)
        background.paste(frontImage, (width, height), frontImage)
        # Save this image
        background.save("new.png", format="png")
        #background.save(filepath)



# download image with PIL and requests
""" buffer = tempfile.SpooledTemporaryFile(max_size=1e9)
r = requests.get(img_url, stream=True)
if r.status_code == 200:
    downloaded = 0
    filesize = int(r.headers['content-length'])
    for chunk in r.iter_content(chunk_size=1024):
        downloaded += len(chunk)
        buffer.write(chunk)
        print(downloaded/filesize)
    buffer.seek(0)
    i = Image.open(io.BytesIO(buffer.read()))
    i.save(os.path.join(out_dir, 'image.jpg'), quality=85)
buffer.close()
frontImage = Image.open(img_data) """


get_img(img_url)