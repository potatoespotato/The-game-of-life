from PIL import Image

SIZE = (500, 500)  # размер gif
WHITE = (255, 255, 255)  # фон каждого кадра gif


def prepare(img):  # resize to 300x300 and remove opacity
    bg = Image.new("RGB", SIZE, WHITE)
    img = img.resize(SIZE, Image.ANTIALIAS)
    bg.paste(img)
    return bg.convert('P', palette=Image.ADAPTIVE, dither=None)
s = int(input('how mach img?'))
images = list(map(prepare, map(Image.open, ('{}.png'.format(x) for x in range(s)))))
gif = Image.new('RGB', SIZE, WHITE)
gif.save('game_of_life.gif', 'GIF', save_all=True, append_images=images)
print('done')