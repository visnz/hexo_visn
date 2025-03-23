import os
import re
import requests
from urllib.parse import urlparse

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

def replace_image_links(md_content, image_links, base_name, save_dir):
    for i, img_url in enumerate(image_links, start=1):
        img_name = f"{base_name}{i}.webp"
        img_path = os.path.join(save_dir, img_name)
        download_image(img_url, img_path)
        relative_path = f"/assets/blog/CG/{img_name}"
        md_content = md_content.replace(img_url, relative_path)
    return md_content

def process_md_file(md_file_path, save_dir):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    image_links = re.findall(r'!\[.*?\]\((.*?)\)', content)
    base_name = os.path.splitext(os.path.basename(md_file_path))[0]

    new_content = replace_image_links(content, image_links, base_name, save_dir)

    # Save a copy of the original file
    original_copy_path = md_file_path.replace('.md', '_original.md')
    with open(original_copy_path, 'w', encoding='utf-8') as file:
        file.write(content)

    # Save the modified file
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == "__main__":
    md_file_path = r"C:\Users\zyvis\Documents\git\hexo_visn\source\_posts\CG\Blender\ShapeKey.md"
    save_dir = r"C:\Users\zyvis\Documents\git\hexo_visn\source\assets\blog\CG\Blender"
    
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    process_md_file(md_file_path, save_dir)
    print("处理完成，图片已下载并替换链接。")