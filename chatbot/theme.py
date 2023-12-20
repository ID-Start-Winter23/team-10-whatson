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
            button_secondary_border_color=red, #? -> nicht genutzt?
            checkbox_label_text_color=beige, #
            color_accent=red, # Beim Generieren der Nachricht wird Border diese Farbe
            color_accent_soft=red, # z.B. Buttons-Hover, Nutzer-Background-Farbe
            background_fill_primary=white, # wird nicht genutzt?
            background_fill_secondary=blue, # ?
            checkbox_label_padding=None, # Padding beim Dropdown verkleinert
            input_background_fill=white, #
            body_text_color=blue, #
            )


custom_css = """


:root {
    --font: 'Source Code Pro', monospace;
    --border-color-accent-subdued: var(--neutral-200);
    --border-color-accent: var(--neutral-200);
    --body-background-fill: #f4f1df;
    --panel-background-fill: none;
}

.dark{
    --font: 'Source Code Pro', monospace;
}

/* Message-Form und Länge an Text angepasst */
.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    display: auto;
    width: auto;
    max-width: 75%
}

/* Dropdown Padding verkleinert */
.compact.svelte-vt1mxs, .panel.svelte-vt1mxs{
    padding: 0px;
}

/* Label Chatbot Textbox hidden */
div.svelte-1mwvhlq:not(.float){
    visibility: hidden;
}

.show-api.svelte-1ax1toq.svelte-1ax1toq.svelte-1ax1toq:hover {
    color: var(--button-secondary-text-color);
}

/* ? */
.built-with.svelte-1ax1toq.svelte-1ax1toq.svelte-1ax1toq:hover {
    color: var(--button-secondary-text-color);
}

/* Text angepasst */
.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    line-height: var(--line-sm);
}

/* Submit-Button */
.primary.svelte-cmf5ev {
    flex-grow: 0.3 !important;
}

/* ? */
.panel.svelte-vt1mxs {
    flex-grow: 0 !important;
}

/* Themen aus Dropdown Background Color */
.container.svelte-tq78c3 .wrap.svelte-tq78c3 {
    background-color: #f4f1df;
}

/* Chatbot Message Color */
.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    color: white;
}


.user.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    color: black;
    background-color: #ffffff;
    border-color: #DB7842;
}

"""