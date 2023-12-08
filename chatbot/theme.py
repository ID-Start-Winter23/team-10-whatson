from gradio.themes.base import Base


class CustomTheme(Base):

    def __init__(self):
        super().__init__()

        white = "#FFFFFF"
        blue = "#2D7BF0"
        grey = "#d9d9d9"


        super().set(
            body_background_fill=white,
            button_primary_background_fill=blue,
            button_primary_text_color=white,
            button_secondary_background_fill=grey,
            button_secondary_text_color=blue,
            button_secondary_border_color=white,
            color_accent_soft=white,
            border_color_accent_subdued=blue,)


custom_css = """
body > gradio-app > div {
    background-image: url("https://i.ibb.co/G9pHv6k/tiled-background.png");
    background-size: 200px 117px;
    padding: 0;
    margin: 0;
}

#component-3 > div {
    background-image: none;
    background-color: white;
}

#component-3 > div > div{
    background-image: none;
    background-color: white;
}

#component-1 > div.svelte-1ed2p3z > div > span > h1 {
    visibility: hidden;
}

#component-1 > div.svelte-1ed2p3z > div {
    background-image: url(https://i.ibb.co/LYnNtBV/Der-KI-Kurier-Upload.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: 100px 100px;
}
"""