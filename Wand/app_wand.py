from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display

background = "./scorebola.jpg"
filename_output = "score-output.png"
font_text = "./oswald.ttf"
filename_logo = "./logo-chelsea.png"

def Draw(skor):
    with Image(filename=background) as img_background:
        with Drawing() as context:
            context.font = font_text
            context.fill_color = Color('white')
            context.font_size = 300
            # metrics = context.get_font_metrics(img_background, skor, multiline=True)
            context.text(
                x=800,
                y=900,
                body=skor)
            context(img_background)
        with Image(filename=filename_logo) as logo:
            img_background.composite(logo, left=80, top=570)
        img_background.format = "png"
        img_background.save(filename=filename_output)
    
    return filename_output

Draw('5')

