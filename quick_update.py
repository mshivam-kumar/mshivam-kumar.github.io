#!/usr/bin/env python3
"""
Quick Portfolio Update Script
============================

This script reads from portfolio_config.json and updates your portfolio automatically.

Usage:
    python3 quick_update.py
"""

import json
import re
import subprocess
from datetime import datetime

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def update_from_config():
    """Update portfolio from configuration file"""
    print("🔄 Reading configuration...")
    
    # Load configuration
    with open('portfolio_config.json', 'r') as f:
        config = json.load(f)
    
    # Read JavaScript file
    js_content = read_file('static/js/main.945f37a7.chunk.js')
    
    # Update personal info
    print("📝 Updating personal information...")
    js_content = re.sub(r'firstName:"[^"]*"', f'firstName:"{config["personal_info"]["first_name"]}"', js_content)
    js_content = re.sub(r'lastName:"[^"]*"', f'lastName:"{config["personal_info"]["last_name"]}"', js_content)
    js_content = re.sub(r'"[^"]*@[^"]*"', f'"{config["personal_info"]["email"]}"', js_content)
    
    # Update About section - direct replacement
    print("📝 Updating About section...")
    about_text = config["about_section"]["message"]
    js_content = re.sub(r'message:"[^"]*"', f'message:"{about_text}"', js_content)
    
    # Update resume link
    print("📄 Updating resume link...")
    resume_url = config["resume"]["url"]
    js_content = re.sub(r'resume:"[^"]*"', f'resume:"{resume_url}"', js_content)
    
    # Update social links
    print("🔗 Updating social media links...")
    social = config["social_links"]
    js_content = re.sub(r'url:"https://github.com/[^"]*"', f'url:"{social["github"]}"', js_content)
    js_content = re.sub(r'url:"https://www.linkedin.com/in/[^"]*"', f'url:"{social["linkedin"]}"', js_content)
    js_content = re.sub(r'url:"https://leetcode.com/u/[^"]*"', f'url:"{social["leetcode"]}"', js_content)
    
    # Write updated JavaScript
    write_file('static/js/main.945f37a7.chunk.js', js_content)
    
    # Update asset manifest
    print("📄 Updating asset manifest...")
    manifest_content = read_file('asset-manifest.json')
    manifest_data = json.loads(manifest_content)
    manifest_data["files"]["static/media/resume.pdf"] = resume_url
    write_file('asset-manifest.json', json.dumps(manifest_data, indent=2))
    
    # Update cache busting
    print("🔄 Updating cache busting...")
    index_content = read_file('index.html')
    timestamp = datetime.now().strftime("%y%m%d%H")
    index_content = re.sub(r'\?v=\d+', f'?v={timestamp}', index_content)
    write_file('index.html', index_content)
    
    print("✅ Portfolio updated from configuration!")

def commit_and_push():
    """Commit and push changes"""
    print("🚀 Committing and pushing changes...")
    
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Updated portfolio from configuration"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ Changes pushed to GitHub!")
        print("🌐 Your portfolio is live at: https://mshivam-kumar.github.io")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🎯 Quick Portfolio Update")
    print("=" * 40)
    
    update_from_config()
    
    deploy = input("\nDeploy to GitHub? (y/n): ").lower().strip()
    if deploy == 'y':
        commit_and_push()
    else:
        print("📝 Changes saved locally. Run 'git add . && git commit -m \"Update\" && git push' to deploy.")
