import os
import openai
import gradio as gr
import os.path
from llama_index import StorageContext, load_index_from_storage, VectorStoreIndex, SimpleDirectoryReader, download_loader
from theme import CustomTheme
from theme import custom_css

storage_directory = "./storage"

Beispielfragen=[
    ['Zeige mir aktuelle Nachrichten.'],
    ['Was sind die neusten innenpolitischen Ereignisse?'],
    ['Sage mir aktuelle außenpolitische Neuigkeiten.']]


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

def response(message, history):

    query_engine = index.as_query_engine()
    answer = query_engine.query(message)

    return str(answer)


def main():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    
    custom_theme = CustomTheme()

    chat_interface = gr.ChatInterface(
        fn=response,
        theme=custom_theme,
        retry_btn="Retry",
        undo_btn="Undo",
        clear_btn="Clear",
        textbox=gr.Textbox(placeholder="Frage mich etwas..."),
        #examples=Beispielfragen,
        css=custom_css,
        chatbot = gr.Chatbot(
            avatar_images=["ui_elements/avatar_user.png", "ui_elements/avatar_bot.png"],
            value=[(None, "Willkommen 👋. Mein Name ist Whatson und ich versorge dich mit den aktuellsten politischen Nachrichten.")],
            )
        )

    # blocks
    with gr.Blocks(theme=custom_theme, title="Whatson", css=custom_css) as chatbot:
        gr.Image("ui_elements/whatson_title.png", show_label=False, show_download_button=False, width=200)
        with gr.Row(theme=custom_theme, equal_height=False):
            with gr.Column(theme=custom_theme, scale=0.1):
                gr.Image("ui_elements/avatar_blau.png", show_label=False, show_download_button=False) # Avatar wird noch aktualisiert!!
                gr.Markdown("Hier ist eine Anleitung:")
                gr.Dropdown(["", "Innenpolitik Deutschlands", "Europa", "Amerika", "Afrika", "Asien", "Ozeanien"], label="Themenauswahl", multiselect=False), 
            chat_interface.render(),
            #gr.Examples(["Was sind die neusten Nachrichten?", "Was sind topaktuelle innenpolitische Ereignisse?", "Kannst du mir relevante außenpolitische Neuigkeiten zeigen?"], inputs=textbox)

    chatbot.launch(inbrowser=True)

if __name__ == "__main__":
    main()