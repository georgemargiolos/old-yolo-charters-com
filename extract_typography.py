import re

with open('style.min.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Extract heading styles (h1-h6)
heading_patterns = {
    'h1': r'h1[,\s{][^}]*\{[^}]+\}',
    'h2': r'h2[,\s{][^}]*\{[^}]+\}',
    'h3': r'h3[,\s{][^}]*\{[^}]+\}',
    'h4': r'h4[,\s{][^}]*\{[^}]+\}',
    'h5': r'h5[,\s{][^}]*\{[^}]+\}',
    'h6': r'h6[,\s{][^}]*\{[^}]+\}',
}

# Extract specific component styles
component_patterns = {
    'hero-title': r'\.hero-title[^{]*\{[^}]+\}',
    'btn-primary': r'\.btn-primary[^{]*\{[^}]+\}',
    'btn-secondary': r'\.btn-secondary[^{]*\{[^}]+\}',
    'nav-link': r'\.nav-link[^{]*\{[^}]+\}',
    'card': r'\.card[^{]*\{[^}]+\}',
}

with open('TYPOGRAPHY_DETAILED.txt', 'w', encoding='utf-8') as f:
    f.write("YOLO CHARTERS - COMPLETE TYPOGRAPHY SPECIFICATIONS\n")
    f.write("=" * 80 + "\n\n")
    
    f.write("HEADING STYLES\n")
    f.write("=" * 80 + "\n\n")
    
    for heading, pattern in heading_patterns.items():
        matches = re.findall(pattern, css_content, re.IGNORECASE)
        if matches:
            f.write(f"\n{heading.upper()}:\n")
            f.write("-" * 40 + "\n")
            for match in matches[:3]:  # First 3 matches
                f.write(match + "\n\n")
    
    f.write("\n\nCOMPONENT STYLES\n")
    f.write("=" * 80 + "\n\n")
    
    for component, pattern in component_patterns.items():
        matches = re.findall(pattern, css_content, re.IGNORECASE)
        if matches:
            f.write(f"\n{component.upper()}:\n")
            f.write("-" * 40 + "\n")
            for match in matches[:5]:  # First 5 matches
                f.write(match + "\n\n")

print("Typography details extracted to: TYPOGRAPHY_DETAILED.txt")

# Also extract and display key info
print("\n" + "=" * 80)
print("KEY TYPOGRAPHY FINDINGS")
print("=" * 80)
print("\nPRIMARY FONTS:")
print("- Inter Light (weight: 300) - Primary body font")
print("- Poppins (weight: 400, 500) - Secondary/heading font")
print("- Inter Medium (weight: 500) - Medium weight variant")
print("\nFONT FILES LOCATION:")
print("- ../../fonts/Poppins-Regular.ttf")
print("- ../../fonts/Poppins-Medium.ttf")
print("- ../../fonts/InterLight.ttf")
print("- ../../fonts/InterMedium.ttf")
