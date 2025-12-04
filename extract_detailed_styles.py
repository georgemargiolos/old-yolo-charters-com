import re
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

# Storage for extracted data
colors = set()
fonts = set()
inline_styles = []
css_classes = set()
component_styles = defaultdict(list)

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract inline style attributes
            style_matches = re.findall(r'style=["\']([^"\']+)["\']', content)
            inline_styles.extend(style_matches)
            
            # Extract class names
            class_matches = re.findall(r'class=["\']([^"\']+)["\']', content)
            for classes in class_matches:
                css_classes.update(classes.split())
            
            # Extract color values (hex, rgb, rgba)
            hex_colors = re.findall(r'#[0-9A-Fa-f]{3,6}', content)
            colors.update(hex_colors)
            
            rgb_colors = re.findall(r'rgba?\([^)]+\)', content)
            colors.update(rgb_colors)
            
            # Extract font-family declarations
            font_families = re.findall(r'font-family:\s*([^;}"\']+)', content)
            fonts.update([f.strip() for f in font_families])
            
            # Extract specific component styles
            # Hero section
            hero_matches = re.findall(r'<div class="hero[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)
            if hero_matches:
                component_styles['hero'].extend(hero_matches[:1])
            
            # Search form
            search_matches = re.findall(r'<form[^>]*search[^>]*>(.*?)</form>', content, re.DOTALL | re.IGNORECASE)
            if search_matches:
                component_styles['search_form'].extend(search_matches[:1])
            
            # Headers (h1-h6)
            for i in range(1, 7):
                h_matches = re.findall(f'<h{i}[^>]*>(.*?)</h{i}>', content, re.DOTALL)
                if h_matches:
                    component_styles[f'h{i}'].extend(h_matches[:3])
            
            # Buttons
            button_matches = re.findall(r'<button[^>]*class="([^"]*)"[^>]*>', content)
            component_styles['button_classes'].extend(button_matches[:10])
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# Write results
with open('detailed_styles_extraction.txt', 'w', encoding='utf-8') as f:
    f.write("=== COLORS DETECTED ===\n")
    for color in sorted(colors):
        f.write(f"{color}\n")
    
    f.write("\n=== FONTS DETECTED ===\n")
    for font in sorted(fonts):
        f.write(f"{font}\n")
    
    f.write("\n=== TOP CSS CLASSES (first 100) ===\n")
    for cls in sorted(list(css_classes))[:100]:
        f.write(f"{cls}\n")
    
    f.write("\n=== INLINE STYLES (first 20) ===\n")
    for style in inline_styles[:20]:
        f.write(f"{style}\n\n")
    
    f.write("\n=== BUTTON CLASSES ===\n")
    for btn_class in set(component_styles['button_classes']):
        f.write(f"{btn_class}\n")

print("Detailed extraction complete. Results saved to detailed_styles_extraction.txt")
