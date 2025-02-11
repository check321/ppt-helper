from pptx import Presentation

def load_template(template_path: str) -> Presentation:
    prs = Presentation(template_path)
    return prs

def get_layout_mapping(prs: Presentation) -> dict:
    layout_mapping = {}
    for i, slide_layout in enumerate(prs.slide_layouts):
        layout_mapping[slide_layout.name] = i
    return layout_mapping

def print_layouts(prs: Presentation):
    for i,layout in enumerate(prs.slide_layouts):
        print(f"{i}: {layout.name}")