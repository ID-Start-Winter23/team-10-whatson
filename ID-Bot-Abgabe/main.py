import os
import openai
import gradio as gr
import os.path
from llama_index import StorageContext, load_index_from_storage, VectorStoreIndex, SimpleDirectoryReader, download_loader
from theme import CustomTheme

storage_directory = "./storage"
custom_css = """
body > gradio-app > div {
    background-image: url("https://i.ibb.co/G9pHv6k/tiled-background.png");
    background-size: 200px 117px;
    padding: 0;
    margin: 0;
}

#component-3 > div {
    background-image: none;
    background-color: white;
}

#component-3 > div > div{
    background-image: none;
    background-color: white;
}

#component-1 > div.svelte-1ed2p3z > div > span > h1 {
    visibility: hidden;
}

#component-1 > div.svelte-1ed2p3z > div {
    background-image: url(https://i.ibb.co/LYnNtBV/Der-KI-Kurier-Upload.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: 100px 100px;
}
"""


def response(message, history):
    # check if storage already exists
    if not os.path.exists(storage_directory):
    # load the documents and create the index
        documents = SimpleDirectoryReader(input_dir="data").load_data()
        index = VectorStoreIndex.from_documents(documents)
    # store it for later
        index.storage_context.persist(storage_directory)
    else:
    # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=storage_directory)
        index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    answer = query_engine.query(message)

    return str(answer)


def main():
    openai.api_key = os.environ["OPENAI_API_KEY"]

    custom_theme = CustomTheme()

    chatbot = gr.ChatInterface(
        title="Pressed Bot",
        fn=response,
        retry_btn=None,
        undo_btn=None,
        theme=custom_theme,
        css=custom_css
    )
    chatbot.launch(inbrowser=True)


if __name__ == "__main__":
    main()
