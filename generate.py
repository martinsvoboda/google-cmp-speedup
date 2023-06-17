import base64
import re
from fontTools import subset
from pathlib import Path

from urllib.request import urlopen, Request


SOURCE_CSS_FILE = "./src/cmp.css"

TMP_ICONS_FILE = "./src/icons.tmp.woff2"

DIST_ICONS_FILE = "./dist/icons.dist.woff2"
DIST_CSS_FILE = "./dist/cmp.dist.css"


def file_to_base64(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        base64_data = base64.b64encode(file_data)
        base64_string = base64_data.decode('utf-8')
        return base64_string


def url_to_string(url, headers):
    request = Request(url, headers=headers)

    f = urlopen(request)
    content = f.read().decode('utf-8')
    return content

def url_to_file(url, file):
    f = urlopen(url)
    content = f.read()
    Path(file).write_bytes(content)


# Download CSS file with @font-face definition
# Fake modern browser headers in order to get woff2 font
font_face_css = url_to_string("https://fonts.googleapis.com/icon?family=Material+Icons", headers={'User-Agent': 'Mozilla/5.0 Firefox/90.0'})

# Get font woff2 url
matches = re.search(r"src: url\((https://.*)\) format\('woff2'\)", font_face_css)
if matches == 1:
    raise Exception("Can't find font woff2 URL.")

# Download font file
url_to_file(matches[1], TMP_ICONS_FILE)

# Generate icons subset
# Only following icons: ...
# fonttools subset flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.woff2 --unicodes=5f-7a,30-39,e8a6,e1b1,e5cf,e15b,e5c4,e8fd --no-layout-closure --output-file=icons.woff2 --flavor=woff2
args = [
    TMP_ICONS_FILE,
    "--unicodes=5f-7a,30-39,e8a6,e1b1,e5cf,e15b,e5c4,e8fd",
    "--no-layout-closure",
    f"--output-file={DIST_ICONS_FILE}",
    "--flavor=woff2",
]
subset.main(args)

# Convert icons to base64 and include it to CSS template
icons_base64 = file_to_base64(DIST_ICONS_FILE)

# Load CSS template file and convert it to final dist file
template_css = Path(SOURCE_CSS_FILE).read_text()

# Replace variables
css = template_css.replace("{MATERIAL_ICONS_BASE64}", icons_base64)

# Write final CSS file
Path(DIST_CSS_FILE).write_text(css)

# Remove tmp file
Path(TMP_ICONS_FILE).unlink()
