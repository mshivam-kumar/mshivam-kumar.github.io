#!/usr/bin/env python3
"""
Quick Resume Link Update
========================

Usage: python3 update_resume.py "https://your-new-resume-link.com"
"""

import sys
import re
import subprocess
from datetime import datetime

def update_resume_link(new_url):
    """Update resume link in all necessary files"""
    print(f"🔄 Updating resume link to: {new_url}")
    
    # Update JavaScript file
    with open('static/js/main.945f37a7.chunk.js', 'r') as f:
        content = f.read()
    
    content = re.sub(r'resume:"[^"]*"', f'resume:"{new_url}"', content)
    
    with open('static/js/main.945f37a7.chunk.js', 'w') as f:
        f.write(content)
    
    # Update asset manifest
    import json
    with open('asset-manifest.json', 'r') as f:
        manifest = json.load(f)
    
    manifest["files"]["static/media/resume.pdf"] = new_url
    
    with open('asset-manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)
    
    # Update cache busting
    with open('index.html', 'r') as f:
        index_content = f.read()
    
    timestamp = datetime.now().strftime("%y%m%d%H")
    index_content = re.sub(r'\?v=\d+', f'?v={timestamp}', index_content)
    
    with open('index.html', 'w') as f:
        f.write(index_content)
    
    print("✅ Resume link updated!")
    print("🚀 Deploying changes...")
    
    # Deploy
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Updated resume link"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ Changes deployed to GitHub!")
        print("🌐 Your portfolio is live at: https://mshivam-kumar.github.io")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error deploying: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 update_resume.py \"https://your-resume-link.com\"")
        sys.exit(1)
    
    new_url = sys.argv[1]
    update_resume_link(new_url)
