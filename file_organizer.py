import os
import shutil
from pathlib import Path

TRACKED_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".tar", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}

def organize_folder(target_folder):
    target_path = Path(target_folder)
    
    if not target_path.exists():
        print(f"❌ Error: The directory '{target_folder}' does not exist.")
        return

    print(f"⚡ Scanning and organizing: {target_path.resolve()}\n")
    moved_count = 0

    for item in target_path.iterdir():
        if item.is_dir():
            continue
            
        if item.name == "file_organizer.py":
            continue

        file_extension = item.suffix.lower()
        moved = False

        for category, extensions in TRACKED_EXTENSIONS.items():
            if file_extension in extensions:
                category_dir = target_path / category
                category_dir.mkdir(exist_ok=True)
                
                destination = category_dir / item.name
                
                try:
                    shutil.move(str(item), str(destination))
                    print(f"📁 Moved: {item.name} ➔ {category}/")
                    moved_count += 1
                    moved = True
                except Exception as e:
                    print(f"❌ Failed to move {item.name}: {e}")
                break
        
        if not moved and file_extension != "":
            others_dir = target_path / "Others"
            others_dir.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(others_dir / item.name))
                print(f"📁 Moved: {item.name} ➔ Others/")
                moved_count += 1
            except Exception as e:
                print(f"❌ Failed to move {item.name}: {e}")

    print(f"\n✨ Done! Organized {moved_count} files.")

if __name__ == "__main__":
    folder_to_clean = input("Enter the absolute path of the folder to organize (or '.' for current folder): ").strip()
    organize_folder(folder_to_clean)