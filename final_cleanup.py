#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Final pass to fix all lowercase "ghauri" in user-facing strings
REPLACEMENTS = {
    r'(["\'])ghauri(["\']| is| will| detected| was| could| can|currently)': r'\1SQLancer\2',
    r'update ghauri': 'update SQLancer',
    r'performance of ghauri': 'performance of SQLancer',
    r'git clone %s ghauri': 'git clone %s sqlancer',
    r'# ghauri ': '# sqlancer ',
}

# Directories to search
sqlancer_dir = r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer"

# Get all Python files
python_files = list(Path(sqlancer_dir).rglob("*.py"))

print(f"Found {len(python_files)} Python files to process...\n")

total_replacements = 0

for filepath in python_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_replacements = 0
        
        # Apply all replacements
        for pattern, replacement in REPLACEMENTS.items():
            matches = len(re.findall(pattern, content))
            if matches > 0:
                content = re.sub(pattern, replacement, content)
                file_replacements += matches
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filepath.name}: {file_replacements} replacements")
            total_replacements += file_replacements
    
    except Exception as e:
        print(f"✗ {filepath.name}: Error - {e}")

print(f"\n{'='*60}")
print(f"Total string replacements made: {total_replacements}")
print(f"{'='*60}")
