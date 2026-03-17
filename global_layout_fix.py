import re
import os

def global_layout_fix(content):
    # 1. Fix the cascading subtext by replacing the fragmented reveal spans
    # The subtext starts with "Work smarter" and ends with "easier."
    # We'll use a regex that matches the entire fragmented paragraph structure.
    
    # Matching the specific fragmented structure commonly used by Framer
    # <p class="framer-text..."><span style="white-space:nowrap"><span ...>W</span>...</span>...</p>
    content = re.sub(
        r'<p class="framer-text framer-styles-preset-18p0xtk" data-styles-preset="X7htgiN0Z">.*?Work.*?smarter.*?create.*?faster.*?achieve.*?more.*?Sistechwork.*?advanced.*?features.*?designed.*?to.*?make.*?your.*?life.*?easier.*?</p>',
        '<p class="framer-text framer-styles-preset-18p0xtk" data-styles-preset="X7htgiN0Z">Work smarter, create faster, and achieve more with Sistechwork\'s advanced features designed to make your life easier.</p>',
        content,
        flags=re.DOTALL
    )
    
    # 2. Remove the phone-shaped background from ALL variants
    # Target the specific border-radius and box-shadow identified by the subagent
    content = content.replace('border-radius: 78px; box-shadow: rgba(0, 0, 0, 0.26) -38px 21px 62px 0px;', '')
    content = content.replace('border-radius: 78px; box-shadow: rgba(0, 0, 0, 0.26) -38px 21px 62px 0px', '')
    
    # 3. Clean up any remaining "Phone" name attributes if they cause confusion
    content = content.replace('data-framer-name="Phone"', 'data-framer-name="Laptop"')
    
    return content

try:
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    with open("index.html", "r", encoding="latin-1") as f:
        content = f.read()

new_content = global_layout_fix(content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Global layout fix completed.")
