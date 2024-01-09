from gradio.themes.base import Base

#Hier habe ich die Zeilen: 9, 14, 15, 20, 65 geändert. Hab die Farbe ganz leicht angepasst, weil sie nicht so "rein" aussah, 
#aber kannst du gerne entscheiden, ob du es übernehmen willst -> fffbe3 ist die neue Farbe
#Und die Zeilen ab 77 sind neu, hier habe ich den hover Effekt eingefügt für den submit Button
light_css = """


:root {
    --font: 'Source Code Pro', monospace !important;
    --body-background-fill: #fffbe3 !important;
    --panel-background-fill: none !important;
    --color-accent-soft: none !important;
    --color-accent: #DB7842 !important;
    --checkbox-background-color-selected: #DB7842 !important;
    --checkbox-label-background-fill-hover: #fffbe3 !important;
    --checkbox-label-background-fill: #fffbe3 !important;
    --checkbox-label-background-fill: #ffffff !important;
    --form-gap-width: none !important;
    --input-border-width: none !important;
    --input-background-fill: #ffffff !important;
    --background-fill-secondary: #fffbe3 !important;
    --button-primary-background-fill-hover: #3d405b !important;
    --button-cancel-background-fill-hover: #DB7842 !important;
    --button-cancel-background-fill: #DB7842 !important;
    --button-cancel-text-color: black !important;
    --button-primary-background-fill: #3d405b !important;
    --button-primary-text-color: #ffffff !important;
    --border-color-primary: #ffffff !important;
    --border-color-accent-subdued: #DB7842 !important;
    --shadow-inset: none !important;
    --text-lg: var(--text-mg) !important;
}


/* ---- ab hier klappt bei HuggingFaces nicht, jedoch in VS-Code ---- */

.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    display: auto !important;
    width: auto !important;
    max-width: 75% !important;}

.compact.svelte-vt1mxs, .panel.svelte-vt1mxs{
    padding: 0px !important;}

div.svelte-1mwvhlq:not(.float){
    visibility: hidden !important;}

.show-api.svelte-1ax1toq.svelte-1ax1toq.svelte-1ax1toq:hover {
    color: var(--button-secondary-text-color) !important;}

.built-with.svelte-1ax1toq.svelte-1ax1toq.svelte-1ax1toq:hover {
    color: var(--button-secondary-text-color) !important;}

.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    line-height: var(--line-sm) !important;}

.primary.svelte-cmf5ev {
    flex-grow: 0.3 !important;}

.panel.svelte-vt1mxs {
    flex-grow: 0 !important;}

.container.svelte-tq78c3 .wrap.svelte-tq78c3 {
    background-color: #fffbe3 !important;}

.user.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    color: black !important;
    background-color: #ffffff !important;
    border-color: #DB7842 !important;}

.bot.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    color: white !important;
    background: #3d405b !important;
}    

.svelte-cmf5ev:hover {
    background-color: #db7842 !important;
    border-radius: 10px !important;
    color: #ffffff !important;
}

.svelte-cmf5ev {
    font-size: large !important;
}
.svelte-cmf5ev {
    border-radius: 7px !important;
}

"""