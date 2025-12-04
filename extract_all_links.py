import re
from urllib.parse import urljoin

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

base_url = "http://yolo-charters.com/"
css_links = set()
js_links = set()
all_links = set()

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract CSS links
            css_matches = re.findall(r'<link[^>]*href=["\']([^"\']+\.css[^"\']*)["\']', content)
            for link in css_matches:
                full_url = urljoin(base_url, link)
                css_links.add(full_url)
            
            # Extract JS links
            js_matches = re.findall(r'<script[^>]*src=["\']([^"\']+\.js[^"\']*)["\']', content)
            for link in js_matches:
                full_url = urljoin(base_url, link)
                js_links.add(full_url)
            
            # Extract all href links
            href_matches = re.findall(r'href=["\']([^"\']+)["\']', content)
            for link in href_matches:
                if link.startswith('http') or link.startswith('//'):
                    all_links.add(link)
                elif not link.startswith('#') and not link.startswith('mailto:') and not link.startswith('tel:'):
                    all_links.add(urljoin(base_url, link))
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")

print("=" * 80)
print("CSS LINKS")
print("=" * 80)
for link in sorted(css_links):
    print(link)

print("\n" + "=" * 80)
print("JAVASCRIPT LINKS")
print("=" * 80)
for link in sorted(js_links):
    print(link)

print("\n" + "=" * 80)
print("ALL UNIQUE LINKS (first 50)")
print("=" * 80)
for i, link in enumerate(sorted(all_links)[:50]):
    print(link)

# Save to file
with open('all_extracted_links.txt', 'w') as f:
    f.write("CSS LINKS\n")
    f.write("=" * 80 + "\n")
    for link in sorted(css_links):
        f.write(link + "\n")
    
    f.write("\n\nJAVASCRIPT LINKS\n")
    f.write("=" * 80 + "\n")
    for link in sorted(js_links):
        f.write(link + "\n")
    
    f.write("\n\nALL LINKS\n")
    f.write("=" * 80 + "\n")
    for link in sorted(all_links):
        f.write(link + "\n")

print(f"\n\nTotal CSS links: {len(css_links)}")
print(f"Total JS links: {len(js_links)}")
print(f"Total unique links: {len(all_links)}")
print("\nAll links saved to: all_extracted_links.txt")
