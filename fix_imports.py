#!/usr/bin/env python3
import os
import re
from pathlib import Path

# List of files that still have ghauri imports
files_to_fix = [
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\logger\colored_logger.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\extractor\common.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\extractor\advance.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\dbms\fingerprint.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\core\update.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\core\tests.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\core\request.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\core\inject.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\core\extract.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\common\utils.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\common\colors.py",
    r"c:\Users\Mohamed Asem\Downloads\Compressed\ghauri-main\sqlancer\common\banner.py",
]

for filepath in files_to_fix:
    print(f"Fixing {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace all ghauri imports with sqlancer
        content = re.sub(r'from ghauri\.', 'from sqlancer.', content)
        content = re.sub(r'import ghauri([^_])', r'import sqlancer\1', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  -> Fixed successfully")
    except Exception as e:
        print(f"  -> Error: {e}")

print("\nAll imports fixed!")
