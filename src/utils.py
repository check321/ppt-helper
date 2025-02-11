from pptx import Presentation

def remove_all_slides(prs: Presentation):
    xml_slides = prs.slides._sldIdLst
    slides = list(xml_slides)
    for slide in slides:
        xml_slides.remove(slide)
    print("remove all the slides.")