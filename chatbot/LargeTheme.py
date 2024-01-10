from gradio.themes.base import Base

large_css = """


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
    --text-xxs: 12px !important;
    --text-xs: 15px !important;
    --text-sm: 18px !important;
    --text-md: 20px !important;
    --text-lg: 24px !important;
    --text-xl: 28px !important;
    --text-xxl: 30px !important;
}

.dark{
    --font: 'Source Code Pro', monospace;
    --body-text-color: white;
    --body-background-fill: black;
    --panel-background-fill: none;
    --border-color-accent: #DB7842;
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
    --text-xxs: 12px !important;
    --text-xs: 15px !important;
    --text-sm: 18px !important;
    --text-md: 20px !important;
    --text-lg: 24px !important;
    --text-xl: 28px !important;
    --text-xxl: 30px !important;
    --checkbox-background-color: black;
}


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

.svelte-cmf5ev:hover {
    border-radius: 10px !important;
}

.svelte-cmf5ev {
    border-radius: 7px !important;
    font-size: large !important;
    }


"""