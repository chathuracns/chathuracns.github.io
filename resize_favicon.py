from PIL import Image

def make_square(im, min_size=192, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

try:
    img = Image.open("favicon.png")
    # Resize logic:
    # The user image is 275x235.
    # To make it square, we can either crop or pad.
    # Since it's likely a logo, padding (centering) is safer than cropping which might cut off edges.
    # But for a clear favicon, cropping might be better if the logo has whitespace.
    # Let's try to center crop the largest possible square?
    # Actually, padding is safer to preserve content.
    
    # Strategy: Pad to square, then resize to standard sizes if needed.
    # But search engines often like 48px multiples.
    # 275x235 -> pad to 275x275? No, let's just make it square 256x256 or similar.
    # Let's pad to square at current max dimension, then resize to 192x192 (Google recommendation).
    
    max_dim = max(img.size)
    square_img = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
    offset = ((max_dim - img.size[0]) // 2, (max_dim - img.size[1]) // 2)
    square_img.paste(img, offset)
    
    # Save as high-res square
    square_img.save("favicon.png")
    print(f"Resized to {max_dim}x{max_dim}")
    
except Exception as e:
    print(f"Error: {e}")
