import re
import json

# Read all pasted content files
files = [
    'pasted_content.txt',
    'pasted_content_2.txt',
    'pasted_content_3.txt',
    'pasted_content_4.txt',
    'pasted_content_5.txt',
    'pasted_content_6.txt',
    'pasted_content_7.txt',
    'pasted_content_8.txt'
]

css_files = set()
js_files = set()
fonts = set()
libraries = {}

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract CSS files
            css_matches = re.findall(r'<link[^>]*href=["\']([^"\']*\.css[^"\']*)["\']', content)
            css_files.update(css_matches)
            
            # Extract JS files
            js_matches = re.findall(r'<script[^>]*src=["\']([^"\']*\.js[^"\']*)["\']', content)
            js_files.update(js_matches)
            
            # Extract font references
            font_matches = re.findall(r'font-family:\s*["\']?([^;"\']+)["\']?', content)
            fonts.update(font_matches)
            
            # Look for Google Fonts
            google_fonts = re.findall(r'fonts\.googleapis\.com/css\?family=([^"\'&]+)', content)
            fonts.update(google_fonts)
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# Output results
print("=== CSS FILES ===")
for css in sorted(css_files):
    print(css)

print("\n=== JAVASCRIPT FILES ===")
for js in sorted(js_files):
    print(js)

print("\n=== FONTS ===")
for font in sorted(fonts):
    print(font)
