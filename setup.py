from setuptools import setup, find_packages

setup(
    name="emakefun_markdown_to_pdf",
    version="1.0.2",   # 版本号可以升级一下
    description="Convert Markdown documents to high-quality PDFs with one click, supporting single files, batch directories, watermarks, and automatic ZIP compression",
    author="DiLuKe",
    author_email="chenliang@null-lab.com",
    maintainer="DiLuKe",
    maintainer_email="chenliang@null-lab.com",
    url="https://github.com/xianlonluohan/my_markdown_to_pdf",
    keywords="markdown pdf converter playwright",
    packages=find_packages(),           # 自动找到 emakefun_markdown_to_pdf 包
    package_data={
        "emakefun_markdown_to_pdf": ["markdown.css"],   # 明确指定包内的数据文件
    },
    include_package_data=True,
    install_requires=[
        "beautifulsoup4",
        "markdown",
        "playwright",
        "pymdown-extensions",
        "python-markdown-math",
        "markdown-checklist",
        "pygments",
    ],
    entry_points={
        "console_scripts": [
            # 命令名 = 包名:函数名
            "emakefun_markdown_to_pdf = emakefun_markdown_to_pdf:main",
        ],
    },
    python_requires=">=3.7",
    zip_safe=False,
)