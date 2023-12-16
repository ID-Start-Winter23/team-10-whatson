from gradio.themes.base import Base


class CustomTheme(Base):

    def __init__(self):
        super().__init__()

        white = "#FFFFFF"
        blue = "#2D7BF0"
        grey = "#d9d9d9"


        super().set(
            body_background_fill=white,
            button_primary_background_fill=blue, #Submit-Button-Color
            button_primary_text_color=white, #Submit-Button-Text-Color
            button_secondary_background_fill=blue, #Themenauswahl-Button-Color
            button_secondary_text_color=blue, #Examples-Text-Color
            button_secondary_border_color=white, #? -> nicht genutzt?
            border_color_accent_subdued=blue, #User-Chat-Border-Color
            checkbox_label_text_color=white,
            panel_background_fill=white,
            )


custom_css = """

:root {
    --color-accent-soft: var(--border-color-primary);
    --font: ''Lora', serif';
    --border-color-accent-subdued: var(--border-color-primary);
    --body-background-fill: var(--border-color-primary);
    --panel-background-fill: none;

}

.dark{
    --font: ''Lora', serif';
}

body > gradio-app > div {
    /* background-image: url("https://i.ibb.co/hdNXYhZ/background-whatson.png"); */
}

.lg.svelte-cmf5ev {
    flex-grow: 0.3;
}

.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    display: auto;
    width: auto;
    max-width: 75%
}

.compact.svelte-vt1mxs, .panel.svelte-vt1mxs{
    padding: 0px;
}

div.svelte-1mwvhlq:not(.float){
    visibility: hidden;
}

.gallery-item.svelte-13hsdno.svelte-13hsdno.svelte-13hsdno {
    background-color: white
}

.show-api.svelte-1ax1toq.svelte-1ax1toq.svelte-1ax1toq:hover {
    color: var(--button-secondary-text-color);
}

.built-with.svelte-1ax1toq.svelte-1ax1toq.svelte-1ax1toq:hover {
    color: var(--button-secondary-text-color);
}

"""