from PIL import Image
from PIL.ExifTags import TAGS
import wget
import os

print("Example URL1: http://courseres.org/duck.jpg")
print("Example URL2: https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg")
print("Example URL3: https://upload.wikimedia.org/wikipedia/commons/5/54/Panda_Cub_(4274178112).jpg")
url = input("What URL?:")

filename = wget.download(url)

#xwget http://courseres.org/duck.jpg

# path to the image or video
imagename = filename

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
    question = input("Do you want to see all tags?: y/n ")
    if question == "y":
        print(TAGS)
        quit()
        os.remove(imagename)
    else:
        quit()
        os.remove(filename)
