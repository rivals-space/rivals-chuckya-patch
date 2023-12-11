#!/usr/bin/env python3
import cairosvg
import os
from PIL import Image

def convert_svg_to_png(svg_file, output_dir, output_sizes):
    # Ensure the SVG file exists
    if not os.path.exists(svg_file):
        print(f"File {svg_file} not found.")
        return

    # Ensure output directory exists, create if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    for size in output_sizes:
        file_name = f"android-chrome-{size}x{size}.png" if size >= 36 else f"favicon-{size}x{size}.png"
        output_file = os.path.join(output_dir, file_name)
        cairosvg.svg2png(url=svg_file, write_to=output_file, output_width=size, output_height=size)
        print(f"File {output_file} created.")

def create_standard_favicon(svg_file, output_dir):
    # Ensure output directory exists, create if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    favicon_file = os.path.join(output_dir, "favicon.ico")
    cairosvg.svg2png(url=svg_file, write_to=favicon_file, output_width=32, output_height=32)
    # Convert PNG to ICO
    img = Image.open(favicon_file)
    img.save(favicon_file, format='ICO', sizes=[(32, 32)])
    print(f"Favicon.ico created at {favicon_file}")

# List of required sizes for PNG files
png_sizes = [36, 48, 72, 96, 144, 192, 256, 384, 512, 16, 32, 48]

# Output directories
png_output_dir = "../files/app/javascript/icons"
ico_output_dir = "../files/public"

# Convert the SVG to PNG files
convert_svg_to_png("base.svg", png_output_dir, png_sizes)

# Create standard favicon.ico
create_standard_favicon("base.svg", ico_output_dir)
