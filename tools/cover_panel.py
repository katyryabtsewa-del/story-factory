"""Competitor-style cover: dark text panel on the left (white text, yellow highlights, ends with '...'), face on the right.
usage: cover_panel.py BASE.png OUT.png "plain text [[highlighted text]] more text..." [--flip]
Use --flip when the person in the base image is on the left. Output 1280x720."""
import re, sys, argparse, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONTS = ["/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
W, H = 1280, 720
YELLOW, WHITE = (255, 212, 0), (255, 255, 255)

ap = argparse.ArgumentParser()
ap.add_argument("base"); ap.add_argument("out"); ap.add_argument("text")
ap.add_argument("--flip", action="store_true")
a = ap.parse_args()

img = Image.open(a.base).convert("RGB")
if a.flip:
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
scale = max(W / img.width, H / img.height)
img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
l, t = (img.width - W) // 2, (img.height - H) // 2
img = img.crop((l, t, l + W, t + H))
# shift the picture to the right so the face sits right of the panel
canvas = Image.new("RGB", (W, H), (0, 0, 0))
canvas.paste(img.resize((int(W * 0.62), int(H * 0.62 * 1.0))) if False else img, (int(W * 0.0), 0))
img = canvas

# dark panel: solid up to 50% of the width, smooth fade to 64%
mask = Image.new("L", (W, H), 0); md = ImageDraw.Draw(mask)
for x in range(W):
    p = x / W
    alpha = 255 if p < 0.50 else max(0, int(255 * (1 - (p - 0.50) / 0.14)))
    md.line([(x, 0), (x, H)], fill=alpha)
img = Image.composite(Image.new("RGB", (W, H), (8, 8, 8)), img, mask)

# tokens with colours
words = []
for i, part in enumerate(re.split(r"\[\[|\]\]", a.text)):
    for w in part.split():
        words.append((w.upper(), YELLOW if i % 2 else WHITE))

d = ImageDraw.Draw(img)
BOX_L, BOX_R, BOX_T, BOX_B = 36, int(W * 0.52), 28, H - 28
font_path = next(f for f in FONTS if pathlib.Path(f).exists())

def layout(size):
    font = ImageFont.truetype(font_path, size)
    space = d.textlength(" ", font=font)
    lines, cur, cur_w = [], [], 0
    for w, c in words:
        ww = d.textlength(w, font=font)
        if cur and cur_w + space + ww > BOX_R - BOX_L:
            lines.append((cur, cur_w)); cur, cur_w = [], 0
        cur_w += (space if cur else 0) + ww; cur.append((w, c, ww))
    lines.append((cur, cur_w))
    return font, space, lines

size = 80
while size > 22:
    font, space, lines = layout(size)
    if len(lines) * size * 1.18 <= BOX_B - BOX_T:
        break
    size -= 1
lh = size * 1.18
y = BOX_T + (BOX_B - BOX_T - lh * len(lines)) / 2
for cur, cur_w in lines:
    x = BOX_L + (BOX_R - BOX_L - cur_w) / 2      # centred like the competitors
    for w, c, ww in cur:
        d.text((x, y), w, font=font, fill=c, stroke_width=max(1, size // 22), stroke_fill=(0, 0, 0))
        x += ww + space
    y += lh
img.save(a.out)
print("cover saved", a.out, "font", size, "lines", len(lines))
