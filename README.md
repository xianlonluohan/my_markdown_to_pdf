# emakefun_markdown_to_pdf

一个 Markdown 转 PDF 工具，基于 Playwright 渲染，完美支持**数学公式**、**Mermaid 图表**、**图片内嵌**、**水印**、**批量目录转换**及**自动 ZIP 打包**。一次安装，命令行即可调用。

## ✨ 功能特性

- 📄 单个 Markdown 文件转 PDF
- 📁 批量转换整个目录（保持目录结构）
- 🧮 支持 LaTeX 数学公式（`mdx_math`）
- 📊 支持 Mermaid 流程图、时序图等（通过 `mermaid.js`）
- 💧 可自定义文字水印（默认 “emakefun”），也可完全禁用
- 🗜️ 批量模式下自动将生成的 PDF 连同其他资源文件打包为 ZIP
- 🎨 内置 `markdown.css` 样式，打印排版美观（A4 纸边距优化）
- 🚀 一键安装，全局命令使用

## 📦 安装

### 安装 Python 库

使用本工具前需要先安装，可通过以下两种方式之一完成：

#### 方法一 从 Git 仓库安装（推荐）

```bash
pip install git+https://github.com/xianlonluohan/my_markdown_to_pdf.git
```

#### 方法二 本地开发安装

```bash
git clone https://github.com/xianlonluohan/my_markdown_to_pdf.git
cd my_markdown_to_pdf
pip install -e .
```


###  安装 Playwright 浏览器内核（必须）

本工具依赖 Playwright 控制 Chromium 渲染 PDF。安装完 Python 包后，还需单独安装浏览器内核：

```bash
playwright install chromium
```

### 安装推荐字体（提升中文显示效果）

转换后的PDF 默认使用 更纱黑体 (Sarasa Fixed SC) 作为中文字体，该字体开源且美观。如果系统中没有该字体，PDF 中的中文会回退到系统默认字体（可能显示为方框或样式不佳）。强烈建议安装此字体。

**安装步骤：**

1. 下载更纱黑体 (Sarasa Fixed SC)字体安装包。

    **下载地址：**

```bash
https://github.com/be5invis/Sarasa-Gothic/releases/download/v1.0.37/SarasaFixedSC-TTF-Unhinted-1.0.37.7z

```

2. 将下载后的安装包进行解压，解压后会得到多个 .ttf字体文件

3. 根据操作系统进行安装这些字体：
    - **Windows**：右键点击 .ttf 文件 → “安装” 或 “为所有用户安装”。
    - **macOS**：双击 .ttf 文件 → 点击 “安装字体”。
    - **Linux**：将 .ttf 文件复制到 ~/.local/share/fonts/ 目录，然后执行 fc-cache -fv。

4. 安装完成后重启终端（或重新打开命令提示符），转换 PDF 时即可自动使用该字体。

>如果跳过此步骤，转换后的 PDF 中的中文可能显示为系统默认字体或者是显示乱码。建议安装以获得最佳视觉效果。

## 🚀 使用方法

安装完成后，你可以直接在终端使用命令 `emakefun_markdown_to_pdf`。

```bash
emakefun_markdown_to_pdf --input <文件或目录> [--output <路径>] [--watermark TEXT] [--no-watermark] [--zip-name NAME]
```

**参数说明**

| 参数              | 类型   | 说明                                                                      |
| ----------------- | ----- | ------------------------------------------------------------------------- |
| --input           | 必选  | 输入需要转换的 Markdown 文件（.md/.markdown）或目录路径                      |
| --output          | 可选  | 转换后的输出文件或目录（单文件模式默认同目录同名 .pdf；目录模式默认同输入目录）  |
| --watermark TEXT  | 可选  | 启用水印并设置文本（默认水印文本为 emakefun）                                |
| --no-watermark    | 可选  | 完全禁用所有水印                                                            |
| --zip-name NAME   | 可选  | 批量模式下 ZIP 压缩包名称（不含扩展名），默认为 `pdf-documents`               |

**注意事项：**

1. **`--input` 参数**  
   - 指定**单个 Markdown 文件**：执行单文件转换，直接输出 PDF，**不打包 ZIP**。  
   - 指定**目录**：执行批量转换，递归处理目录下所有 `.md` / `.markdown` 文件，同时复制所有**非 Markdown 且非图片**的文件到输出目录，最后打包为 ZIP。

2. **`--output` 参数**  
   - 若值为 `xxx.pdf`（文件名）：仅当 `--input` 为单个文件时有效，输出 PDF 命名为 `xxx.pdf` 并保存在当前目录（或相对路径下）。  
   - 若值为 `yyy`（目录路径）：无论单文件还是批量转换，所有输出均放入该目录。单文件模式下自动使用原文件名。

