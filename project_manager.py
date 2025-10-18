#!/usr/bin/env python3
"""
Project Manager - Add/Edit Projects and Sections
===============================================

This script allows you to easily manage projects and add new sections to your portfolio.

Usage:
    python3 project_manager.py
"""

import json
import re
import subprocess
from datetime import datetime

class ProjectManager:
    def __init__(self):
        self.js_file = "static/js/main.945f37a7.chunk.js"
        self.config_file = "portfolio_config.json"
        
    def read_file(self, filename):
        """Read file content"""
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_file(self, filename, content):
        """Write content to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def load_config(self):
        """Load portfolio configuration"""
        with open(self.config_file, 'r') as f:
            return json.load(f)
    
    def save_config(self, config):
        """Save portfolio configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def add_new_project(self):
        """Add a new project"""
        print("\n🆕 Adding New Project")
        print("=" * 40)
        
        name = input("Project Name: ").strip()
        if not name:
            print("❌ Project name is required!")
            return
        
        print("\nEnter project description (use • for bullet points, <br/> for line breaks):")
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
        
        # Load current config
        config = self.load_config()
        
        # Add new project
        new_project = {
            "name": name,
            "description": description,
            "url": url,
            "date": date
        }
        
        config["projects"].append(new_project)
        self.save_config(config)
        
        print(f"✅ Project '{name}' added successfully!")
        return new_project
    
    def edit_existing_project(self):
        """Edit an existing project"""
        print("\n✏️ Edit Existing Project")
        print("=" * 40)
        
        config = self.load_config()
        projects = config["projects"]
        
        if not projects:
            print("❌ No projects found!")
            return
        
        # Show existing projects
        print("\nCurrent Projects:")
        for i, project in enumerate(projects, 1):
            print(f"{i}. {project['name'].replace('<br/>', ' ').replace('<strong>', '').replace('</strong>', '')}")
        
        try:
            choice = int(input(f"\nSelect project to edit (1-{len(projects)}): ")) - 1
            if choice < 0 or choice >= len(projects):
                print("❌ Invalid selection!")
                return
            
            project = projects[choice]
            print(f"\nEditing: {project['name']}")
            
            # Edit fields
            new_name = input(f"Name (current: {project['name']}): ").strip()
            if new_name:
                project['name'] = new_name
            
            new_desc = input(f"Description (current: {project['description'][:50]}...): ").strip()
            if new_desc:
                project['description'] = new_desc
            
            new_url = input(f"URL (current: {project['url']}): ").strip()
            if new_url:
                project['url'] = new_url
            
            new_date = input(f"Date (current: {project['date']}): ").strip()
            if new_date:
                if not new_date.endswith('Z'):
                    new_date += "T10:30:00Z"
                project['date'] = new_date
            
            self.save_config(config)
            print("✅ Project updated successfully!")
            
        except ValueError:
            print("❌ Invalid input!")
    
    def delete_project(self):
        """Delete a project"""
        print("\n🗑️ Delete Project")
        print("=" * 40)
        
        config = self.load_config()
        projects = config["projects"]
        
        if not projects:
            print("❌ No projects found!")
            return
        
        # Show existing projects
        print("\nCurrent Projects:")
        for i, project in enumerate(projects, 1):
            print(f"{i}. {project['name'].replace('<br/>', ' ').replace('<strong>', '').replace('</strong>', '')}")
        
        try:
            choice = int(input(f"\nSelect project to delete (1-{len(projects)}): ")) - 1
            if choice < 0 or choice >= len(projects):
                print("❌ Invalid selection!")
                return
            
            project_name = projects[choice]['name']
            confirm = input(f"Are you sure you want to delete '{project_name}'? (y/n): ").lower().strip()
            
            if confirm == 'y':
                del projects[choice]
                self.save_config(config)
                print("✅ Project deleted successfully!")
            else:
                print("❌ Deletion cancelled!")
                
        except ValueError:
            print("❌ Invalid input!")
    
    def add_new_section(self):
        """Add a new section to the portfolio"""
        print("\n🆕 Adding New Section")
        print("=" * 40)
        
        print("Available section types:")
        print("1. Skills Section")
        print("2. Experience Section") 
        print("3. Education Section")
        print("4. Certifications Section")
        print("5. Publications Section")
        print("6. Custom Section")
        
        section_type = input("\nSelect section type (1-6): ").strip()
        
        if section_type == "1":
            self.add_skills_section()
        elif section_type == "2":
            self.add_experience_section()
        elif section_type == "3":
            self.add_education_section()
        elif section_type == "4":
            self.add_certifications_section()
        elif section_type == "5":
            self.add_publications_section()
        elif section_type == "6":
            self.add_custom_section()
        else:
            print("❌ Invalid selection!")
    
    def add_skills_section(self):
        """Add a skills section"""
        print("\n🛠️ Adding Skills Section")
        print("=" * 40)
        
        config = self.load_config()
        
        # Add skills section to config
        if "skills" not in config:
            config["skills"] = {
                "show": True,
                "heading": "Technical Skills",
                "hard_skills": [],
                "soft_skills": []
            }
        
        print("Add technical skills (enter skill name and percentage, e.g., 'Python 95'):")
        print("Press Enter with empty input to finish")
        
        while True:
            skill_input = input("Skill: ").strip()
            if not skill_input:
                break
            
            try:
                skill_name, percentage = skill_input.rsplit(' ', 1)
                percentage = int(percentage)
                config["skills"]["hard_skills"].append({
                    "name": skill_name,
                    "value": percentage
                })
                print(f"✅ Added {skill_name} ({percentage}%)")
            except:
                print("❌ Invalid format! Use 'Skill Name Percentage'")
        
        print("\nAdd soft skills (enter skill name and percentage):")
        while True:
            skill_input = input("Soft Skill: ").strip()
            if not skill_input:
                break
            
            try:
                skill_name, percentage = skill_input.rsplit(' ', 1)
                percentage = int(percentage)
                config["skills"]["soft_skills"].append({
                    "name": skill_name,
                    "value": percentage
                })
                print(f"✅ Added {skill_name} ({percentage}%)")
            except:
                print("❌ Invalid format! Use 'Skill Name Percentage'")
        
        self.save_config(config)
        print("✅ Skills section added!")
    
    def add_experience_section(self):
        """Add an experience section"""
        print("\n💼 Adding Experience Section")
        print("=" * 40)
        
        config = self.load_config()
        
        if "experience" not in config:
            config["experience"] = {
                "show": True,
                "heading": "Work Experience",
                "data": []
            }
        
        role = input("Job Title: ").strip()
        company = input("Company: ").strip()
        duration = input("Duration (e.g., 'Jan 2023 - Present'): ").strip()
        description = input("Description: ").strip()
        
        new_experience = {
            "role": role,
            "company": company,
            "duration": duration,
            "description": description
        }
        
        config["experience"]["data"].append(new_experience)
        self.save_config(config)
        print("✅ Experience added!")
    
    def add_education_section(self):
        """Add an education section"""
        print("\n🎓 Adding Education Section")
        print("=" * 40)
        
        config = self.load_config()
        
        if "education" not in config:
            config["education"] = {
                "show": True,
                "heading": "Education",
                "data": []
            }
        
        degree = input("Degree: ").strip()
        institution = input("Institution: ").strip()
        year = input("Year: ").strip()
        gpa = input("GPA (optional): ").strip()
        
        new_education = {
            "degree": degree,
            "institution": institution,
            "year": year,
            "gpa": gpa
        }
        
        config["education"]["data"].append(new_education)
        self.save_config(config)
        print("✅ Education added!")
    
    def add_certifications_section(self):
        """Add a certifications section"""
        print("\n🏆 Adding Certifications Section")
        print("=" * 40)
        
        config = self.load_config()
        
        if "certifications" not in config:
            config["certifications"] = {
                "show": True,
                "heading": "Certifications",
                "data": []
            }
        
        name = input("Certification Name: ").strip()
        issuer = input("Issuer: ").strip()
        date = input("Date: ").strip()
        credential_id = input("Credential ID (optional): ").strip()
        
        new_cert = {
            "name": name,
            "issuer": issuer,
            "date": date,
            "credential_id": credential_id
        }
        
        config["certifications"]["data"].append(new_cert)
        self.save_config(config)
        print("✅ Certification added!")
    
    def add_publications_section(self):
        """Add a publications section"""
        print("\n📚 Adding Publications Section")
        print("=" * 40)
        
        config = self.load_config()
        
        if "publications" not in config:
            config["publications"] = {
                "show": True,
                "heading": "Publications",
                "data": []
            }
        
        title = input("Publication Title: ").strip()
        authors = input("Authors: ").strip()
        venue = input("Venue/Journal: ").strip()
        year = input("Year: ").strip()
        link = input("Link (optional): ").strip()
        
        new_pub = {
            "title": title,
            "authors": authors,
            "venue": venue,
            "year": year,
            "link": link
        }
        
        config["publications"]["data"].append(new_pub)
        self.save_config(config)
        print("✅ Publication added!")
    
    def add_custom_section(self):
        """Add a custom section"""
        print("\n🔧 Adding Custom Section")
        print("=" * 40)
        
        config = self.load_config()
        
        section_name = input("Section Name: ").strip()
        heading = input("Section Heading: ").strip()
        content = input("Section Content: ").strip()
        
        section_key = section_name.lower().replace(" ", "_")
        
        config[section_key] = {
            "show": True,
            "heading": heading,
            "content": content
        }
        
        self.save_config(config)
        print("✅ Custom section added!")
    
    def show_menu(self):
        """Display the main menu"""
        print("\n" + "="*60)
        print("🎯 PROJECT & SECTION MANAGER")
        print("="*60)
        print("PROJECTS:")
        print("1. Add New Project")
        print("2. Edit Existing Project")
        print("3. Delete Project")
        print("4. List All Projects")
        print("")
        print("SECTIONS:")
        print("5. Add New Section")
        print("6. Update and Deploy")
        print("7. Exit")
        print("="*60)
    
    def list_projects(self):
        """List all current projects"""
        print("\n📋 Current Projects")
        print("=" * 40)
        
        config = self.load_config()
        projects = config.get("projects", [])
        
        if not projects:
            print("No projects found!")
            return
        
        for i, project in enumerate(projects, 1):
            print(f"\n{i}. {project['name'].replace('<br/>', ' ').replace('<strong>', '').replace('</strong>', '')}")
            print(f"   URL: {project['url']}")
            print(f"   Date: {project['date']}")
            print(f"   Description: {project['description'][:100]}...")
    
    def update_and_deploy(self):
        """Update portfolio and deploy"""
        print("\n🚀 Updating and Deploying")
        print("=" * 40)
        
        # Run the quick update script
        import subprocess
        try:
            result = subprocess.run(["python3", "quick_update.py"], 
                                  input="y\n", text=True, capture_output=True)
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def run(self):
        """Main execution function"""
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                self.add_new_project()
            elif choice == "2":
                self.edit_existing_project()
            elif choice == "3":
                self.delete_project()
            elif choice == "4":
                self.list_projects()
            elif choice == "5":
                self.add_new_section()
            elif choice == "6":
                self.update_and_deploy()
            elif choice == "7":
                print("\n👋 Goodbye!")
                break
            else:
                print("\n❌ Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    manager = ProjectManager()
    manager.run()
