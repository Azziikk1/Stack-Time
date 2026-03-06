from PIL import Image
img = Image.open('icon_512_final.png')
import os
sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}
for folder, size in sizes.items():
    path = f'android/app/src/main/res/{folder}'
    os.makedirs(path, exist_ok=True)
    img.resize((size, size), Image.LANCZOS).save(f'{path}/ic_launcher.png')
    img.resize((size, size), Image.LANCZOS).save(f'{path}/ic_launcher_round.png')
print('Icons created successfully')
