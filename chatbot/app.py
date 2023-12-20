import os
import openai
import gradio as gr
import os.path
from llama_index import (
    Document,
    ServiceContext, 
    load_index_from_storage, 
    StorageContext,
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    download_loader, 
    set_global_service_context
)
from llama_index.llms import OpenAI
from llama_index.text_splitter import SentenceSplitter
from theme import CustomTheme
from theme import custom_css

import scraping

import time
import asyncio


storage_directory = "./storage"


# check if storage already exists
if not os.path.exists(storage_directory):
# load the documents and create the index
    documents = SimpleDirectoryReader(input_dir="data").load_data()
    index = VectorStoreIndex.from_documents(documents)
# store it for later
    index.storage_context.persist(persist_dir=storage_directory)
else:
# load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=storage_directory)
    index = load_index_from_storage(storage_context)


# Scraping: Extraktion der Schlagzeilen nach Themengebieten aus den RSS-Feeds der Tagesschau
top_headlines_innenpolitik = scraping.get_rss('https://www.tagesschau.de/inland/innenpolitik/index~rss2.xml')
top_headlines_europa = scraping.get_rss('https://www.tagesschau.de/ausland/europa/index~rss2.xml')
top_headlines_amerika = scraping.get_rss('https://www.tagesschau.de/ausland/amerika/index~rss2.xml')
top_headlines_afrika = scraping.get_rss('https://www.tagesschau.de/ausland/afrika/index~rss2.xml')
top_headlines_asien = scraping.get_rss('https://www.tagesschau.de/ausland/asien/index~rss2.xml')
top_headlines_ozeanien = scraping.get_rss('https://www.tagesschau.de/ausland/ozeanien/index~rss2.xml')

# Sammeln aller Schlagzeilen im Dictionary top_news
top_news = {
    "innenpolitik": top_headlines_innenpolitik,
    "europa": top_headlines_europa,
    "amerika": top_headlines_amerika,
    "afrika": top_headlines_afrika,
    "asien": top_headlines_asien,
    "ozeanien": top_headlines_ozeanien
}

parser = SentenceSplitter()
nodes = []

# Anlegen von documents und Aufteilung in nodes
# news = Key -> (innenpolitik, europa, ...)
for topic in top_news:
    top_headlines = top_news[topic]
    for article in top_headlines:
        text = f'Title: {article["title"]}\n' \
               f'Datum: {article["published"]}\n' \
               f'Inhalt: {article["description"]}\n'

        document = Document(
            text=text,
            metadata={
                'Themenauswahl': topic,
                'Link': article["link"]
            }
        )

        node = parser.get_nodes_from_documents([document])

        print(40*"#")
        print(node)

        nodes.extend(node)

index = VectorStoreIndex(nodes)

llm = OpenAI(model="gpt-4-1106-preview", temperature=0.1)
service_context = ServiceContext.from_defaults(llm = llm)

set_global_service_context(service_context)

# Prompt Engineering: Chatbot Charakter, Tone-of-Voice
system_prompt = (
    "You are a neutral news reporter."
    "If the provided context is not helpful you still answer the question."
)

context = (
    "Context information is below. \n"
    "--------------------\n"
    "{context_str}\n"
    "--------------------\n"
    "Respond about news based on context only. \n"
    "If the user asks about general information about a news topic use ur general knowledge to answer the question!\n"    
    "Greet the user in a friendly way.\n"
    "Always keep the user on a first-name basis and address the user informally.\n"
    "Answer always in German and in a friendly, informative matter.\n"
    "Keep the answers short and simple.\n"
    "Tell the user in a friendly way that you can only answer questions about political news if they have questions about other topics.\n"
    "Don't be afraid to ask the user to rephrase the question if you don't understand it.\n"
    "Don't repeat yourself.\n"
)

chat_engine = index.as_chat_engine(
    similarity_top_k = 5,
    chat_mode = "context",
    system_prompt = system_prompt,
    context_template = context,
)

# Chatbot Antwort basierend auf Nutzeranfragen und Historie, schrittweiser Aufbau des Antworttext
def response(message, history):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    chat_history = chat_engine.chat_history
    answer = chat_engine.stream_chat(message, chat_history)

    output_text = ""
    for token in answer.response_gen:
        time.sleep(0.1)
        output_text += token
        yield output_text


example_questions=[
    ['Woher stammen deine Infos?']]

# Themenauswahl über Dropdown Menü
def dropdown_selection(selection):

    if selection == "Innenpolitik Deutschlands":
        top_headlines = scraping.get_rss('https://www.tagesschau.de/inland/innenpolitik/index~rss2.xml')
    elif selection == "Europa":
        top_headlines = scraping.get_rss('https://www.tagesschau.de/ausland/europa/index~rss2.xml')
    elif selection == "Amerika":
        top_headlines = scraping.get_rss('https://www.tagesschau.de/ausland/amerika/index~rss2.xml')
    elif selection == "Afrika":
        top_headlines = scraping.get_rss('https://www.tagesschau.de/ausland/afrika/index~rss2.xml')
    elif selection == "Asien":
        top_headlines = scraping.get_rss('https://www.tagesschau.de/ausland/asien/index~rss2.xml')
    elif selection == "Ozeanien":
        top_headlines = scraping.get_rss('https://www.tagesschau.de/ausland/ozeanien/index~rss2.xml')
    else:
        top_headlines = []

    output_text = ""
    for idx, article in enumerate(top_headlines):
        output_text += f'{idx + 1}: {article["title"]}\n\n'

    if output_text == "":
        output_text = "Du kannst mich zu Nachrichten über die Themen ... befragen"

    return output_text


def main():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    
    custom_theme = CustomTheme()

    chat_interface = gr.ChatInterface(
        fn=response,
        theme=custom_theme,
        css=custom_css,
        retry_btn=None,
        undo_btn=None,
        clear_btn=None,
        textbox=gr.Textbox(placeholder="Frage mich etwas..."),
        examples=example_questions,
        chatbot = gr.Chatbot(
            avatar_images=["ui_elements/avatar_user.png", "ui_elements/avatar_bot.png"],
            value=[(None, "Willkommen 👋. Mein Name ist Whatson und ich versorge dich mit den aktuellsten politischen Nachrichten.")],)
        )

    # blocks
    with gr.Blocks(theme=custom_theme, title="Whatson", css=custom_css) as chatbot:
        with gr.Column():
            with gr.Row(equal_height=False):
                gr.Image("ui_elements/logo-avatar.png", show_label=False, show_download_button=False, scale=0.3)
            with gr.Row():
                with gr.Column(scale=0.4):
                    gr.Radio(["Heller-Modus", "Dunkler-Mode", "Leihter-Mode"], label="Modusauswahl")
                    dropdown = gr.Dropdown(["", "Innenpolitik Deutschlands", "Europa", "Amerika", "Afrika", "Asien", "Ozeanien"], label="Themenauswahl", multiselect=False)

                    top_news = gr.Textbox(
                        lines=15,
                        interactive=False,
                        label="",
                        value="Du kannst mich zu Nachrichten der auswählbaren Themen befragen"
                    )

                    dropdown.change(fn=dropdown_selection, inputs=dropdown, outputs=top_news)

                with gr.Column():
                    chat_interface.render(),

    chatbot.queue()
    chatbot.launch(inbrowser=True)


if __name__ == "__main__":
    main()