import svgwrite

# Создаем новый SVG файл
dwg = svgwrite.Drawing('interdisciplinary_field.svg', profile='tiny', size=(800, 600))

# Фон
dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='lightgray'))

# Добавляем заголовок
dwg.add(dwg.text('Interdisciplinary Area',
                 insert=(200, 50),
                 font_size='30px',
                 fill='black',
                 font_family='Alegreya Sans'))

# Функция для создания эллипсов с текстом
def add_ellipse(dwg, center, r_x, r_y, fill, text, text_offset=(0, 0)):
    dwg.add(dwg.ellipse(center=center, r=(r_x, r_y), fill=fill, fill_opacity=0.5, stroke='black'))
    dwg.add(dwg.text(text, insert=(center[0] + text_offset[0], center[1] + text_offset[1]),
                     font_size='18px', fill='black', transform=f'rotate(-30 {center[0]},{center[1]})',
                     font_family='Alegreya Sans'))

# Добавляем эллипсы
add_ellipse(dwg, (250, 250), 120, 60, '#D3D3D3', 'Philosophy', (-40, 0))
add_ellipse(dwg, (350, 250), 120, 60, '#2CA02C', 'Computer Science', (-40, 0))
add_ellipse(dwg, (300, 350), 120, 60, 'yellow', 'Psychology', (-40, 0))
add_ellipse(dwg, (300, 150), 120, 60, 'purple', 'Logic', (-40, 0))
add_ellipse(dwg, (400, 350), 120, 60, '#FF7F0E', 'Linguistics', (-40, 0))
add_ellipse(dwg, (350, 300), 100, 50, '#1F77B4', 'ML', (-10, 0))

# Сохраняем SVG файл
print("dwg.save() закоммичено потому что ручная правка!!!")
# dwg.save()


