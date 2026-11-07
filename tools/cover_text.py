"""Add the title text to a cover image generated in Google Flow (no text in the image itself).
usage: cover_text.py BASE.png OUT.png "LINE ONE|LINE TWO" [--side left|right] [--color yellow|white]
Produces a 1280x720 JPEG/PNG with a soft dark gradient behind the text for readability."""
import sys, argparse, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = [ROOT / "assets/fonts/Anton-Regular.ttf", pathlib.Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")]
COLORS = {"yellow": (255, 214, 0), "white": (255, 255, 255)}

ap = argparse.ArgumentParser()
ap.add_argument("base"); ap.add_argument("out"); ap.add_argument("text")
ap.add_argument("--side", default="left", choices=["left", "right"])
ap.add_argument("--color", default="yellow", choices=list(COLORS))
a = ap.parse_args()

W, H = 1280, 720
img = Image.open(a.base).convert("RGB")
scale = max(W / img.width, H / img.height)
img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
left, top = (img.width - W) // 2, (img.height - H) // 2
img = img.crop((left, top, left + W, top + H))

# dark gradient on the text side
grad = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(grad)
for x in range(W // 2):
    alpha = int(170 * (1 - x / (W / 2)) ** 1.5)
    xx = x if a.side == "left" else W - 1 - x
    gd.line([(xx, 0), (xx, H)], fill=alpha)
img = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, grad.filter(ImageFilter.GaussianBlur(20)))

font_path = next(str(f) for f in FONTS if f.exists())
lines = [l.strip().upper() for l in a.text.split("|") if l.strip()]
d = ImageDraw.Draw(img)
max_w = int(W * 0.46)
size = 150
while size > 40:
    font = ImageFont.truetype(font_path, size)
    if all(d.textlength(l, font=font) <= max_w for l in lines) and size * 1.08 * len(lines) <= H * 0.6:
        break
    size -= 4
line_h = int(size * 1.08)
y = (H - line_h * len(lines)) // 2
for l in lines:
    tw = d.textlength(l, font=font)
    x = 50 if a.side == "left" else W - 50 - tw
    d.text((x, y), l, font=font, fill=COLORS[a.color], stroke_width=max(4, size // 14), stroke_fill=(0, 0, 0))
    y += line_h
img.save(a.out, quality=92)
print("cover saved", a.out)
