import re
import os

def final_polish(content):
    # 1. Simplify "Sistechwork AI" to "Sistechwork" in targeted areas
    # This addresses the subagent's feedback about keeping it simple
    content = content.replace("Sistechwork AI", "Sistechwork")
    content = content.replace("Sistechwork AI's", "Sistechwork's")
    
    # 2. Fix "@Sistech" to "@Sistechwork" in copyright if needed
    content = content.replace("@Sistech", "@Sistechwork")
    
    # 3. Ensure the logo image is used everywhere the Geni logo was
    content = content.replace("assets/images/pTjMKbpgqUMuwl5KBCRw0sFjoEM.png", "./assets/images/logo.png")
    
    return content

try:
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    with open("index.html", "r", encoding="latin-1") as f:
        content = f.read()

new_content = final_polish(content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Final branding polish completed.")
