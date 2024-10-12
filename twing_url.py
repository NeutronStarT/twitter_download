import re

def get_origin_url(img_url):
    # 定义正则表达式模式
    pattern = r'https://pbs\.twimg\.com/media/([a-zA-Z0-9\-_]+)(\?format=|.)(jpg|jpeg|png|webp)'
    
    # 使用正则表达式搜索匹配项
    match = re.match(pattern, img_url)
    
    if not match:
        return False
    
    # 如果匹配成功，提取相关组
    media_id = match.group(1)
    format_part = match.group(2)
    extension = match.group(3)
    
    # 如果是 webp 格式，转换为 jpg
    if extension == 'webp':
        extension = 'jpg'
    
    # 检查是否已经有 'name=orig' 参数，如果没有，则添加
    if format_part == '?format=' or 'name=orig' not in img_url:
        return f'https://pbs.twimg.com/media/{media_id}.{extension}?name=orig'
    else:
        return False