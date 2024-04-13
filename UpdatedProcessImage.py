
#!/usr/bin/env python3

from PIL import Image
import os

def is_image(filepath):
  try:
    with Image.open(filepath) as img:
      img.verify()
    return True
  except (IOError, SyntaxError):
    return False

def process_images(directory):
  for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    if os.path.isfile(filepath):
      if is_image(filepath):
        with Image.open(filepath) as img:
          rotated_img = img.rotate(-90, expand=True)
          resized_img = rotated_img.resize((128, 128))

          outfile = os.path.splitext(filename)[0]
          outdir = os.path.join(directory, 'opt', 'icons')
          if not os.path.exists(outdir):
            os.makedirs(outdir)
          outpath = os.path.join(outdir, outfile)
          resized_img.convert("RGB").save(outpath, format="JPEG")

directory_path = os.getcwd()

process_images(directory_path)