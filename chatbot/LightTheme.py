from gradio.themes.base import Base

'''
used colors:
    #DB7842 <- orange
    #f4f1df <- beige
    #3d405b <- darkblue
    #ffffff <- white
    #000000 <- black
'''

light_css = """


:root {
    --font: 'Source Code Pro', monospace !important;
    --body-background-fill: #f4f1df !important;
    --block-title-text-color: black;
    --block-info-text-color: black;
    --block-label-text-color: black;
    --panel-background-fill: none !important;
    --color-accent-soft: none !important;
    --color-accent: #DB7842 !important;
    --checkbox-background-color-selected: #DB7842 !important;
    --checkbox-label-background-fill-hover: #f4f1df !important;
    --checkbox-label-background-fill: #f4f1df !important;
    --checkbox-background-color: #3d405b;
    --form-gap-width: none !important;
    --input-border-width: none !important;
    --input-background-fill: #ffffff !important;
    --background-fill-secondary: #f4f1df !important;
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


.dark {
    --font: 'Source Code Pro', monospace !important;
    --body-background-fill: #f4f1df !important;
    --panel-background-fill: none !important;
    --block-background-fill: white;
    --block-title-text-color: black;
    --block-info-text-color: black;
    --block-label-text-color: black;
    --body-text-color: black;
    --color-accent-soft: none !important;
    --color-accent: #DB7842 !important;
    --checkbox-background-color-selected: #DB7842 !important;
    --checkbox-label-background-fill-hover: #f4f1df !important;
    --checkbox-label-background-fill: #f4f1df !important;
    --form-gap-width: none !important;
    --input-border-width: none !important;
    --input-background-fill: #ffffff !important;
    --background-fill-secondary: #f4f1df !important;
    --button-primary-background-fill-hover: #3d405b !important;
    --button-cancel-background-fill-hover: #DB7842 !important;
    --button-cancel-background-fill: #DB7842 !important;
    --button-cancel-text-color: black !important;
    --button-primary-background-fill: #3d405b !important;
    --button-primary-text-color: #ffffff !important;
    --border-color-primary: #ffffff !important;
    --button-secondary-text-color: black;
    --border-color-accent: #DB7842 !important;
    --border-color-accent-subdued: #DB7842 !important;
    --shadow-inset: none !important;
    --text-lg: var(--text-mg) !important;
}


/* ---- ab hier klappt der Code bei HuggingFaces nicht ---- */

.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    display: auto !important;
    width: auto !important;
    max-width: 75% !important;}

.compact.svelte-vt1mxs, .panel.svelte-vt1mxs{
    padding: 0px !important;}

div.svelte-e8n7p6{
    font-size: 16px;
}

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
    background-color: #fffbe3 !important;
}

.user.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    color: black !important;
    background-color: #ffffff !important;
    border-color: #DB7842 !important;}

.bot.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    color: white !important;
    background: #3d405b !important;
}    

.svelte-cmf5ev:hover {
    background-color: #DB7842 !important;
    border-radius: 10px !important;
    color: #ffffff !important;
}

.svelte-cmf5ev {
    border-radius: 7px !important;
    font-size: large !important;

"""