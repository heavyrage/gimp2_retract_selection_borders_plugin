#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import os

def retract_borders(image, drawable):
    rebord = 5 # 5% retraction
    width = drawable.width
    height = drawable.height
    new_width = int(width * (100-rebord)/100)
    new_height = int(height * (100-rebord)/100)
    offx = 0 - int((width - new_width) / 2)
    offy = 0 - int((height - new_height) / 2)
    pdb.gimp_layer_resize(drawable, new_width, new_height, offx, offy)
    pdb.gimp_displays_flush()
    pdb.gimp_image_flatten(image)

    # overwrite file
    filename = image.filename
    base_name, ext = os.path.splitext(filename)
    ext = ext.lower() 
    drawable = image.active_layer

    if ext == ".png":
        pdb.file_png_save(image, drawable, filename, filename, 0, 9, 1, 1, 1, 1, 1)
    elif ext in [".jpg", ".jpeg"]:
        pdb.file_jpeg_save(image, drawable, filename, filename, 0.95, 0, 1, 0, "", 0, 1, 0, 0)
    elif ext == ".webp":
        pdb.file_webp_save(image, drawable, filename, filename, 0, 1, 100, 100, True, True, False, 0, False, False, False, 500, 500)

register(
    "retract_borders",
    "Retract borders",        # Short description
    "Retract borders of highest layer",  # Detailled help
    "Heavyrage", "Heavyrage", "2025",    # Author, Copyright, Date
    "Retract borders and overwrite image",    # Text
    "*",                             # Supported types (* = all)
    [
        (PF_IMAGE, 'image', 'Image', None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
    ],
    [],
    retract_borders,                      # callback
    menu='<Image>/Select/'
)

main()
