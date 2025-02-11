from template_manager import load_template,get_layout_mapping,print_layouts
from input_parser import parse_text_to_ppt
from ppt_generator import generate_presentation

def main():
    
    input_text = """
    # ChatPPT_Demo

    ## ChatPPT Demo [Title]

    ## 2024 业绩概述 [Title and Content]
    - 总收入增长15%
    - 市场份额扩大至30%

    ## 业绩图表 [Title and Picture 1]
    ![业绩图表](images/performance_chart.png)

    ## 新产品发布 [Title and 2 Column]
    - 产品A: 特色功能介绍
    - 产品B: 市场定位
    ![未来增长](images/forecast.png)
    """
    template_path = "template/master_template.pptx"
    prs = load_template(template_path=template_path)
    
    print("Load template successfully: ")
    print_layouts(prs)
    
    layout_mapping = get_layout_mapping(prs)
    
    ppt, prs_title = parse_text_to_ppt(input_text,layout_mapping)
    output_pptx = f"outputs/{prs_title}.pptx"
    generate_presentation(ppt,template_path,output_pptx)
    
if __name__ == "__main__":
    main()