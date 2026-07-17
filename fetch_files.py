import os
import urllib.request
import json
import ssl

# Disable SSL verification for simple downloads if needed
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

REPO = "AVIVASHISHTA29/AVIVASHISHTA29"
BRANCH = "main"
BASE_URL = f"https://api.github.com/repos/{REPO}/git/trees/{BRANCH}?recursive=1"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"

def download_file(url, dest_path):
    print(f"Downloading {url} to {dest_path}...")
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx) as response, open(dest_path, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def main():
    dest_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Fetch tree
    req = urllib.request.Request(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            tree_data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to fetch tree: {e}")
        # Fallback to direct well-known files
        files_to_download = [
            "README.md",
            "scripts/prep_photo.py",
            "scripts/make_ascii_svg.py",
            "scripts/make_info_card.py",
        ]
        for f in files_to_download:
            download_file(RAW_BASE_URL + f, os.path.join(dest_dir, f))
        return

    for item in tree_data.get('tree', []):
        if item['type'] == 'blob':
            path = item['path']
            # Skip binary image files that are large unless needed, but let's download everything except raw image assets to be lightweight, or download them too if they are small
            if path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')) and 'source' in path:
                # We can download them too or skip them
                pass
            download_file(RAW_BASE_URL + path, os.path.join(dest_dir, path))

if __name__ == '__main__':
    main()
