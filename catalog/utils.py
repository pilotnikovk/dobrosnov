from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def compress_image(image, max_size_kb=500, quality=85):
    img = Image.open(image)

    if img.mode in ("RGBA", "LA"):
        img = img.convert("RGB")

    width, height = img.size
    max_dimension = 2000

    if width > max_dimension or height > max_dimension:
        if width > height:
            new_width = max_dimension
            new_height = int(height * (max_dimension / width))
        else:
            new_height = max_dimension
            new_width = int(width * (max_dimension / height))
        
        img = img.resize((new_width, new_height), Image.LANCZOS)

    output = BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)

    while output.tell() > max_size_kb * 1024 and quality > 10:
        quality -= 5
        output = BytesIO()
        img.save(output, format='JPEG', quality=quality, optimize=True)

    compressed_image = InMemoryUploadedFile(
        output,
        'ImageField',
        "%s.jpg" % image.name.split('.')[0],
        'image/jpeg',
        sys.getsizeof(output),
        None
    )

    return compressed_image
        