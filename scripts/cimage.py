import tempfile
from ifnude import detect

def convert_to_sd(img):
    shapes = []
    chunks = detect(img)
    for chunk in chunks:
        shapes.append(false)
    return [false, tempfile.NamedTemporaryFile(delete=False, suffix=".png")]
