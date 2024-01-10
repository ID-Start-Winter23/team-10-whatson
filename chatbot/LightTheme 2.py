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

button_css = """
:root[data-theme="light"] {
	--page-bg: #fff;

	--primary-text: #3C3A47;
	--muted-text: #B1B0B5;

	--logo-fill: var(--primary-text);

	--input-bg: #F5F5F6;
	--input-bg-hover: #ecebed;
	--input-border-focus: var(--muted-text);
	--input-text: var(--primary-text);
	--input-placeholder: var(--muted-text);

	--button-text: #D19361;
	--button-text-hover: #faf4ef;

    --switch-bg: #F5F5F6 !important;
    --switch-circle-bg: #FFD371;
    --switch-circle-pos: 0.22rem;
    --icon-sun: #997F44;
    --icon-moon: var(--muted-text);

}

:root[data-theme="dark"] {
	

	--primary-text: #F5F5F6;
	--muted-text: #77757E;

	--button-text: #D19361;
	--button-text-hover: #faf4ef;

    --switch-bg: #2D2C35 !important;
    --switch-circle-bg: #7190FF;
    --switch-circle-pos: 2.88rem;
    --icon-sun: var(--muted-text);
    --icon-moon: #DCE3FF;

}

:root {
    --default-border-radius: 8px;
	--default-transition: color .3s ease-in-out, background-color .3s ease-in-out, border-color .3s ease-in-out, fill .3s ease-in-out, transform .3s ease-in-out;
}

/* ================================================= */
/* General styles */
/* ================================================= */
html {
	font-size: 112.5%; /* 18px */
}

body {
	font-family: 'Poppins', sans-serif;
	line-height: 1.5;
	color: var(--primary-text);
	background-color: var(--page-bg);
	transition: var(--default-transition);
}

h1 {
	font-size: 2.4rem;
	line-height: 1.3;
	font-weight: 700;
	letter-spacing: -2px;
	margin: 2rem 0;
}

p {
	margin: 0 0 1rem;
}

small {
	font-size: 0.78rem;
	line-height: 1.4;
}

img {
	display: block;
	max-width: 100%;
	height: auto;
}



/* ================================================= */
/* Forms */
/* ================================================= */
input {
	background-color: var(--input-bg);
	border-radius: var(--default-border-radius);
	border: none;
	padding: 1.333rem;
	outline: none;
	margin-bottom: 1rem;
	width: 100%;
	line-height: 1.5;
	border: 1px solid var(--input-bg);
	color: var(--input-text);
	transition: var(--default-transition);
}

input::placeholder {
	color: var(--input-placeholder);
	transition: var(--default-transition);
}

input:hover {
	background-color: var(--input-bg-hover);
}

input:focus {
	border-color: var(--input-border-focus);
}

button {
	background-color: transparent;
	border-radius: var(--default-border-radius);
	padding: 1.333rem 2.666rem;
	color: var(--button-text);
	border: 1px solid var(--button-text);
	line-height: 1.5;
	font-weight: 700;
	width: 100%;
	white-space: nowrap;
	cursor: pointer;
	transition: var(--default-transition);
}

button:hover {
	background-color: var(--button-text);
	color: var(--button-text-hover);
}



/* ================================================= */
/* Layout */
/* ================================================= */
#main-container {
	padding: 2rem;
}



/* ================================================= */
/* Header */
/* ================================================= */
header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 5.33rem;
}

#logo svg {
	height: 3rem;
	display: block;
}

#logo-path {
	transition: var(--default-transition);
	fill: var(--logo-fill);
}

#theme-switcher {
	background-color: var(--switch-bg);
	border-radius: 50px;
	display: flex;
	align-items: center;
	gap: 1.33rem;
	cursor: pointer;
	padding: 0.66rem;
	position: relative;
    transform: var(--default-border-radius);
}

#theme-switcher::before {
	content: '';
	position: absolute;
	width: 2.22rem;
	height: 2.22rem;
	background-color: var(--switch-circle-bg);
	border-radius: 50px;
	z-index: 0;
	left: 0;
	transform: translateX(var(--switch-circle-pos));
    transition: var(--default-transition);

#theme-switcher svg {
	z-index: 1;
    transition: var(--default-transition);
}


/* ================================================= */
/* Main content */
/* ================================================= */
#hero-image {
	display: none;
}

#main-content {
	margin-bottom: 5.33rem;
}

.subtitle {
	color: var(--muted-text);
	font-weight: 300;
	text-transform: uppercase;
	letter-spacing: 1px;
	margin-bottom: 0;
	transition: var(--default-transition);
}

#notify-form {
	width: 100%;
	margin-bottom: 2rem;
}

#footnote {
	color: var(--muted-text);
	transition: var(--default-transition);
}

#mid-container {
	margin-bottom: 5.33rem;
}



/* ================================================= */
/* Footer */
/* ================================================= */
#social-icons {
	list-style: none;
	display: flex;
	align-items: center;
	gap: 1.333rem;
	margin: 0;
	padding: 0;
}

#social-icons svg {
	fill: var(--icon-socials);
	transition: var(--default-transition);
	display: block;
}

#social-icons a:hover svg {
	fill: var(--icon-socials-hover);
}



/* ================================================= */
/* 768px + */
/* ================================================= */
@media screen and (min-width: 768px) {
	#notify-form {
		display: flex;
		gap: 1rem;
	}

	input {
		width: 20rem;
		margin: 0;
	}

	button {
		width: auto;
	}
}



/* ================================================= */
/* 1200px + */
/* ================================================= */
@media screen and (min-width: 1200px) {
	#main-container {
		padding: 4rem;
	}

	#mid-container {
		display: grid;
		grid-template-columns: 1fr 1fr;
		align-items: center;
	}

	#hero-image {
		display: block;
	}
}



/* ================================================= */
/* 2000px + */
/* ================================================= */
@media screen and (min-width: 2000px) {
	#main-container {
		max-width: 100rem;
		margin: 0 auto;
	}
}
"""