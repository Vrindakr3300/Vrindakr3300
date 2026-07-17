"""
Lightweight background removal:
Uses simple intensity thresholding based on a consensus of background samples.
Guaranteed not to leak because it doesn't use floodfill or segmentation.
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

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = gray.shape

# Apply CLAHE to enhance local facial features and hair texture
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
gray_enhanced = clahe.apply(gray)

# Sample background value at multiple top row points to avoid scanning margins/borders
samples = [
    int(gray_enhanced[15, 15]),                 # Top-left
    int(gray_enhanced[15, w // 4]),             # Top-mid-left
    int(gray_enhanced[15, w // 2]),             # Top-middle
    int(gray_enhanced[15, 3 * w // 4]),         # Top-mid-right
    int(gray_enhanced[15, w - 15])              # Top-right
]
print(f"Background sample points: {samples}")

# Consensus background classification
light_samples = [s for s in samples if s > 120]
dark_samples = [s for s in samples if s <= 120]

if len(light_samples) >= 3:
    is_light_bg = True
    bg_val = np.median(light_samples)
    thresh = max(130, bg_val - 25)
    print(f"Consensus: LIGHT background (val={bg_val:.1f}). Threshold: {thresh}")
    out = np.where(gray_enhanced > thresh, 255, gray_enhanced)
else:
    is_light_bg = False
    bg_val = np.median(dark_samples)
    thresh = min(110, bg_val + 25)
    print(f"Consensus: DARK background (val={bg_val:.1f}). Threshold: {thresh}")
    out = np.where(gray_enhanced < thresh, 255, gray_enhanced)

# Save output
Image.fromarray(out, mode="L").save(OUT)
print(f"Successfully wrote prepped image to {OUT} (consensus threshold mode)")
