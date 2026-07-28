import os
from PIL import Image, ImageDraw, ImageFont

def draw_relay_png(size, no_margin=False):
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw squircle
    margin = 0 if no_margin else int(size * 0.05)
    r = int(size * 0.2)
    draw.rounded_rectangle([margin, margin, size - margin, size - margin], radius=r, fill="#F1F5F9", outline="#E2E8F0", width=max(1, int(size*0.01)))
    
    # Draw a stylized 'R' in Indigo
    font_size = int(size * 0.6)
    try:
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except:
        font = ImageFont.load_default()
        
    text = "R"
    # Approximate centering
    text_x = size // 2 - font_size // 3
    text_y = size // 2 - font_size // 2
    draw.text((text_x, text_y), text, fill="#6366F1", font=font)
    
    return img

def main():
    sizes = [1024, 512, 256, 128, 64, 48, 32, 24, 16]
    os.makedirs("app-icon", exist_ok=True)
    os.makedirs("logo", exist_ok=True)
    
    for size in sizes:
        img = draw_relay_png(size)
        img.save(f"app-icon/relay-icon-{size}.png")
        
    draw_relay_png(256, False).save("logo/logo_256.png")
    draw_relay_png(256, True).save("logo/logo_256_no_margin.png")
    draw_relay_png(1024, False).save("app-icon/icon_round512@2x.png")
    
    img256 = draw_relay_png(256)
    img256.save("app-icon/icon256.ico", format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])

if __name__ == "__main__":
    main()
