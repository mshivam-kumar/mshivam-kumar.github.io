# 🎯 Complete Portfolio Management Guide

This guide makes it super easy to update your portfolio without dealing with complex minified JavaScript files.

## 🚀 Quick Start

### Option 1: Interactive Manager (Recommended)
```bash
python3 portfolio_manager.py
```
This gives you a menu-driven interface to update any section.

### Option 2: Configuration File (Recommended)
1. Edit `portfolio_config.json` with your changes
2. Run: `python3 quick_update.py`

### Option 3: Direct Update (Simplest)
```bash
python3 direct_update.py
```
Directly takes text from JSON and updates the website.

### Option 4: Project Management
```bash
python3 project_manager.py
```
For managing projects and adding new sections.

## 📝 How to Update Different Sections

### 1. Update About Section
**Method A (Interactive):**
```bash
python3 portfolio_manager.py
# Choose option 1, enter your new About text
```

**Method B (Config file):**
Edit `portfolio_config.json`:
```json
{
  "about_section": {
    "message": "Your new About section text here..."
  }
}
```
Then run: `python3 quick_update.py`

### 2. Change Resume Link
**Method A (Interactive):**
```bash
python3 portfolio_manager.py
# Choose option 2, enter your new resume URL
```

**Method B (Quick script):**
```bash
python3 update_resume.py "https://your-new-resume-link.com"
```

**Method C (Config file):**
Edit `portfolio_config.json`:
```json
{
  "resume": {
    "url": "https://your-new-resume-link.com"
  }
}
```

### 3. Update Social Media Links
**Method A (Interactive):**
```bash
python3 portfolio_manager.py
# Choose option 3, enter your social media URLs
```

**Method B (Config file):**
Edit `portfolio_config.json`:
```json
{
  "social_links": {
    "github": "https://github.com/yourusername/",
    "linkedin": "https://www.linkedin.com/in/yourprofile/",
    "leetcode": "https://leetcode.com/u/yourusername/"
  }
}
```

### 4. Update Personal Information
**Method A (Interactive):**
```bash
python3 portfolio_manager.py
# Choose option 4, enter your personal details
```

**Method B (Config file):**
Edit `portfolio_config.json`:
```json
{
  "personal_info": {
    "first_name": "Your Name",
    "last_name": "Your Last Name",
    "email": "your.email@domain.com"
  }
}
```

## 🆕 Project Management

### Add New Project
**Method A (Quick):**
```bash
python3 add_project.py
```

**Method B (Full management):**
```bash
python3 project_manager.py
# Choose option 1: Add New Project
```

**Method C (Config file):**
Edit the `projects` array in `portfolio_config.json`:
```json
{
  "projects": [
    {
      "name": "Project Name<br/>(Additional Info)",
      "description": "• Point 1<br/>• Point 2<br/>• Point 3",
      "url": "https://github.com/yourusername/project",
      "date": "2025-01-15T10:30:00Z"
    }
  ]
}
```

### Edit Existing Project
```bash
python3 project_manager.py
# Choose option 2: Edit Existing Project
```

### Delete Project
```bash
python3 project_manager.py
# Choose option 3: Delete Project
```

### List All Projects
```bash
python3 project_manager.py
# Choose option 4: List All Projects
```

## 🆕 Adding New Sections

### Available Section Types
```bash
python3 project_manager.py
# Choose option 5: Add New Section
```

1. **Skills Section** - Technical and soft skills with percentages
2. **Experience Section** - Work experience with role, company, duration
3. **Education Section** - Educational background with degree, institution
4. **Certifications Section** - Professional certifications
5. **Publications Section** - Research publications
6. **Custom Section** - Completely custom content

### Section Configuration Examples

#### Skills Section
```json
{
  "skills": {
    "show": true,
    "heading": "Technical Skills",
    "hard_skills": [
      {"name": "Python", "value": 95},
      {"name": "Machine Learning", "value": 90}
    ],
    "soft_skills": [
      {"name": "Problem Solving", "value": 95},
      {"name": "Leadership", "value": 90}
    ]
  }
}
```

#### Experience Section
```json
{
  "experience": {
    "show": true,
    "heading": "Work Experience",
    "data": [
      {
        "role": "Software Engineer",
        "company": "Tech Company",
        "duration": "Jan 2023 - Present",
        "description": "Developed web applications using React and Node.js"
      }
    ]
  }
}
```

#### Education Section
```json
{
  "education": {
    "show": true,
    "heading": "Education",
    "data": [
      {
        "degree": "Bachelor of Technology",
        "institution": "University Name",
        "year": "2020-2024",
        "gpa": "8.5/10"
      }
    ]
  }
}
```

## 🚀 Deployment

### Automatic Deployment
All scripts offer automatic deployment:
- Interactive manager: Choose option 5
- Quick update: Answer 'y' when prompted
- Project manager: Choose option 6

### Manual Deployment
```bash
git add .
git commit -m "Updated portfolio"
git push origin main
```

## 📁 File Structure

```
mshivam-kumar.github.io/
├── portfolio_manager.py      # Interactive management tool
├── project_manager.py        # Project & section management
├── add_project.py           # Quick project addition
├── update_resume.py         # Quick resume update
├── quick_update.py           # Configuration-based updates
├── portfolio_config.json     # Your portfolio configuration
├── static/js/main.945f37a7.chunk.js  # Main content (auto-updated)
├── asset-manifest.json       # Asset mappings (auto-updated)
└── index.html               # Main page (auto-updated)
```

## 🎨 Formatting Tips

### HTML in Text Fields
You can use HTML tags in your text:
- `<strong>Bold text</strong>`
- `<br/>` for line breaks
- `<em>Italic text</em>`
- `<a href="url">Link text</a>` for links

### Project Descriptions
Use bullet points with line breaks:
```
"• First point<br/>• Second point<br/>• Third point"
```

### Dates
Use ISO format for dates: `2025-01-15T10:30:00Z`

## 🔍 Troubleshooting

### Changes Not Showing?
1. Check if you updated the cache busting parameter
2. Clear your browser cache (Ctrl+F5)
3. Check the live site: https://mshivam-kumar.github.io

### About Section Not Updating?
The About section is embedded in the minified JavaScript. Use the management scripts to update it properly.

### Git Issues?
```bash
git status
git add .
git commit -m "Your message"
git push origin main
```

### Script Errors?
Make sure you're in the correct directory:
```bash
cd /path/to/mshivam-kumar.github.io
python3 portfolio_manager.py
```

## 🎯 Quick Commands

```bash
# Direct update from JSON (simplest)
python3 direct_update.py

# Update everything from config and deploy
python3 quick_update.py

# Interactive updates
python3 portfolio_manager.py

# Add a new project
python3 add_project.py

# Update resume link
python3 update_resume.py "https://new-link.com"

# Full project management
python3 project_manager.py

# Manual deployment
git add . && git commit -m "Update" && git push
```

## 📞 Support

If you need help:
1. Check this guide first
2. Look at the `portfolio_config.json` examples
3. Run the interactive managers for guided updates
4. All content is backed up in the JSON configuration file

---

**Your portfolio is live at: https://mshivam-kumar.github.io** 🌐
