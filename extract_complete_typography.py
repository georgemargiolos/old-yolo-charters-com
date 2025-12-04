import re

with open('style.min.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Function to extract complete typography info for a selector
def extract_typography(selector_pattern, css_content, label):
    # Find the rule
    pattern = f'{selector_pattern}[^{{]*{{([^}}]+)}}'
    matches = re.findall(pattern, css_content, re.IGNORECASE)
    
    results = []
    for match in matches[:3]:  # First 3 matches
        info = {'selector': label}
        
        # Extract font-family
        font_family = re.search(r'font-family:([^;]+)', match)
        if font_family:
            info['font-family'] = font_family.group(1).strip()
        
        # Extract font-size
        font_size = re.search(r'font-size:([^;]+)', match)
        if font_size:
            info['font-size'] = font_size.group(1).strip()
        
        # Extract font-weight
        font_weight = re.search(r'font-weight:([^;]+)', match)
        if font_weight:
            info['font-weight'] = font_weight.group(1).strip()
        
        # Extract color
        color = re.search(r'(?:^|;)color:([^;]+)', match)
        if color:
            info['color'] = color.group(1).strip()
        
        # Extract line-height
        line_height = re.search(r'line-height:([^;]+)', match)
        if line_height:
            info['line-height'] = line_height.group(1).strip()
        
        if len(info) > 1:  # Has more than just selector
            results.append(info)
    
    return results

# Elements to analyze
elements_to_check = [
    ('h1', r'h1(?![a-z])', 'H1'),
    ('h2', r'h2(?![a-z])', 'H2'),
    ('h3', r'h3(?![a-z])', 'H3'),
    ('h4', r'h4(?![a-z])', 'H4'),
    ('h5', r'h5(?![a-z])', 'H5'),
    ('h6', r'h6(?![a-z])', 'H6'),
    ('body', r'body(?![a-z])', 'Body'),
    ('.hero-title', r'\.hero-title(?![a-z-])', 'Hero Title'),
    ('.btn-primary', r'\.btn-primary', 'Primary Button'),
    ('.btn-secondary', r'\.btn-secondary', 'Secondary Button'),
    ('.btn', r'\.btn(?![a-z-])', 'Button (general)'),
    ('.nav-link', r'\.nav-link', 'Navigation Link'),
    ('.card-title', r'\.card-title', 'Card Title'),
    ('.small-search', r'\.small-search', 'Search Box'),
    ('.footer', r'\.footer', 'Footer'),
]

all_results = {}
for key, pattern, label in elements_to_check:
    results = extract_typography(pattern, css, label)
    if results:
        all_results[key] = results

# Create comprehensive report
with open('COMPLETE_TYPOGRAPHY_SPECS.md', 'w', encoding='utf-8') as f:
    f.write("# Complete Typography Specifications - YOLO Charters\n\n")
    f.write("**Generated:** December 4, 2025  \n")
    f.write("**Source:** `dist/css/style.min.css`\n\n")
    f.write("This document shows the exact font, size, weight, and color for each element.\n\n")
    f.write("---\n\n")
    
    f.write("## Font Variables Reference\n\n")
    f.write("```css\n")
    f.write("--font-primary: \"Inter Light\"     /* Weight: 300 */\n")
    f.write("--font-secondary: \"Poppins\"       /* Weight: 400-500 */\n")
    f.write("```\n\n")
    f.write("---\n\n")
    
    # Headings
    f.write("## Headings\n\n")
    for i in range(1, 7):
        key = f'h{i}'
        if key in all_results:
            f.write(f"### H{i}\n\n")
            for idx, info in enumerate(all_results[key], 1):
                if idx > 1:
                    f.write(f"\n**Variant {idx}:**\n\n")
                f.write("```css\n")
                for prop, value in info.items():
                    if prop != 'selector':
                        f.write(f"{prop}: {value};\n")
                f.write("```\n\n")
    
    # Hero Section
    if '.hero-title' in all_results:
        f.write("## Hero Section\n\n")
        f.write("### Hero Title\n\n")
        for idx, info in enumerate(all_results['.hero-title'], 1):
            if idx > 1:
                f.write(f"\n**Variant {idx}:**\n\n")
            f.write("```css\n")
            for prop, value in info.items():
                if prop != 'selector':
                    f.write(f"{prop}: {value};\n")
            f.write("```\n\n")
    
    # Buttons
    f.write("## Buttons\n\n")
    for key in ['.btn', '.btn-primary', '.btn-secondary']:
        if key in all_results:
            title = key.replace('.', '').replace('-', ' ').title()
            f.write(f"### {title}\n\n")
            for idx, info in enumerate(all_results[key], 1):
                if idx > 1:
                    f.write(f"\n**Variant {idx}:**\n\n")
                f.write("```css\n")
                for prop, value in info.items():
                    if prop != 'selector':
                        f.write(f"{prop}: {value};\n")
                f.write("```\n\n")
    
    # Navigation
    if '.nav-link' in all_results:
        f.write("## Navigation\n\n")
        f.write("### Nav Link\n\n")
        for idx, info in enumerate(all_results['.nav-link'], 1):
            if idx > 1:
                f.write(f"\n**Variant {idx}:**\n\n")
            f.write("```css\n")
            for prop, value in info.items():
                if prop != 'selector':
                    f.write(f"{prop}: {value};\n")
            f.write("```\n\n")
    
    # Cards
    if '.card-title' in all_results:
        f.write("## Cards\n\n")
        f.write("### Card Title\n\n")
        for idx, info in enumerate(all_results['.card-title'], 1):
            if idx > 1:
                f.write(f"\n**Variant {idx}:**\n\n")
            f.write("```css\n")
            for prop, value in info.items():
                if prop != 'selector':
                    f.write(f"{prop}: {value};\n")
            f.write("```\n\n")
    
    # Search
    if '.small-search' in all_results:
        f.write("## Search Box\n\n")
        f.write("### Small Search\n\n")
        for idx, info in enumerate(all_results['.small-search'], 1):
            if idx > 1:
                f.write(f"\n**Variant {idx}:**\n\n")
            f.write("```css\n")
            for prop, value in info.items():
                if prop != 'selector':
                    f.write(f"{prop}: {value};\n")
            f.write("```\n\n")
    
    # Body
    if 'body' in all_results:
        f.write("## Body Text\n\n")
        for idx, info in enumerate(all_results['body'], 1):
            if idx > 1:
                f.write(f"\n**Variant {idx}:**\n\n")
            f.write("```css\n")
            for prop, value in info.items():
                if prop != 'selector':
                    f.write(f"{prop}: {value};\n")
            f.write("```\n\n")
    
    # Footer
    if '.footer' in all_results:
        f.write("## Footer\n\n")
        for idx, info in enumerate(all_results['.footer'], 1):
            if idx > 1:
                f.write(f"\n**Variant {idx}:**\n\n")
            f.write("```css\n")
            for prop, value in info.items():
                if prop != 'selector':
                    f.write(f"{prop}: {value};\n")
            f.write("```\n\n")

print("Complete typography specifications saved to: COMPLETE_TYPOGRAPHY_SPECS.md")
print("\nSummary of elements found:")
for key in all_results:
    print(f"  - {key}: {len(all_results[key])} variant(s)")
