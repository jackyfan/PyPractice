import os
from PyPDF2 import PdfReader, PdfWriter
from typing import List, Tuple


def validate_page_ranges(ranges: List[str], total_pages: int) -> List[Tuple[int, int]]:
    """
    验证并解析页码范围

    Args:
        ranges: 页码范围字符串列表，如["1-500", "501-749"]
        total_pages: PDF文件的总页数

    Returns:
        解析后的页码范围元组列表，转换为0基索引

    Raises:
        ValueError: 当页码范围无效时
    """
    parsed_ranges = []

    for r in ranges:
        # 处理单页情况
        if '-' not in r:
            try:
                page = int(r)
                if page < 1 or page > total_pages:
                    raise ValueError(f"页码 {page} 超出范围（1-{total_pages}）")
                parsed_ranges.append((page - 1, page - 1))  # 转换为0基索引
            except ValueError:
                raise ValueError(f"无效的页码格式: {r}")
        # 处理范围情况
        else:
            parts = r.split('-')
            if len(parts) != 2:
                raise ValueError(f"无效的页码范围格式: {r}")

            try:
                start = int(parts[0])
                end = int(parts[1])
            except ValueError:
                raise ValueError(f"无效的页码格式: {r}")

            if start < 1 or end < start or end > total_pages:
                raise ValueError(f"无效的页码范围: {r}（有效范围1-{total_pages}）")

            # 转换为0基索引
            parsed_ranges.append((start - 1, end - 1))

    return parsed_ranges


def split_pdf(input_path: str, output_dir: str, page_ranges: List[Tuple[int, int]]) -> None:
    """
    按指定页码范围拆分PDF文件

    Args:
        input_path: 输入PDF文件路径
        output_dir: 输出目录
        page_ranges: 页码范围元组列表（0基索引）
    """
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 读取PDF
    with open(input_path, 'rb') as f:
        reader = PdfReader(f)
        total_pages = len(reader.pages)

        print(f"成功读取PDF文件，共 {total_pages} 页")

        # 处理每个页码范围
        for i, (start, end) in enumerate(page_ranges, 1):
            writer = PdfWriter()

            # 添加指定范围的页面
            for page_num in range(start, end + 1):
                writer.add_page(reader.pages[page_num])

            # 生成输出文件名
            input_filename = os.path.splitext(os.path.basename(input_path))[0]
            output_filename = f"{input_filename}_pages_{start + 1}-{end + 1}.pdf"  # 转回1基索引显示
            output_path = os.path.join(output_dir, output_filename)

            # 写入输出文件
            with open(output_path, 'wb') as out_f:
                writer.write(out_f)

            print(f"已生成: {output_path}（包含 {end - start + 1} 页）")


def main():
    # 固定参数设置 - 在这里修改为你的需求
    input_path = "C:\\Users\\30046\\Downloads\\test.pdf"  # 输入PDF文件路径
    page_ranges = ["1-500", "501-749"]  # 页码范围
    output_dir = "C:\\Users\\30046\\Downloads\\"  # 输出目录

    # 验证输入文件
    if not os.path.isfile(input_path):
        print(f"错误: 输入文件不存在 - {input_path}")
        return

    if not input_path.lower().endswith('.pdf'):
        print(f"错误: 输入文件必须是PDF格式 - {input_path}")
        return

    # 获取总页数
    try:
        with open(input_path, 'rb') as f:
            reader = PdfReader(f)
            total_pages = len(reader.pages)
    except Exception as e:
        print(f"读取PDF文件时出错: {str(e)}")
        return

    # 验证页码范围
    try:
        parsed_ranges = validate_page_ranges(page_ranges, total_pages)
    except ValueError as e:
        print(f"页码范围错误: {str(e)}")
        return

    # 执行拆分
    try:
        split_pdf(input_path, output_dir, parsed_ranges)
        print("PDF拆分完成！")
    except Exception as e:
        print(f"拆分PDF时出错: {str(e)}")


if __name__ == "__main__":
    main()
