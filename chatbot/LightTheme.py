from gradio.themes.base import Base

light_css = """


:root {
    --font: 'Source Code Pro', monospace !important;
    --body-background-fill: #f4f1df !important;
    --panel-background-fill: none !important;
    --color-accent-soft: none !important;
    --color-accent: #DB7842 !important;
    --checkbox-background-color-selected: #DB7842 !important;
    --checkbox-label-background-fill-hover: #f4f1df !important;
    --checkbox-label-background-fill: #f4f1df !important;
    --checkbox-label-background-fill: #ffffff !important;
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
    background-color: #f4f1df !important;}

.user.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    color: black !important;
    background-color: #ffffff !important;
    border-color: #DB7842 !important;}

.bot.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    color: white !important;
    background: #3d405b !important;
}    

"""