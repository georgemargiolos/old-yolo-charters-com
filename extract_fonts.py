import re

with open('style.min.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Extract @font-face declarations
font_faces = re.findall(r'@font-face\{[^}]+\}', css_content)

# Extract CSS variables for fonts
root_vars = re.findall(r':root\{[^}]+\}', css_content)

# Extract all font-family declarations with context
font_families = re.findall(r'([^{]+)\{[^}]*font-family:([^;}]+)', css_content)

print("=" * 80)
print("@FONT-FACE DECLARATIONS")
print("=" * 80)
for i, font_face in enumerate(font_faces, 1):
    print(f"\n{i}. {font_face}\n")

print("\n" + "=" * 80)
print("CSS ROOT VARIABLES")
print("=" * 80)
for root_var in root_vars:
    # Extract font-related variables
    font_vars = re.findall(r'(--[^:]+:[^;]+)', root_var)
    for var in font_vars:
        if 'font' in var.lower():
            print(var)

print("\n" + "=" * 80)
print("UNIQUE FONT FAMILIES USED")
print("=" * 80)
unique_fonts = set()
for selector, font in font_families[:50]:  # First 50 to avoid too much output
    font_clean = font.strip()
    unique_fonts.add(font_clean)

for font in sorted(unique_fonts):
    print(font)

# Save detailed report
with open('FONTS_DETAILED_REPORT.txt', 'w', encoding='utf-8') as f:
    f.write("YOLO CHARTERS - COMPLETE FONT ANALYSIS\n")
    f.write("=" * 80 + "\n\n")
    
    f.write("@FONT-FACE DECLARATIONS\n")
    f.write("=" * 80 + "\n")
    for font_face in font_faces:
        f.write(font_face + "\n\n")
    
    f.write("\n\nCSS ROOT VARIABLES (Font-related)\n")
    f.write("=" * 80 + "\n")
    for root_var in root_vars:
        font_vars = re.findall(r'(--[^:]+:[^;]+)', root_var)
        for var in font_vars:
            if 'font' in var.lower():
                f.write(var + "\n")
    
    f.write("\n\nALL FONT FAMILIES USED\n")
    f.write("=" * 80 + "\n")
    for font in sorted(unique_fonts):
        f.write(font + "\n")

print("\n\nDetailed report saved to: FONTS_DETAILED_REPORT.txt")
