import svgwrite
from cairosvg import svg2png


def create_venn_diagram():
    # Create a new SVG drawing
    dwg = svgwrite.Drawing('nlp_diagram.svg', size=('400px', '400px'))

    # Define colors
    gray = '#D3D3D3'
    blue = '#2CA02C'
    orange = '#FF7F0E'
    deep_blue = '#1F77B4'

    # Create the main circle (AI)
    dwg.add(dwg.circle(center=(200, 200), r=180, fill=gray))

    # Create ML circle
    dwg.add(dwg.circle(center=(150, 200), r=120, fill=blue))

    # Create NLP circle
    dwg.add(dwg.circle(center=(250, 200), r=120, fill=orange))

    # Create DL circle
    dwg.add(dwg.circle(center=(200, 200), r=70, fill=deep_blue))

    # Add text
    dwg.add(dwg.text('Artificial Intelligence (AI)', insert=(105, 70), fill='white',
                     style="font-size:14px; font-weight:bold"))
    dwg.add(dwg.text('Machine Learning (ML)', insert=(50, 180), fill='white', style="font-size:12px; font-weight:bold", font_family='Alegreya Sans'))
    dwg.add(dwg.text('Natural Language', insert=(280, 180), fill='white', style="font-size:12px; font-weight:bold", font_family='Alegreya Sans'))
    dwg.add(dwg.text('Processing (NLP)', insert=(280, 200), fill='white', style="font-size:12px; font-weight:bold", font_family='Alegreya Sans'))
    dwg.add(dwg.text('Deep', insert=(185, 190), fill='white', style="font-size:12px; font-weight:bold", font_family='Alegreya Sans'))
    dwg.add(dwg.text('Learning (DL)', insert=(170, 210), fill='white', style="font-size:12px; font-weight:bold", font_family='Alegreya Sans'))

    # Save the SVG file
    print("сохранение закоммичено !!!")
    # dwg.save()
    # svg_string = dwg.tostring()
    # svg2png(bytestring=svg_string, write_to='nlp_diagram.png', dpi=600)


create_venn_diagram()