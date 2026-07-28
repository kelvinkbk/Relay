import os
import sys

def rasterize():
    sizes = [1024, 512, 256, 128, 64, 48, 32, 24, 16]
    app_icon_svg = "app-icon/relay-icon.svg"
    logo_svg = "logo/relay-symbol.svg"
    logo_no_margin_svg = "logo/relay-symbol-mono.svg"
    
    if not os.path.exists(app_icon_svg):
        print(f"Error: {app_icon_svg} not found.")
        return

    try:
        import cairosvg
    except ImportError:
        print("Please pip install cairosvg")
        return
    except OSError as e:
        print(f"Cairo error: {e}")
        return

    print("Generating PNGs using cairosvg...")
    try:
        for size in sizes:
            out_png = f"app-icon/relay-icon-{size}.png"
            cairosvg.svg2png(url=app_icon_svg, write_to=out_png, output_width=size, output_height=size)
            print(f"Created: {out_png}")
            
        # Extra required assets
        cairosvg.svg2png(url=logo_svg, write_to="logo/logo_256.png", output_width=256, output_height=256)
        cairosvg.svg2png(url=logo_no_margin_svg, write_to="logo/logo_256_no_margin.png", output_width=256, output_height=256)
        cairosvg.svg2png(url=app_icon_svg, write_to="app-icon/icon_round512@2x.png", output_width=1024, output_height=1024)
        print("Special PNGs created.")
        
        # Create ICO
        try:
            from PIL import Image
            img = Image.open("app-icon/relay-icon-256.png")
            img.save("app-icon/icon256.ico", format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
            print("Created ICO.")
        except Exception as e:
            print("Pillow ICO generation failed:", e)
            
    except Exception as e:
        print(f"Rasterization failed: {e}")

if __name__ == "__main__":
    rasterize()
