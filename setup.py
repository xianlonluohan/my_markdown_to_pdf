from setuptools import setup

setup(
    name="emakefun_markdown_to_pdf",
    version="1.0.0",
    description="Convert Markdown documents to high-quality PDFs with one click, supporting single files, batch directories, watermarks, and automatic ZIP compression",
    author="DiLuKe",
    author_email="chenliang@null-lab.com",
    maintainer="DiLuKe",
    maintainer_email="chenliang@null-lab.com",
    url="https://github.com/xianlonluohan/my_markdown_to_pdf",
    keywords="markdown pdf converter playwright",
    py_modules=["emakefun_markdown_to_pdf"],   
    package_data={
        "": ["markdown.css"],                 
    },
    install_requires=[
        "beautifulsoup4",
        "markdown",
        "playwright",
        "pymdown-extensions",
        "python-markdown-math",
        "markdown-checklist",
    ],
    entry_points={
        "console_scripts": [
            "emakefun_markdown_to_pdf = emakefun_markdown_to_pdf:main",   
        ],
    },
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)