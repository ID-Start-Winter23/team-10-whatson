from gradio.themes.base import Base


class CustomTheme(Base):

    def __init__(self):
        super().__init__()

        beige = "#f4f1df"
        red = "#DB7842"
        white = "#ffffff"
        blue = "#3d405b"


        super().set(
            button_primary_background_fill=blue, #Submit-Button-Color
            button_primary_text_color=white, #Submit-Button-Text-Color
            button_secondary_background_fill=white, #Themenauswahl-Button-Color
            button_secondary_text_color=blue, #Examples-Text-Color
            button_secondary_border_color=beige, #? -> nicht genutzt?
            checkbox_label_text_color=beige,
            color_accent_soft=blue,
            background_fill_primary=white,
            checkbox_label_padding=None,
            input_background_fill=white,
            )


custom_css = """

:root {
    --font: 'Source Code Pro', monospace;
    --border-color-accent-subdued: var(--border-color-primary);
    --body-background-fill: #f4f1df;
    --panel-background-fill: none;
}

.dark{
    --font: 'Source Code Pro', monospace;
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

.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    line-height: var(--line-sm);
}

.user.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    color: var(--button-secondary-text-color);
}

.primary.svelte-cmf5ev {
    flex-grow: 0.3 !important;
}

.secondary.svelte-cmf5ev{
    background: #DB7842;
    flex-grow: 0.3;
    color: #ffffff;
}

.secondary.svelte-cmf5ev:hover, .secondary[disabled].svelte-cmf5ev{
    background: #DB7842;
    flex-grow: 0.3;
    color: rgba(0, 0, 0, 10);
}

"""