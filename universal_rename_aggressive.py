import os

def replace_ghauri_aggressive(content):
    # Simple string replacements to catch everything
    # Order matters to preserve case as much as possible
    
    # 1. Ghauri -> SQLancer (Mixed case)
    content = content.replace('Ghauri', 'SQLancer')
    
    # 2. GHAURI -> SQLANCER (Upper case)
    content = content.replace('GHAURI', 'SQLANCER')
    
    # 3. ghauri -> sqlancer (Lower case)
    # This matches 'ghauri' inside other words too, but since we already did Ghauri/GHAURI, 
    # the remaining 'ghauri' substrings are likely part of snake_case or lowercase references.
    content = content.replace('ghauri', 'sqlancer')
    
    return content

root_dir = r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer"

print("Starting aggressive rename...")
count = 0
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".py") or filename.endswith(".md") or filename.endswith(".txt"):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = replace_ghauri_aggressive(content)
                
                if new_content != content:
                    print(f"Updating {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception as e:
                print(f"Failed to process {filepath}: {e}")

# Main script
script_path = r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer.py" 
if os.path.exists(script_path):
     with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
     new_content = replace_ghauri_aggressive(content)
     if new_content != content:
        print(f"Updating {script_path}")
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

# Setup.py (in root)
setup_path = r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\setup.py"
if os.path.exists(setup_path):
     with open(setup_path, 'r', encoding='utf-8') as f:
        content = f.read()
     new_content = replace_ghauri_aggressive(content)
     if new_content != content:
        print(f"Updating {setup_path}")
        with open(setup_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Aggressive replacement complete. Updated {count} files.")
