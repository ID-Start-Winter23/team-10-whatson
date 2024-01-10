from gradio.themes.base import Base

'''
used colors:
    #DB7842 <- orange
    #3d405b <- darkblue
'''

dark_css = """

:root {
    --font: 'Source Code Pro', monospace;
    --body-text-color: white;
    --body-background-fill: black;
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
}

.dark {
    --font: 'Source Code Pro', monospace;
    --body-text-color: white;
    --body-background-fill: black;
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
}


.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    display: auto !important;
    width: auto !important;
    max-width: 75% !important;}

.compact.svelte-vt1mxs, .panel.svelte-vt1mxs{
    padding: 0px !important;}

.message.svelte-1pjfiar.svelte-1pjfiar.svelte-1pjfiar {
    line-height: var(--line-sm) !important;}

.primary.svelte-cmf5ev {
    flex-grow: 0.3 !important;}

.panel.svelte-vt1mxs {
    flex-grow: 0 !important;}

.input.svelte-1f354aw.svelte-1f354aw:disabled, textarea.svelte-1f354aw.svelte-1f354aw:disabled {
    background: black;
}

.svelte-cmf5ev:hover {
    background-color: #DB7842 !important;
    border-radius: 10px !important;
}

.svelte-cmf5ev {
    border-radius: 7px !important;
    font-size: large !important;


"""