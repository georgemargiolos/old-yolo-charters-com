import re
import json
from collections import defaultdict

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

resources = {
    'css_files': set(),
    'js_files': set(),
    'fonts': set(),
    'cdn_resources': set(),
    'libraries': defaultdict(dict),
    'page_titles': []
}

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract page title
            title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
            if title_match:
                resources['page_titles'].append(title_match.group(1).strip())
            
            # Extract CSS files
            css_matches = re.findall(r'<link[^>]*href=["\']([^"\']*\.css[^"\']*)["\'][^>]*>', content)
            resources['css_files'].update(css_matches)
            
            # Extract JS files
            js_matches = re.findall(r'<script[^>]*src=["\']([^"\']*\.js[^"\']*)["\'][^>]*>', content)
            resources['js_files'].update(js_matches)
            
            # Extract CDN resources
            cdn_patterns = [
                r'https?://cdn\.jsdelivr\.net/[^"\']+',
                r'https?://cdnjs\.cloudflare\.com/[^"\']+',
                r'https?://fonts\.googleapis\.com/[^"\']+',
                r'https?://fonts\.gstatic\.com/[^"\']+',
                r'https?://www\.google\.com/recaptcha/[^"\']+',
            ]
            for pattern in cdn_patterns:
                matches = re.findall(pattern, content)
                resources['cdn_resources'].update(matches)
            
            # Identify specific libraries
            if 'jquery' in content.lower():
                resources['libraries']['jQuery']['detected'] = True
            if 'litepicker' in content.lower():
                resources['libraries']['Litepicker']['detected'] = True
            if 'select2' in content.lower():
                resources['libraries']['Select2']['detected'] = True
            if 'photo-swipe' in content.lower() or 'photoswipe' in content.lower():
                resources['libraries']['PhotoSwipe']['detected'] = True
            if 'magnific-popup' in content.lower():
                resources['libraries']['Magnific Popup']['detected'] = True
            if 'jquery-ui' in content.lower():
                resources['libraries']['jQuery UI']['detected'] = True
            if 'bootpag' in content.lower():
                resources['libraries']['jQuery Bootpag']['detected'] = True
            if 'recaptcha' in content.lower():
                resources['libraries']['Google reCAPTCHA']['detected'] = True
                
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# Save to JSON
with open('resources_analysis.json', 'w') as f:
    json.dump({
        'css_files': sorted(list(resources['css_files'])),
        'js_files': sorted(list(resources['js_files'])),
        'cdn_resources': sorted(list(resources['cdn_resources'])),
        'libraries': dict(resources['libraries']),
        'page_titles': resources['page_titles']
    }, f, indent=2)

print("Analysis complete. Results saved to resources_analysis.json")
