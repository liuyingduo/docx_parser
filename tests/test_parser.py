import os
import unittest
from docx_parser import extract_docx, parse_relationships, extract_text_and_images

class TestDocxParser(unittest.TestCase):
    
    def setUp(self):
        # Create a test docx file or use a sample one
        self.test_docx = "test.docx"
        self.extract_folder = "docx_extracted"
    
    def test_extract_docx(self):
        # Test if extraction works
        if os.path.exists(self.test_docx):
            extract_docx(self.test_docx, self.extract_folder)
            self.assertTrue(os.path.exists(self.extract_folder))
    
    def test_parse_relationships(self):
        # Test relationship parsing
        if os.path.exists(self.test_docx):
            rels_path = os.path.join(self.extract_folder, "word", "_rels", "document.xml.rels")
            if os.path.exists(rels_path):
                rels_dict = parse_relationships(rels_path)
                self.assertIsInstance(rels_dict, dict)
    
    def test_extract_text_and_images(self):
        # Test content extraction
        if os.path.exists(self.test_docx):
            document_path = os.path.join(self.extract_folder, "word", "document.xml")
            if os.path.exists(document_path):
                content = extract_text_and_images(document_path, {})
                self.assertIsInstance(content, list)

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.extract_folder):
            import shutil
            shutil.rmtree(self.extract_folder)

if __name__ == '__main__':
    unittest.main() 