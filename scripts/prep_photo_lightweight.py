"""
Lightweight background removal fallback:
Uses OpenCV thresholding and morphological operations to mask out a dark background,
avoiding the need for the heavy rembg model.
"""
import os
import sys
import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

print(f"Reading {INP}...")
img = cv2.imread(INP)
if img is None:
    print(f"Error: Could not read image {INP}")
    sys.exit(1)

# Convert to grayscale to find dark background
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold: background is very dark (value < 35)
# Anything brighter than 35 is considered subject (foreground)
_, mask = cv2.threshold(gray, 35, 255, cv2.THRESH_BINARY)

# Morphological operations to clean up the mask
# Close small holes inside the subject (e.g., dark eyes/hair highlights)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# Open to remove small noise in the background
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Apply a soft blur to feather the edges of the mask
mask_blur = cv2.GaussianBlur(mask.astype(np.float32) / 255.0, (0, 0), 3.0)

# Apply local contrast enhancement (CLAHE) to the subject
clahe = cv2.createCLAHE(clipLimit=2.6, tileGridSize=(8, 8))
gray_enhanced = clahe.apply(gray)
gray_enhanced = cv2.convertScaleAbs(gray_enhanced, alpha=1.05, beta=18)

# Composite onto a white background (255) using the mask
out = gray_enhanced.astype(np.float32) * mask_blur + 255.0 * (1.0 - mask_blur)
out = np.clip(out, 0, 255).astype(np.uint8)

# Save output
Image.fromarray(out, mode="L").save(OUT)
print(f"Successfully wrote prepped image to {OUT} (lightweight mode)")
