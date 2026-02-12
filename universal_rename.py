import os
import re

def replace_ghauri(content):
    # Order matters! Specific replacements first.
    
    # 1. Ghauri -> SQLancer (Class names, Titles)
    content = re.sub(r'\bGhauri\b', 'SQLancer', content)
    
    # 2. GHAURI -> SQLANCER (Constants)
    content = re.sub(r'\bGHAURI\b', 'SQLANCER', content)
    
    # 3. ghauri -> sqlancer (Variables, packages, general lowercase)
    content = re.sub(r'\bghauri\b', 'sqlancer', content)
    
    # 4. Handle Mixed Case/Substring occurrences if needed (be careful)
    # e.g., update_ghauri -> update_sqlancer
    content = re.sub(r'update_ghauri', 'update_sqlancer', content)
    content = re.sub(r'ghauri_extractor', 'sqlancer_extractor', content)
    
    return content

root_dir = r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".py"):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = replace_ghauri(content)
                
                if new_content != content:
                    print(f"Updating {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"Failed to process {filepath}: {e}")

# Also update the main script separately if it's not in the walk path
script_path = r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer.py" 
if os.path.exists(script_path):
     with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
     new_content = replace_ghauri(content)
     if new_content != content:
        print(f"Updating {script_path}")
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Replacement complete.")
