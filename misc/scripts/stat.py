from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib.ttFont import TTFont

path = "fonts/variable/InterNumeric[wght,RDNS].ttf"
font = TTFont(path)

axes = [
    dict(
        tag="wght",
        name="Weight",
        values=[
            dict(value=100, name='Thin'),
            dict(value=200, name='Extralight'),
            dict(value=300, name='Light'),
            dict(value=400, name='Regular', flags=0x2, linkedValue=700),
            dict(value=500, name='Medium'),
            dict(value=600, name='Semibold'),
            dict(value=700, name='Bold'),
            dict(value=800, name='Extrabold'),
            dict(value=900, name='Black'),
        ],
    ),
    dict(
        tag="RDNS",
        name="Roundness",
        values=[
            dict(value=-1, name='Regular'),
            dict(value=0, name='Softened', flags=0x2),
            dict(value=1, name='Rounded'),
        ],
    )
]


buildStatTable(font, axes=axes)
font.save(path)