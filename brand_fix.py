import re
import os

def replace_brand(content):
    # 1. Logo image replacements
    content = content.replace("assets/images/pTjMKbpgqUMuwl5KBCRw0sFjoEM.png", "./assets/images/logo.png")
    content = content.replace("https://framerusercontent.com/images/pTjMKbpgqUMuwl5KBCRw0sFjoEM.png", "./assets/images/logo.png")
    
    # 2. Domain and Link replacements
    content = content.replace("https://geniai.framer.website", "https://sistechwork.com")
    
    # 3. Aggressive Split Text Replacement using Regex
    # Pattern for "G-e-n-i" in spans
    geni_split = r'<span[^>]*>[Gg]</span>\s*<span[^>]*>[Ee]</span>\s*<span[^>]*>[Nn]</span>\s*<span[^>]*>[Ii]</span>'
    content = re.sub(geni_split, '<span style="display:inline-block">Sistechwork</span>', content, flags=re.DOTALL)
    
    # Pattern for "G-e-n" followed by "A-I" (case: Gen AI)
    gen_ai_split = r'<span[^>]*>[Gg]</span>\s*<span[^>]*>[Ee]</span>\s*<span[^>]*>[Nn]</span>\s*</span>\s*<span[^>]*><span[^>]*>[Aa]</span>\s*<span[^>]*>[Ii]</span>'
    content = re.sub(gen_ai_split, '<span style="display:inline-block">Sistechwork</span>', content, flags=re.DOTALL)
    
    # Pattern for "A-I" (case: Geni AI) if it follows the now-replaced Sistechwork
    content = re.sub(r'Sistechwork</span>\s*</span>\s*<span[^>]*><span[^>]*>[Aa]</span>\s*<span[^>]*>[Ii]</span>', 'Sistechwork</span>', content, flags=re.DOTALL)
    content = re.sub(r'Sistechwork</span>\s*<span[^>]*>\s*<span[^>]*>[Aa]</span>\s*<span[^>]*>[Ii]</span>', 'Sistechwork</span>', content, flags=re.DOTALL)

    # 4. Literal text replacements (cleaning up any stragglers)
    content = content.replace("Geni AI", "Sistechwork")
    content = content.replace("GeniAI", "Sistechwork")
    content = content.replace("Geni", "Sistechwork")
    content = content.replace("Gen AI", "Sistechwork")
    content = content.replace("@Geni", "@Sistechwork")
    
    # 5. data-framer-name and other attributes
    content = content.replace('data-framer-name="Geni"', 'data-framer-name="Sistechwork"')
    content = content.replace('data-framer-name="Geni AI"', 'data-framer-name="Sistechwork"')
    
    return content

# Read with error handling for encoding
try:
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    with open("index.html", "r", encoding="latin-1") as f:
        content = f.read()

new_content = replace_brand(content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Brand replacement successfully completed with Python.")
