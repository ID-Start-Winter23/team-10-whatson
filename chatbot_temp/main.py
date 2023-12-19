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
from llama_index.text_splitter import SentenceSplitter  # woher SentenceSplitter importieren????? 
#from llama_index.node_parser import SentenceSplitter
from theme import CustomTheme
from theme import custom_css
# für scraping
import requests
from bs4 import BeautifulSoup
import scraping

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

# Scraping
top_headlines_innenpolitik = scraping.get_rss('https://www.tagesschau.de/inland/innenpolitik/index~rss2.xml')

### News Content
documents = []
for article in top_headlines_innenpolitik:
    print(article)
    text = f'Title: {article["title"]}\n' \
           f'Datum: {article["published"]}\n' \
           f'Inhalt: {article["description"]}\n\n\n'
    print(text)

    document = Document(text=text)
    documents.append(document)

parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

index = VectorStoreIndex(nodes)

llm = OpenAI(model="gpt-4", temperature=0.1)
service_context = ServiceContext.from_defaults(llm = llm)

set_global_service_context(service_context)

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
    "For questions about general information about the news, answer with your general knowledge. \n "    
    "Greet the user in a friendly way.\n"
    "Always keep the user on a first-name basis.\n"
    "Answer always in German and in a friendly, informative matter.\n"
    "Keep the answers short and simple.\n"
    "Tell the user in a friendly way that you can only answer questions about political news if they have questions about other topics.\n"
    "If the user asks a question that you cannot answer, tell them that you cannot answer the question and that they should try asking something else.\n"
    "Don't be afraid to ask the user to rephrase the question if you don't understand it.\n"
    "Don't repeat yourself.\n"
)

chat_engine = index.as_chat_engine(
    similarity_top_k = 5,
    chat_mode = "context",
    system_prompt = system_prompt,
    context_template = context,
    service_context = service_context,
)
###

def response(message, history):

    query_engine = index.as_query_engine()
    answer = query_engine.query(message)

    return str(answer)

example_questions=[
    ['Woher stammen deine Infos?']]

def main():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    
    custom_theme = CustomTheme()

    chat_interface = gr.ChatInterface(
        fn=response,
        theme=custom_theme,
        retry_btn=None,
        undo_btn=None,
        clear_btn=None,
        textbox=gr.Textbox(placeholder="Frage mich etwas..."),
        examples=example_questions,
        css=custom_css,
        chatbot = gr.Chatbot(
            avatar_images=["ui_elements/avatar_user.png", "ui_elements/avatar_bot.png"],
            value=[(None, "Willkommen 👋. Mein Name ist Whatson und ich versorge dich mit den aktuellsten politischen Nachrichten.")],)
        )

    # blocks
    with gr.Blocks(theme=custom_theme, title="Whatson", css=custom_css) as chatbot:
        gr.Image("ui_elements/whatson_title.png", show_label=False, show_download_button=False, width=200)
        with gr.Row(theme=custom_theme, equal_height=False):
            with gr.Column(theme=custom_theme, scale=0.1):
                gr.Image("ui_elements/avatar_blau.png", show_label=False, show_download_button=False)
                gr.Markdown("Hier ist eine Anleitung:")
                gr.Dropdown(["", "Innenpolitik Deutschlands", "Europa", "Amerika", "Afrika", "Asien", "Ozeanien"], label="Themenauswahl", multiselect=False), 
            chat_interface.render(),
            
    chatbot.launch(inbrowser=True)

if __name__ == "__main__":
    main()