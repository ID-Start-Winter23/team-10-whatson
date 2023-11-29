from gradio.themes.base import Base
import gradio as gr

class CustomTheme(Base):

    def __init__(self):
        super().__init__(
            font=[gr.themes.GoogleFont("Lora Regular")])

        white = "#FFFFFF"
        lightblue = "#2D7BF0"
        lightgray = "#D9D9D9"

        new_background = "background_test.png"
        super().set(
            body_background_fill=new_background,
            button_primary_background_fill=lightblue,
            button_primary_text_color=white,
            button_secondary_background_fill=lightgray,
            button_secondary_text_color=white,
            button_secondary_border_color=white,
            color_accent_soft=lightblue,
            border_color_accent_subdued=lightblue,
        )

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