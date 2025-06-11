import os

BASE_PATH = "/Volumes/1 up 24/001_design_tools_resources/design_brand_plan/design_brand_plan_assets/design_brand_plan_assets_elements"

folders = [
    "Texture",
    "Badge",
    "Shape",
    "Photography",
    "Background",
    "Icon",
    "Pattern",
    "Line",
    "Divider",
    "Overlay"
]

print(f"\n📂 Creating folders inside: {BASE_PATH}\n")

for folder in folders:
    path = os.path.join(BASE_PATH, folder)
    os.makedirs(path, exist_ok=True)
    print(f"✅ Created: {path}")

print("\n🎉 All design element folders created!\n")
