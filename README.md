
```markdown:README.md
# docx_parser
用来将word文件解析为AI应用方便使用的逐段文字和图像输出

## 环境要求
- Python 3.10
- Pillow >= 10.0.0

## 安装步骤

1. 创建并激活 conda 环境：
```bash
conda create -n docx_parser python=3.10
conda activate docx_parser
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 安装包：
```bash
pip install -e .
```

## 使用方法

### 命令行使用
```bash
docx-parser path/to/your/document.docx
```

### Python 代码中使用
```python
from docx_parser import main

# 解析 docx 文件
main("path/to/your/document.docx")
```

## 功能特点
- 提取 docx 文件中的文本和图片
- 保持内容的原始顺序
- 将提取的图片保存到单独的文件夹
- 提供简单的命令行接口

## 开发
运行测试：
```bash
python -m unittest tests/test_parser.py
```

## License
MIT License
```

这些更新：
1. 添加了具体的环境要求
2. 提供了完整的安装步骤，包括 conda 环境创建
3. 添加了使用说明和开发指南
4. 创建了 requirements.txt 文件指定依赖