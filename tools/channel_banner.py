import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
src, out = sys.argv[1], sys.argv[2]
W, H = 2560, 1440
bg = Image.open(src).convert("RGB")
s = max(W / bg.width, H / bg.height)
bg = bg.resize((round(bg.width * s), round(bg.height * s)), Image.LANCZOS)
bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
# soft dark band behind the safe area (1546x423 centered)
band = Image.new("L", (W, H), 0)
ImageDraw.Draw(band).rounded_rectangle((470, 470, W - 470, H - 470), radius=60, fill=150)
band = band.filter(ImageFilter.GaussianBlur(70))
bg = Image.composite(Image.new("RGB", (W, H), (35, 20, 10)), bg, band)
d = ImageDraw.Draw(bg)
B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
def text(y, t, path, size, fill, shadow=6):
    f = ImageFont.truetype(path, size)
    w = d.textlength(t, font=f)
    x = (W - w) / 2
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((x + shadow, y + shadow), t, font=f, fill=(0, 0, 0, 200))
    bg.paste(sh.filter(ImageFilter.GaussianBlur(6)), (0, 0), sh.filter(ImageFilter.GaussianBlur(6)))
    d.text((x, y), t, font=f, fill=fill)
    return w
text(548, "STORIES FROM", B, 74, (240, 200, 120), 4)
text(625, "Grandma's Kitchen", B, 168, (255, 246, 230))
w = 560; d.line(((W - w) / 2, 830, (W + w) / 2, 830), fill=(240, 200, 120), width=3)
text(852, "Family stories told around the kitchen table  ·  New story every week", I, 46, (255, 240, 215), 3)
bg.save(out, optimize=True)
