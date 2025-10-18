#!/usr/bin/env python3
"""
Direct Portfolio Update - Simple Text Replacement
===============================================

This script directly replaces content from JSON config to the website
without complex pattern matching.
"""

import json
import re
from datetime import datetime

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def update_portfolio():
    """Update portfolio directly from JSON config"""
    print("🔄 Updating portfolio from JSON config...")
    
    # Load JSON config
    with open('portfolio_config.json', 'r') as f:
        config = json.load(f)
    
    # Read JavaScript file
    js_content = read_file('static/js/main.945f37a7.chunk.js')
    
    # 1. Update personal info
    print("📝 Updating personal information...")
    js_content = js_content.replace(f'firstName:"{config["personal_info"]["first_name"]}"', f'firstName:"{config["personal_info"]["first_name"]}"')
    js_content = js_content.replace(f'lastName:"{config["personal_info"]["last_name"]}"', f'lastName:"{config["personal_info"]["last_name"]}"')
    
    # 2. Update About section - find and replace the entire message
    print("📝 Updating About section...")
    about_text = config["about_section"]["message"]
    
    # Find the current message and replace it
    current_message_pattern = r'message:"[^"]*"'
    js_content = re.sub(current_message_pattern, f'message:"{about_text}"', js_content)
    
    # 3. Update resume link
    print("📄 Updating resume link...")
    resume_url = config["resume"]["url"]
    resume_pattern = r'resume:"[^"]*"'
    js_content = re.sub(resume_pattern, f'resume:"{resume_url}"', js_content)
    
    # 4. Update social links
    print("🔗 Updating social media links...")
    social = config["social_links"]
    
    # GitHub
    github_pattern = r'url:"https://github\.com/[^"]*"'
    js_content = re.sub(github_pattern, f'url:"{social["github"]}"', js_content)
    
    # LinkedIn
    linkedin_pattern = r'url:"https://www\.linkedin\.com/in/[^"]*"'
    js_content = re.sub(linkedin_pattern, f'url:"{social["linkedin"]}"', js_content)
    
    # LeetCode
    leetcode_pattern = r'url:"https://leetcode\.com/u/[^"]*"'
    js_content = re.sub(leetcode_pattern, f'url:"{social["leetcode"]}"', js_content)
    
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
    
    print("✅ Portfolio updated successfully!")
    print("🌐 Changes will be visible on the website!")

if __name__ == "__main__":
    update_portfolio()
