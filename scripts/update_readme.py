import os
import re

# Define regex patterns to match folder suffixes/names dynamically,
# regardless of what numbers precede them.
PATTERNS = [
    (r"_Admin$", "Team roles, responsibilities, Gantt chart, project plan"),
    (r"_Background$", "Literature reviews, stakeholder communications, standards & regulations"),
    (r"_Requirements$", "Design inputs, stakeholder needs, requirements traceability"),
    (r"_Meetings$", "Meeting agendas, minutes, action items"),
    (r"_Design$", "Concept generation, evaluation matrices, detailed design"),
    (r"_Implementation$", "Code, manufacturing info, assembly instructions, bills of materials"),
    (r"_Testing$", "Test procedures, raw data, processed results, photos & videos"),
    (r"_Risk_Analysis$", "FMEA, risk mitigation plans"),
    (r"_Design_Reviews$", "Discussion documents and feedback records for each review"),
    (r"_Decisions_Log$", "Decision records linking evidence to choices"),
    (r"_Superseded_Approaches$", "Failed approaches and abandoned designs with reasoning")
]

def get_description(folder_name):
    """Checks the folder name against regex patterns and returns its description."""
    for pattern, description in PATTERNS:
        if re.search(pattern, folder_name):
            return description
    return "Project documentation and files" # Default fallback for unmapped folders

def generate_table():
    # Dynamically scan the actual folders present in the repo
    root_items = sorted(os.listdir('.'))
    ignored = {'.git', '.github', 'node_modules', 'scripts', '__pycache__', '.venv'}

    table_lines = [
        "| Folder | Contents |",
        "|--------|----------|"
    ]

    for item in root_items:
        if os.path.isdir(item) and item not in ignored:
            folder_name = f"`{item}/`"
            description = get_description(item)
            table_lines.append(f"| {folder_name} | {description} |")

    return "\n".join(table_lines)

def update_readme():
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md not found!")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_table = generate_table()

    # Replace content between markers using regex
    pattern = r"(<!-- FOLDER_TABLE_START -->)([\s\S]*?)(<!-- FOLDER_TABLE_END -->)"
    replacement = f"\\1\n{new_table}\n\\3"

    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md folder structure table updated successfully.")
    else:
        print("No changes needed in README.md.")

if __name__ == "__main__":
    update_readme()
