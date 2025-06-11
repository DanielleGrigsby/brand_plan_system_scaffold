import os

# ABSOLUTE PATH — update if your location changes
BASE_PATH = "/Volumes/1 up 24/001_design_tools_resources/design_brand_plan/design_brand_plan_assets/design_brand_plan_assets_color"

print(f"\n📍 Current Working Directory: {os.getcwd()}")
print(f"📂 Target BASE_PATH: {BASE_PATH}")
print("🔍 Starting folder creation...\n")

structure = [
    ("01_Palette", [
        "Primary Colors",
        "Secondary Colors",
        "Tertiary Colors",
        "Core Colors",
        "Accent Colors",
        "Neutral Colors"
    ]),
    ("02_Neutrals", [
        "Neutral Primary",
        "Neutral Secondary",
        "Neutral Colors"
    ]),
    ("03_Accents", [
        "Accent Primary",
        "Accent Secondary",
        "Accent Tertiary",
        "Accent Colors"
    ]),
    ("04_Tints", [
        "Tints-Accent Primary",
        "Tints-Accent Secondary",
        "Tints-Accent Tertiary",
        "Tints-Accent Quaternary",
        "Tints-Neutral Primary",
        "Tints-Neutral Inverse"
    ]),
    ("05_Backgrounds", [
        "BG-Primary",
        "BG-Secondary",
        "BG-Accent Primary",
        "BG-Accent Secondary",
        "BG-Accent Tertiary",
        "BG-Inverse"
    ]),
    ("06_Text", [
        "Text Primary",
        "Text Secondary",
        "Text Inverse Primary",
        "Text Inverse Secondary",
        "Text Accent Primary",
        "Text Accent Secondary"
    ]),
]

for superfolder, color_types in structure:
    for color_type in color_types:
        folder_path = os.path.join(BASE_PATH, superfolder, color_type)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"✅ Created: {folder_path}")
        except Exception as e:
            print(f"❌ Failed: {folder_path} — {e}")

print("\n🎉 All color folders have been created in the correct structure!\n")
