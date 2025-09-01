import os
from pathlib import Path
import shutil
from block_markdown import markdown_to_html_node

# pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
#     matches = re.findall(pattern, text)

def extract_title(markdown: str):

    lines = markdown.split("\n")
    for line in lines:
        if len(line) == 0:
            continue
        if line.lstrip().startswith("# "):
            return line.lstrip().split("# ")[1].strip()
    
    raise Exception("There is no h1")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_path_content = ""
    template_path_content = ""
    with open(from_path) as f:
        from_path_content = f.read()    
    with open(template_path) as f:
        template_path_content = f.read()
    
    html_node = markdown_to_html_node(from_path_content).to_html()
    title = extract_title(from_path_content)

    template_path_content = template_path_content.replace("{{ Title }}", title)
    template_path_content = template_path_content.replace("{{ Content }}", html_node)
 
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    f = open(dest_path, "w")
    f.write(template_path_content)
    f.close()



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

