from gradio.themes.base import Base

'''
used colors:
    #DB7842 <- orange
    #f4f1df <- beige
    #3d405b <- darkblue
    #ffffff <- white
    #000000 <- black
'''

css = """


:root {
    --font: 'Source Code Pro', monospace !important;
    --body-background-fill: #f4f1df !important;
    --body-text-color-subdued: #DB7842 !important;
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
    --font: 'Source Code Pro', monospace;
    --body-text-color: white;
    --body-background-fill: black;
    --body-text-color-subdued: #DB7842;
    --panel-background-fill: none;
    --block-background-fill: #3d405b;
    --block-label-background-fill: #3d405b;
    --block-label-text-color: #3d405b;
    --block-label-border-width: 0px;
    --button-primary-text-color: white;
    --button-secondary-text-color: white;
    --button-primary-background-fill: #DB7842;
    --button-primary-background-fill-hover: #DB7842;
    --background-fill-secondary: black;
    --color-accent-soft: black;
    --text-lg: var(--text-mg);
    --checkbox-label-background-fill: #3d405b;
    --checkbox-label-background-fill-hover: #3d405b;
    --checkbox-label-background-fill-selected: black;
    --checkbox-background-color-selected: #DB7842 !important;
    --table-row-focus: none;
    --form-gap-width: none !important;
    --input-border-color: none;
    --input-background-fill: black;
    --text-lg: var(--text-mg) !important;
    --checkbox-background-color: black;
    --border-color-primary: #3d405b;
    --border-color-accent: #DB7842;
    --block-info-text-color: white;
    --button-cancel-background-fill: #DB7842;
    --button-cancel-background-fill-hover: #DB7842;
}


/* ---- ab hier klappt der Code bei HuggingFaces nicht ---- */

/* make message-box wrap around text, reduce length to 75% of textbox */
.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    display: auto !important;
    width: auto !important;
    max-width: 75% !important;}

/* make heading "Aktuelle Nachrichten" bigger */
div.svelte-e8n7p6{
    font-size: 16px;}

/* hide labels of textbox */
div.svelte-1mwvhlq:not(.float){
    visibility: hidden !important;}
.show-api.svelte-1ax1toq.svelte-1ax1toq.svelte-1ax1toq:hover {
    color: var(--button-secondary-text-color) !important;}

/* reduce line-height to fit more text within the textbox */
.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    line-height: var(--line-sm) !important;}

/* make submit-button smaller 
.primary.svelte-cmf5ev {
    flex-grow: 0.3 !important;}

/* styling of user message */
.user.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar{
    color: black !important;
    background-color: #ffffff !important;
    border-width: 1.5px !important;}

/* styling of chatbot message */
.bot.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    border-color: white !important;
    color: white !important;
    background: #3d405b !important;}    

/* submit-button */
.svelte-cmf5ev {
    border-radius: 7px !important;
    font-size: large !important; }
.svelte-cmf5ev:hover {
    background-color: #DB7842 !important;
    color: #ffffff !important;}

/* make textbox taller */
div#component-1{
    height: 500px !important}   
#component-18 {
    flex-grow: 0 !important}

/* make avatar fit in box */
img.svelte-1btp92j{
    display: inline !important}

/* align chatbot-box with other grids */
#component-3 {
    padding: 0px !important}

"""