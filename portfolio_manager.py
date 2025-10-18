#!/usr/bin/env python3
"""
Portfolio Manager - Easy Content Management System
=================================================

This script allows you to easily update your portfolio content without dealing with minified JavaScript files.

Usage:
    python3 portfolio_manager.py

Features:
- Update About section
- Change resume link
- Update social media links
- Modify project information
- Update personal details
- Automatic cache busting
- Git commit and push
"""

import json
import re
import subprocess
import sys
from datetime import datetime

class PortfolioManager:
    def __init__(self):
        self.js_file = "static/js/main.945f37a7.chunk.js"
        self.manifest_file = "asset-manifest.json"
        self.index_file = "index.html"
        
    def read_file(self, filename):
        """Read file content"""
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_file(self, filename, content):
        """Write content to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def update_about_section(self, new_about_text):
        """Update the About section text"""
        print("🔄 Updating About section...")
        content = self.read_file(self.js_file)
        
        # Direct replacement - find any message field and replace it
        pattern = r'message:"[^"]*"'
        new_content = re.sub(pattern, f'message:"{new_about_text}"', content)
        
        self.write_file(self.js_file, new_content)
        print("✅ About section updated!")
    
    def update_resume_link(self, new_resume_url):
        """Update the resume link"""
        print("🔄 Updating resume link...")
        
        # Update JavaScript file
        content = self.read_file(self.js_file)
        pattern = r'resume:"[^"]*"'
        new_content = re.sub(pattern, f'resume:"{new_resume_url}"', content)
        self.write_file(self.js_file, new_content)
        
        # Update asset manifest
        manifest_content = self.read_file(self.manifest_file)
        manifest_data = json.loads(manifest_content)
        manifest_data["files"]["static/media/resume.pdf"] = new_resume_url
        self.write_file(self.manifest_file, json.dumps(manifest_data, indent=2))
        
        print("✅ Resume link updated!")
    
    def update_social_links(self, github=None, linkedin=None, leetcode=None):
        """Update social media links"""
        print("🔄 Updating social media links...")
        content = self.read_file(self.js_file)
        
        # Find the icons array and update URLs
        if github:
            content = re.sub(r'url:"https://github.com/[^"]*"', f'url:"{github}"', content)
        if linkedin:
            content = re.sub(r'url:"https://www.linkedin.com/in/[^"]*"', f'url:"{linkedin}"', content)
        if leetcode:
            content = re.sub(r'url:"https://leetcode.com/u/[^"]*"', f'url:"{leetcode}"', content)
        
        self.write_file(self.js_file, content)
        print("✅ Social media links updated!")
    
    def update_personal_info(self, first_name=None, last_name=None, email=None):
        """Update personal information"""
        print("🔄 Updating personal information...")
        content = self.read_file(self.js_file)
        
        if first_name:
            content = re.sub(r'firstName:"[^"]*"', f'firstName:"{first_name}"', content)
        if last_name:
            content = re.sub(r'lastName:"[^"]*"', f'lastName:"{last_name}"', content)
        if email:
            content = re.sub(r'"[^"]*@[^"]*"', f'"{email}"', content)
        
        self.write_file(self.js_file, content)
        print("✅ Personal information updated!")
    
    def update_cache_busting(self):
        """Update cache busting parameter"""
        print("🔄 Updating cache busting...")
        content = self.read_file(self.index_file)
        
        # Generate new timestamp
        timestamp = datetime.now().strftime("%y%m%d%H")
        
        # Update version parameter
        new_content = re.sub(r'\?v=\d+', f'?v={timestamp}', content)
        self.write_file(self.index_file, new_content)
        
        print("✅ Cache busting updated!")
    
    def commit_and_push(self, message="Updated portfolio content"):
        """Commit changes and push to GitHub"""
        print("🔄 Committing and pushing changes...")
        
        try:
            # Add all changes
            subprocess.run(["git", "add", "."], check=True)
            
            # Commit changes
            subprocess.run(["git", "commit", "-m", message], check=True)
            
            # Push to GitHub
            subprocess.run(["git", "push", "origin", "main"], check=True)
            
            print("✅ Changes committed and pushed to GitHub!")
            print("🌐 Your portfolio will be live at: https://mshivam-kumar.github.io")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e}")
            print("Please check your Git configuration and try again.")
    
    def show_menu(self):
        """Display the main menu"""
        print("\n" + "="*60)
        print("🎯 PORTFOLIO MANAGER - Easy Content Management")
        print("="*60)
        print("1. Update About Section")
        print("2. Change Resume Link")
        print("3. Update Social Media Links")
        print("4. Update Personal Information")
        print("5. Update All and Deploy")
        print("6. Exit")
        print("="*60)
    
    def run(self):
        """Main execution function"""
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                print("\n📝 Update About Section")
                print("Enter your new About section text:")
                about_text = input("> ")
                if about_text:
                    self.update_about_section(about_text)
                    self.update_cache_busting()
            
            elif choice == "2":
                print("\n📄 Update Resume Link")
                print("Enter your new resume URL:")
                resume_url = input("> ")
                if resume_url:
                    self.update_resume_link(resume_url)
                    self.update_cache_busting()
            
            elif choice == "3":
                print("\n🔗 Update Social Media Links")
                github = input("GitHub URL (press Enter to skip): ").strip() or None
                linkedin = input("LinkedIn URL (press Enter to skip): ").strip() or None
                leetcode = input("LeetCode URL (press Enter to skip): ").strip() or None
                
                if any([github, linkedin, leetcode]):
                    self.update_social_links(github, linkedin, leetcode)
                    self.update_cache_busting()
            
            elif choice == "4":
                print("\n👤 Update Personal Information")
                first_name = input("First Name (press Enter to skip): ").strip() or None
                last_name = input("Last Name (press Enter to skip): ").strip() or None
                email = input("Email (press Enter to skip): ").strip() or None
                
                if any([first_name, last_name, email]):
                    self.update_personal_info(first_name, last_name, email)
                    self.update_cache_busting()
            
            elif choice == "5":
                print("\n🚀 Update All and Deploy")
                commit_message = input("Commit message (press Enter for default): ").strip()
                if not commit_message:
                    commit_message = "Updated portfolio content"
                
                self.update_cache_busting()
                self.commit_and_push(commit_message)
            
            elif choice == "6":
                print("\n👋 Goodbye!")
                break
            
            else:
                print("\n❌ Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    manager = PortfolioManager()
    manager.run()
