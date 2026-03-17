$filePath = "index.html"
$content = Get-Content $filePath -Raw

# 1. Logo Replacement
# Replace the Geni logo image with the Sistechwork logo
$content = $content.Replace("assets/images/pTjMKbpgqUMuwl5KBCRw0sFjoEM.png", "./assets/images/logo.png")
$content = $content.Replace("https://framerusercontent.com/images/pTjMKbpgqUMuwl5KBCRw0sFjoEM.png?scale-down-to=512", "./assets/images/logo.png")
$content = $content.Replace("https://framerusercontent.com/images/pTjMKbpgqUMuwl5KBCRw0sFjoEM.png", "./assets/images/logo.png")

# 2. Link Replacement
# Update all internal and external links pointing to the old domain
$content = $content.Replace("https://geniai.framer.website/", "https://sistechwork.com/")
$content = $content.Replace("https://geniai.framer.website", "https://sistechwork.com")

# 3. Simple Text Replacement (Literal)
$content = $content.Replace("Geni AI", "Sistechwork")
$content = $content.Replace("GeniAI", "Sistechwork")
$content = $content.Replace(" Gen AI", " Sistechwork") # Handling "Gen AI"
$content = $content.Replace("Geni", "Sistechwork")

# 4. Regex for Split Character Branding (G-e-n-i)
# This matches sequences of spans that spell "Geni" (case insensitive) and replaces them with a single "Sistechwork" block.
$geniPattern = '(?s)<span[^>]*>[Gg]</span>\s*<span[^>]*>[Ee]</span>\s*<span[^>]*>[Nn]</span>\s*<span[^>]*>[Ii]</span>'
$content = [regex]::Replace($content, $geniPattern, '<span style="display:inline-block">Sistechwork</span>')

# 5. Metadata and data-framer-name
$content = $content.Replace('data-framer-name="Geni"', 'data-framer-name="Sistechwork"')
$content = $content.Replace('data-framer-name="Geni AI"', 'data-framer-name="Sistechwork"')

# 6. Copyright
$content = $content.Replace('@Geni', '@Sistechwork')

Set-Content -Path $filePath -Value $content -NoNewline
Write-Host "Brand replacement complete."
