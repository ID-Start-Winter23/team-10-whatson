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
    set_global_service_context
)
#from llama_index.llms import OpenAI
from llama_index.text_splitter import SentenceSplitter
#from theme import CustomTheme
from LightTheme import light_css
#from DarkTheme import dark_css
#from LargeTheme import large_css

from llama_index.memory import ChatMemoryBuffer
from llama_index.llms import MockLLM
from llama_index import MockEmbedding
import tiktoken
from llama_index.callbacks import CallbackManager, TokenCountingHandler

import scraping

import time
import asyncio

# use MockLLM and MockEmbedding for testing (it's free); use OpenAI for production
llm = MockLLM(max_tokens=56)
embed_model = MockEmbedding(embed_dim=1536)

token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo-1106").encode
)

callback_manager = CallbackManager([token_counter])

storage_directory = "./storage"
print("Current time: ", str(time.time()))
# print("Last modified: ", str(os.path.getmtime(storage_directory)))

# Scraping: Extraktion der Schlagzeilen nach Themengebieten aus den RSS-Feeds der Tagesschau
top_headlines = scraping.get_rss('https://www.tagesschau.de/index~rss2.xml')

parser = SentenceSplitter()
nodes = []

# Anlegen von documents und Aufteilung in nodes
# news = Key -> (innenpolitik, europa, ...)
for article in top_headlines:
    text = f'Title: {article["title"]}\n' \
           f'Datum: {article["published"]}\n' \
           f'Inhalt: {article["description"]}\n'


    
    document = Document(
        text=text,
        metadata={'Link': article["link"]}
    )

    node = parser.get_nodes_from_documents([document])

    print(40*"#")
    print(node)

    nodes.extend(node)

# Ausgabe der Schlagzeilen über Infobox
news_text = ""
for idx, article in enumerate(top_headlines[:10]):
    news_text += f'{idx + 1}: {article["title"]}\n\n'


def check_rss_feed_and_create_index():
    # check if RSS feed was downloaded in the last 7 days
    generate_index = 0
    if not os.path.exists(storage_directory):
        generate_index = 1
    else:
        if os.path.getmtime(storage_directory) < (time.time() - 60 * 60 * 24 * 7):
            generate_index = 1
    
    if generate_index:
        # use nodes from RSS feed, create index and store it in storage folder
        index = VectorStoreIndex(nodes)
        # store it for later
        index.storage_context.persist(persist_dir="./storage")

        print(
            "Embedding Tokens Index: ",
            token_counter.total_embedding_token_count,
            "\n",
            "LLM Prompt Tokens Index: ",
            token_counter.prompt_llm_token_count,
            "\n",
            "LLM Completion Tokens Index: ",
            token_counter.completion_llm_token_count,
            "\n",
            "Total LLM Token Count Index: ",
            token_counter.total_llm_token_count,
            "\n",
        )
        token_counter.reset_counts()

    else:
        print("Index already exists.")
        storage_context = StorageContext.from_defaults(persist_dir=storage_directory)
        index = load_index_from_storage(storage_context)
    
    return index


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
    "If the user asks for a translation to another language, answer in that language.\n" 
    "Keep the answers short and simple.\n"
    "You can only answer questions that relate to your index or help the user understanding the topics of your index. \n" 
    "Tell the user in a friendly way that you can only answer questions about news if they have questions about other topics.\n"
    "Don't be afraid to ask the user to rephrase the question if you don't understand it.\n"
    "Don't repeat yourself.\n"
)

index = check_rss_feed_and_create_index()

#llm = OpenAI(model="gpt-3.5-turbo-1106", temperature=0.1)

service_context = ServiceContext.from_defaults(llm = llm, embed_model=embed_model, callback_manager=callback_manager)
set_global_service_context(service_context)

memory = ChatMemoryBuffer.from_defaults(token_limit=1024)

chat_engine = index.as_chat_engine(
    similarity_top_k = 2,
    chat_mode = "context",
    system_prompt = system_prompt,
    context_template = context,
    memory = memory,
)

# Chatbot Antwort basierend auf Nutzeranfragen und Historie, schrittweiser Aufbau des Antworttext
def response(message, history):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    answer = chat_engine.stream_chat(message)
    print("Message: ", message)
    print("History: ", history)
    print("Answer: ", answer)


    output_text = ""
    for token in answer.response_gen:
        time.sleep(0.05)
        output_text += token
        yield output_text

    print(output_text)

    print(
        "Embedding Tokens response: ",
        token_counter.total_embedding_token_count,
        "\n",
        "LLM Prompt Tokens response: ",
        token_counter.prompt_llm_token_count,
        "\n",
        "LLM Completion Tokens response: ",
        token_counter.completion_llm_token_count,
        "\n",
        "Total LLM Token Count response: ",
        token_counter.total_llm_token_count,
        "\n",
    )

    # try to reduce history size and cost
    chat_engine.reset()


example_questions=[
    'Woher stammen deine Infos?', 
    'Was ist heute passiert?',
    'Was ist in Deutschland passiert?',
    'Was ist in der Welt passiert?']



def main():
    #openai.api_key = os.environ["OPENAI_API_KEY"]

    chat_interface = gr.ChatInterface(
        fn=response,
        #theme=custom_theme,
        css=light_css,
        retry_btn=None,
        undo_btn=None,
        clear_btn=None,
        submit_btn="➤",
####### In app.py habe ich nur hier die scale=4 eingefügt, sonst ist alles andere unverändert :) #####################
        textbox=gr.Textbox(scale=4,placeholder="Frage mich etwas..."),
        examples=example_questions,
        chatbot = gr.Chatbot(
            avatar_images=["ui_elements/avatar_user.png", "ui_elements/avatar_bot.png"],
            value=[(None, "Willkommen 👋. Mein Name ist Whatson und ich versorge dich mit den aktuellsten politischen Nachrichten.")],)
        )

    # blocks
    with gr.Blocks(title="Whatson", css=light_css) as chatbot:
        with gr.Column():
            with gr.Row(equal_height=False):
                gr.Image("ui_elements/logo-avatar.png", show_label=False, show_download_button=False, scale=0.3)
            with gr.Row():
                with gr.Column(scale=0.4):
                    #### Radio-Buttons für Sprint 2
                    #gr.Radio(["Helle Ansicht", "Dunkle Ansicht", "Großer Text"], label="Modusauswahl", interactive=True, value="Helle Ansicht")
                    gr.Textbox(
                        value=news_text,
                        lines=22,
                        interactive=False,
                        label=""
                    )
                with gr.Column():
                    chat_interface.render(),

    chatbot.queue()
    chatbot.launch(inbrowser=True)


if __name__ == "__main__":
    main()