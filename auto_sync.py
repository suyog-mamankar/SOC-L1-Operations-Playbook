import os
import subprocess
from datetime import datetime

# --- Configuration ---
NOTES_DIR = "notes"
README_FILE = "README.md"

def extract_topics(filepath):
    """Extracts H2 headers from the markdown file to use as topics."""
    topics = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('## '):
                    topic = line.replace('## ', '').strip()
                    # Remove numbered prefixes (e.g., "1. " or "1.1 ")
                    if topic[0].isdigit():
                        topic = topic.split(' ', 1)[-1]
                    topics.append(topic)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    # Return a clean, comma-separated list of the top 3-4 topics
    return ", ".join(topics[:4]) if topics else "Topics to be documented."

def generate_markdown_elements():
    """Builds the dynamic text for the Structure, Index, and Roadmap."""
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
        print(f"Created '{NOTES_DIR}' directory.")
        
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith('.md')]
    files.sort()
    
    # Initialize sections
    structure_lines = ["```text", "SOC-L1-Operations-Playbook/", "├── README.md", "├── auto_sync.py", "└── notes/"]
    index_lines = ["| Day | File | Topics Covered |", "| :--- | :--- | :--- |"]
    roadmap_lines = []
    
    day_num = 0
    
    for i, file in enumerate(files):
        # 1. Build Structure Tree
        prefix = "    └── " if i == len(files) - 1 else "    ├── "
        structure_lines.append(f"{prefix}{file}")
        
        # 2. Parse Day and Title
        name_without_ext = file.replace('.md', '')
        parts = name_without_ext.split('-')
        
        if len(parts) >= 2 and parts[0] == "Day":
            try:
                day_num = int(parts[1])
            except ValueError:
                day_num = i + 1
            title = " ".join(parts[2:])
        else:
            day_num = i + 1
            title = name_without_ext.replace('-', ' ')
            
        topics = extract_topics(os.path.join(NOTES_DIR, file))
        
        # 3. Build Index Row
        index_lines.append(f"| **Day {day_num}** | [`notes/{file}`](notes/{file}) | {title} - {topics} |")
        
        # 4. Build Roadmap Checkbox
        roadmap_lines.append(f"- [x] Day {day_num} — {title}")

    structure_lines.append("```")
    
    # Add upcoming projections to roadmap
    roadmap_lines.append(f"- [ ] Day {day_num + 1} — (Upcoming Masterclass)")
    roadmap_lines.append(f"- [ ] Day {day_num + 2}+ — (To be added)")
    
    return "\n".join(structure_lines), "\n".join(index_lines), "\n".join(roadmap_lines)

def inject_content(content, start_marker, end_marker, new_text):
    """Safely injects the new markdown between the designated markers."""
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print(f"⚠️ Warning: Could not find markers {start_marker} and {end_marker} in README.md")
        return content
        
    return (
        content[:start_idx + len(start_marker)] + 
        "\n\n" + new_text + "\n\n" + 
        content[end_idx:]
    )

def update_readme():
    """Coordinates reading, injecting, and saving the README."""
    structure_text, index_text, roadmap_text = generate_markdown_elements()

    if not os.path.exists(README_FILE):
        print(f"Error: {README_FILE} not found in root directory.")
        return False

    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = inject_content(content, "<!-- STRUCTURE_START -->", "<!-- STRUCTURE_END -->", structure_text)
    content = inject_content(content, "<!-- INDEX_START -->", "<!-- INDEX_END -->", index_text)
    content = inject_content(content, "<!-- ROADMAP_START -->", "<!-- ROADMAP_END -->", roadmap_text)
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ README.md auto-generated and updated successfully.")
    return True

def git_sync():
    """Uploads everything directly to GitHub."""
    print("🚀 Pushing updates to GitHub...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Stage all new files and the updated README
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit the changes
        result = subprocess.run(
            ["git", "commit", "-m", f"Automated playbook sync & README update: {timestamp}"],
            capture_output=True, text=True
        )
        
        if "nothing to commit" in result.stdout.lower():
            print("No new changes to push.")
            return
            
        # Push to repository
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Successfully uploaded to GitHub!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git command failed: Make sure you are authenticated and connected to the internet. Error: {e}")

if __name__ == "__main__":
    print("--- Starting Enterprise SOC Playbook Sync ---")
    if update_readme():
        git_sync()
    print("--- Sync Complete ---")