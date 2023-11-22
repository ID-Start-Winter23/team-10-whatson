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
