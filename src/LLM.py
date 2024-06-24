import os
from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate
import re

home = os.path.expanduser("~")
model = "Meta-Llama-3-8B-Instruct-Q6_K.gguf"
template = """Question: {question}

Answer: I am a model designed for music recommendation. 
        My answers are as concise as possible. 
        I respond in lists of songs followed by a description of the playlist and nothing else
        The list has 10 songs unless otherwise specified"""

prompt = PromptTemplate.from_template(template)

llm = LlamaCpp(
    model_path=f"{home}\Documents\Models\\{model}",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    n_ctx=2048,
    use_gpu=True,
    gpu_memory_fraction=0.9
)

llm_chain = prompt | llm


def getLLMrecommendations(question: str) -> list:
    response = (llm_chain.invoke({"question": question}))
    print(response)

    pattern = r'\d+\.\s(.*?)(?=\n|$)'
    matches = re.findall(pattern, str(response))
    return matches


if __name__ == "__main__":
    print("Running as main")
    print(getLLMrecommendations(question="Give me a list of 10 video game OSTs. Do not give any text except the relevant list. No intro or outro text"))
