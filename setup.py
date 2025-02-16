from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='docx_parser',
    version='0.1',
    author='liuyingduo',
    author_email='a2711985388@163.com',
    description='A package for parsing docx files and extracting text and images',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yourusername/docx_parser',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'docx-parser=docx_parser.parser:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
) 