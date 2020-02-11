from random import randrange
from PIL import Image

im = Image.open("static/photos/avatars.png")
image_list = []


def avatars_creator():
    # Setting the points for cropped image
    left = 0
    top = 0
    right = 85
    bottom = 95
    i = 0
    j = 100

    # Cropped image of above dimension
    # (It will not change orginal image)
    while i < 110:
        if left < 1000:
            left += 85
            right +=85
        if left > 1000:
            left = 0
            right = 85
            left += 85
            right += 85
            top +=105
            bottom +=105

        image_list.append(im.crop((left, top, right, bottom)))
        crop = im.crop((left, top, right, bottom))
        crop.save(f'static/photos/avatars/avatar{i}.png')
        i+=1
        j+=85
    return image_list


def avatar_pitcher():
    avatars_creator()
    random_number = randrange(120)
    random_avatar = image_list[random_number]

    return random_avatar

