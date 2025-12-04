import re

with open('style.min.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Function to find font-family for a selector
def find_font_for_selector(selector_pattern, css_content):
    # Find all rules that match the selector
    pattern = f'{selector_pattern}[^{{]*{{[^}}]*font-family:([^;}}]+)'
    matches = re.findall(pattern, css_content, re.IGNORECASE)
    return [m.strip() for m in matches] if matches else None

# Define what to search for
elements = {
    'h1': r'h1(?![a-z])',
    'h2': r'h2(?![a-z])',
    'h3': r'h3(?![a-z])',
    'h4': r'h4(?![a-z])',
    'h5': r'h5(?![a-z])',
    'h6': r'h6(?![a-z])',
    'body': r'body(?![a-z])',
    'p (paragraph)': r'p(?![a-z])',
    '.hero-title': r'\.hero-title',
    '.hero-title h1': r'\.hero-title\s+h1',
    '.btn-primary': r'\.btn-primary',
    '.btn-secondary': r'\.btn-secondary',
    '.btn': r'\.btn(?![a-z-])',
    '.nav-link': r'\.nav-link',
    '.card': r'\.card(?![a-z-])',
    '.card-title': r'\.card-title',
    '.search': r'\.search',
    '.small-search': r'\.small-search',
    'input': r'input(?![a-z])',
    'button': r'button(?![a-z])',
    '.footer': r'\.footer',
}

results = {}
for element, pattern in elements.items():
    fonts = find_font_for_selector(pattern, css)
    if fonts:
        results[element] = fonts

# Print results
print("=" * 80)
print("FONT USAGE BY ELEMENT")
print("=" * 80)

for element, fonts in sorted(results.items()):
    print(f"\n{element}:")
    for font in fonts[:3]:  # First 3 matches
        print(f"  → {font}")

# Save detailed report
with open('FONT_USAGE_BY_ELEMENT.md', 'w', encoding='utf-8') as f:
    f.write("# Font Usage by Element - YOLO Charters\n\n")
    f.write("**Generated:** December 4, 2025\n\n")
    f.write("This document shows exactly which font is used for each element.\n\n")
    f.write("---\n\n")
    
    f.write("## Typography Elements\n\n")
    
    # Group by category
    headings = {k: v for k, v in results.items() if k.startswith('h') and len(k) == 2}
    buttons = {k: v for k, v in results.items() if 'btn' in k}
    nav = {k: v for k, v in results.items() if 'nav' in k}
    cards = {k: v for k, v in results.items() if 'card' in k}
    hero = {k: v for k, v in results.items() if 'hero' in k}
    search = {k: v for k, v in results.items() if 'search' in k}
    other = {k: v for k, v in results.items() if k not in headings and k not in buttons and k not in nav and k not in cards and k not in hero and k not in search}
    
    if headings:
        f.write("### Headings\n\n")
        for element, fonts in sorted(headings.items()):
            f.write(f"**{element.upper()}**\n")
            for font in fonts[:2]:
                f.write(f"- Font: `{font}`\n")
            f.write("\n")
    
    if hero:
        f.write("### Hero Section\n\n")
        for element, fonts in sorted(hero.items()):
            f.write(f"**{element}**\n")
            for font in fonts[:2]:
                f.write(f"- Font: `{font}`\n")
            f.write("\n")
    
    if buttons:
        f.write("### Buttons\n\n")
        for element, fonts in sorted(buttons.items()):
            f.write(f"**{element}**\n")
            for font in fonts[:2]:
                f.write(f"- Font: `{font}`\n")
            f.write("\n")
    
    if nav:
        f.write("### Navigation\n\n")
        for element, fonts in sorted(nav.items()):
            f.write(f"**{element}**\n")
            for font in fonts[:2]:
                f.write(f"- Font: `{font}`\n")
            f.write("\n")
    
    if cards:
        f.write("### Cards\n\n")
        for element, fonts in sorted(cards.items()):
            f.write(f"**{element}**\n")
            for font in fonts[:2]:
                f.write(f"- Font: `{font}`\n")
            f.write("\n")
    
    if search:
        f.write("### Search Elements\n\n")
        for element, fonts in sorted(search.items()):
            f.write(f"**{element}**\n")
            for font in fonts[:2]:
                f.write(f"- Font: `{font}`\n")
            f.write("\n")
    
    if other:
        f.write("### Other Elements\n\n")
        for element, fonts in sorted(other.items()):
            f.write(f"**{element}**\n")
            for font in fonts[:2]:
                f.write(f"- Font: `{font}`\n")
            f.write("\n")

print("\n\nDetailed report saved to: FONT_USAGE_BY_ELEMENT.md")
