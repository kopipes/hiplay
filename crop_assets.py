from PIL import Image

# Crop hIPlay logo more precisely from slide-01 
img1 = Image.open('img/slide-01.jpg')
w1, h1 = img1.size
# Logo "hIPlay" text is approximately at 28%-72% width, 28%-48% height
logo_crop = img1.crop((int(w1*0.28), int(h1*0.28), int(w1*0.72), int(h1*0.56)))
logo_crop.save('img/logo-hiplay.png', 'PNG')
print(f"Saved logo-hiplay.png: {logo_crop.size}")

# Also extract "Indonesia's IP Playground" tagline area
tag_crop = img1.crop((int(w1*0.30), int(h1*0.52), int(w1*0.68), int(h1*0.62)))
tag_crop.save('img/logo-tagline.png', 'PNG')
print(f"Saved logo-tagline.png: {tag_crop.size}")
