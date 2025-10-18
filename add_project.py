#!/usr/bin/env python3
"""
Quick Project Addition Script
=============================

Usage: python3 add_project.py
"""

import json
import sys
from datetime import datetime

def add_project():
    """Add a new project interactively"""
    print("🆕 Add New Project")
    print("=" * 40)
    
    # Load current config
    with open('portfolio_config.json', 'r') as f:
        config = json.load(f)
    
    # Get project details
    name = input("Project Name: ").strip()
    if not name:
        print("❌ Project name is required!")
        return
    
    print("\nEnter project description:")
    print("Use • for bullet points, <br/> for line breaks")
    print("Example: • First point<br/>• Second point<br/>• Third point")
    description = input("Description: ").strip()
    
    url = input("GitHub URL: ").strip()
    if not url:
        print("❌ GitHub URL is required!")
        return
    
    date = input("Date (YYYY-MM-DD format, or press Enter for today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    date += "T10:30:00Z"
    
    # Add new project
    new_project = {
        "name": name,
        "description": description,
        "url": url,
        "date": date
    }
    
    config["projects"].append(new_project)
    
    # Save config
    with open('portfolio_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Project '{name}' added successfully!")
    
    # Ask if user wants to deploy
    deploy = input("\nDeploy to GitHub? (y/n): ").lower().strip()
    if deploy == 'y':
        import subprocess
        try:
            subprocess.run(["python3", "quick_update.py"], 
                          input="y\n", text=True)
            print("✅ Changes deployed!")
        except Exception as e:
            print(f"❌ Error deploying: {e}")

if __name__ == "__main__":
    add_project()