3. **水印参数互斥**  
   `--watermark` 与 `--no-watermark` 不可同时使用。若均不指定，默认启用水印，文本为 `emakefun`。

4. **`--zip-name` 参数**  
   仅在批量模式（`--input` 为目录）下有效，单文件模式下无意义。

## 📝 使用示例

### 一、markdown单文件转换示例

1. 最简单用法（输出到同目录同名 PDF，默认水印 “emakefun”）

```bash
emakefun_markdown_to_pdf --input text.md
```
输出结果👉： 在text.md同级目录下生成 text.pdf，且水印文本为 `emakefun`。


2. 指定输出 PDF 名称（输出到同目录，自定义 PDF名称，默认水印 “emakefun”）

```bash
emakefun_markdown_to_pdf --input text.md --output out.pdf
```
输出结果👉： 在text.md同级目录下生成 out.pdf，且水印文本为 `emakefun`。


3. 指定输出 PDF 路径（自动使用原文件名，默认水印 “emakefun”）

```bash
emakefun_markdown_to_pdf --input text.md --output ./pdfs/
```
输出结果👉： 在 ./pdfs/ 目录下生成 text.pdf，且水印文本为 `emakefun`。


4. 指定输出 PDF 路径和名称（默认水印 “emakefun”）

```bash
emakefun_markdown_to_pdf --input text.md --output ./pdfs/out.pdf
```
输出结果👉： 在 ./pdfs/ 目录下生成 out.pdf，且水印文本为 `emakefun`。

5. 自定义水印文本

```bash
emakefun_markdown_to_pdf --input text.md --watermark "草稿"
```
输出结果👉： 在text.md同级目录下生成 text.pdf，且水印文本为 `草稿`。


6. 禁用水印

```bash
emakefun_markdown_to_pdf --input text.md --no-watermark
```
输出结果👉： 在text.md同级目录下生成 text.pdf，且无水印。

7. 同时指定输出路径和自定义水印

```bash
emakefun_markdown_to_pdf --input text.md --output final/report.pdf --watermark "草稿"
```
输出结果👉：  在 final/report.pdf 目录下生成 report.pdf，且水印文本为 `草稿`。

### 二、markdown文件批量转换示例

1. 最简单的批量转换（输入目录，输出到相同目录，自动打包 ZIP）

```bash
emakefun_markdown_to_pdf --input ./docs
```
输出结果👉： 扫描 ./docs 下所有 .md/.markdown 文件，生成 PDF 并与其他非 MD/非图片文件一起打包为 pdf-documents.zip，保存在 ./docs 目录下；其中pdf文件水印文本为 `emakefun`。

2. 指定输出目录（不与源文件混放）

```bash
emakefun_markdown_to_pdf --input ./docs --output ./output_pdfs
```
输出结果👉： 扫描 ./docs 下所有 .md/.markdown 文件，生成 PDF 并与其他非 MD/非图片文件一起打包为 pdf-documents.zip，保存在 ./output_pdfs 目录下；其中pdf文件水印文本为 `emakefun`。


3. 自定义 ZIP 压缩包名称（不含扩展名）

```bash
emakefun_markdown_to_pdf --input ./docs --zip-name my_docs_v1
```
输出结果👉： 扫描 ./docs 下所有 .md/.markdown 文件，生成 PDF 并与其他非 MD/非图片文件一起打包为 my_docs_v1.zip，保存在 ./docs 目录下；其中pdf文件水印文本为 `emakefun`。

4. 批量转换 + 禁用水印

```bash
emakefun_markdown_to_pdf --input ./docs --no-watermark
```
输出结果👉： 扫描 ./docs 下所有 .md/.markdown 文件，生成 PDF 并与其他非 MD/非图片文件一起打包为 my_docs_v1.zip，保存在 ./docs 目录下；其中pdf文件无水印。

5. 批量转换 + 自定义水印 + 自定义 ZIP 名称

```bash
emakefun_markdown_to_pdf --input ./docs --watermark "草稿" --zip-name my_docs_v1
```
输出结果👉： 扫描 ./docs 下所有 .md/.markdown 文件，生成 PDF 并与其他非 MD/非图片文件一起打包为 my_docs_v1.zip，保存在 ./docs 目录下；其中pdf文件水印文本为`草稿`。

6.  批量转换 + 输出到不同目录 + 自定义 ZIP 名称 + 无水印

```bash
emakefun_markdown_to_pdf --input ./docs --output ./output_pdfs --no-watermark --zip-name my_docs_v1
```
输出结果👉： 扫描 ./docs 下所有 .md/.markdown 文件，生成 PDF 并与其他非 MD/非图片文件一起打包为 my_docs_v1.zip，保存在 ./output_pdfs 目录下；其中pdf文件无水印。
