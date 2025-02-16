import os
import zipfile
import xml.etree.ElementTree as ET
from PIL import Image

def extract_docx(docx_path, extract_to="docx_extracted"):
    """
    Extract docx file to specified folder.
    """
    with zipfile.ZipFile(docx_path, 'r') as docx_zip:
        docx_zip.extractall(extract_to)
    print(f"[Info] .docx file extracted to: {extract_to}")

def parse_relationships(rel_path):
    """
    Parse document.xml.rels to get image rId -> media/xxx.png mapping.
    """
    namespaces = {
        'r': 'http://schemas.openxmlformats.org/package/2006/relationships'
    }
    tree = ET.parse(rel_path)
    root = tree.getroot()
    
    rels_dict = {}
    for rel in root.findall('.//r:Relationship', namespaces):
        rid = rel.get('Id')
        target = rel.get('Target')
        rels_dict[rid] = target

    return rels_dict

def extract_text_and_images(xml_path, rels_dict):
    """
    Parse word/document.xml to extract text and image placeholders in order.
    """
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    content_sequence = []
    
    for elem in root.iter():
        if elem.tag.endswith('}t'):
            if elem.text:
                content_sequence.append(elem.text)
        elif elem.tag.endswith('}drawing'):
            blip = elem.find('.//a:blip', namespaces)
            if blip is not None:
                rid = blip.get(f"{{{namespaces['r']}}}embed")
                if rid and rid in rels_dict:
                    content_sequence.append(f"[Image: {rels_dict[rid]}]")
    
    return content_sequence

def extract_images(media_folder, output_folder="extracted_images"):
    """
    Extract all images from word/media/ directory to specified folder.
    """
    if not os.path.exists(media_folder):
        print(f"[Warning] Media folder {media_folder} not found.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(media_folder):
        file_path = os.path.join(media_folder, file_name)
        if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            try:
                img = Image.open(file_path)
                output_path = os.path.join(output_folder, file_name)
                img.save(output_path)
                print(f"[Info] Extracted image: {output_path}")
            except Exception as e:
                print(f"[Error] Failed to extract {file_name}: {e}")

def main(docx_file):
    """
    Main process:
    1) Extract docx
    2) Parse document.xml.rels to get rId -> image path
    3) Get text and image placeholders from document.xml in order
    4) Extract actual image files from media directory
    5) Output organized information
    """
    extract_folder = "docx_extracted"
    extract_docx(docx_file, extract_folder)
    
    rels_path = os.path.join(extract_folder, "word", "_rels", "document.xml.rels")
    rels_dict = parse_relationships(rels_path)
    
    document_xml = os.path.join(extract_folder, "word", "document.xml")
    content_sequence = extract_text_and_images(document_xml, rels_dict)
    
    media_folder = os.path.join(extract_folder, "word", "media")
    extract_images(media_folder, output_folder="extracted_images")
    
    print("\n[Final Content Sequence]")
    for item in content_sequence:
        print(item) 