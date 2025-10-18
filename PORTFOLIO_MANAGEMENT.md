# 🎯 Portfolio Management Guide

This guide makes it super easy to update your portfolio without dealing with complex minified JavaScript files.

## 🚀 Quick Start

### Option 1: Interactive Manager (Recommended)
```bash
python3 portfolio_manager.py
```
This gives you a menu-driven interface to update any section.

### Option 2: Configuration File
1. Edit `portfolio_config.json` with your changes
2. Run: `python3 quick_update.py`

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

**Method B (Config file):**
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

## 🔧 Advanced Usage

### Update Projects
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

### Manual Cache Busting
If you need to force a browser refresh:
```bash
# Edit index.html and change ?v=XXXXXX to a new number
# Or run the scripts which do this automatically
```

## 🚀 Deployment

### Automatic Deployment
Both scripts offer automatic deployment:
- Interactive manager: Choose option 5
- Quick update: Answer 'y' when prompted

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
├── quick_update.py           # Configuration-based updates
├── portfolio_config.json     # Your portfolio configuration
├── static/js/main.945f37a7.chunk.js  # Main content (auto-updated)
├── asset-manifest.json       # Asset mappings (auto-updated)
└── index.html               # Main page (auto-updated)
```

## 🎨 Customization Tips

### HTML in Text Fields
You can use HTML tags in your text:
- `<strong>Bold text</strong>`
- `<br/>` for line breaks
- `<em>Italic text</em>`

### Project Descriptions
Use `<br/>` for line breaks in project descriptions:
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

## 📞 Support

If you need help:
1. Check this guide first
2. Look at the `portfolio_config.json` examples
3. Run the interactive manager for guided updates

## 🎯 Quick Commands

```bash
# Update everything from config and deploy
python3 quick_update.py

# Interactive updates
python3 portfolio_manager.py

# Manual deployment
git add . && git commit -m "Update" && git push
```

---

**Your portfolio is live at: https://mshivam-kumar.github.io** 🌐
