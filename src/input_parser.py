from dataclasses import dataclass,field
from typing import Optional,List
import re

@dataclass
class SlideContent:
    title: str
    bullet_points: List[str] = field(default_factory=list)
    image_path: Optional[str] = None

@dataclass
class Slide:
    layout: int
    content: SlideContent

@dataclass
class PPT:
    title: str
    slides: List[Slide] = field(default_factory=list)

def parse_text_to_ppt(input_text: str, layout_mapping: dict) -> PPT:
    prs_title = ""
    lines = input_text.split('\n')
    slides = []
    current_slide: Optional[Slide] = None
    
    slide_title_pattern = re.compile(r'^##\s+(.*?)\s+\[(.*?)\]')
    bullet_pattern = re.compile(r'^-\s+(.*)')
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    
    for line in lines:
        line = line.strip()
        # 一级标题为PPT标题
        if line.startswith('# ') and not line.startswith('##'):
            prs_title = line[2:].strip()
        # 二级标题为每页标题
        elif line.startswith('## '):
            match = slide_title_pattern.match(line)
            if match:
                title, layout_name = match.groups()
                layout_index = layout_mapping.get(layout_name.strip(),1)
                if current_slide:
                    slides.append(current_slide)
                current_slide = Slide(layout=layout_index,content=SlideContent(title=title.strip()))
        # 分点明细（bullet points）
        elif line.startswith('- ') and current_slide:
            match = bullet_pattern.match(line)
            if match:
                bullet_point = match.group(1).strip()
                current_slide.content.bullet_points.append(bullet_point)
        # 图片
        elif line.startswith('![') and current_slide:
            match = image_pattern.match(line)
            if match:
                image_path = match.group(1).strip()
                current_slide.content.image_path = image_path
        
    if current_slide:
             slides.append(current_slide)

    return PPT(title=prs_title,slides=slides) , prs_title