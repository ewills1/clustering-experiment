from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import huggingface_hub

huggingface_hub.login(token="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")

#Load LLama model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-3B-Instruct", load_in_8bit=True, device_map="auto")

# Define the inference pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)  

# Function to query the model
def extract_topics(prompts):
    formatted_prompts = [
        (
            "Analyze the text below and list up to 3 key topics that summarise the text. "
            "Each topic should be fewer than 3 words. "
            "Return only the topics, separated by commas. For example, you should return only '{Topic1}, {Topic2}, {Topic3}' \n\n"
            f"Text: {prompt}\n"
            "Topics:"
        )
        for prompt in prompts
    ]

    responses = pipe(formatted_prompts, do_sample=False)  # Batch process

    topic_list = []
    for response in responses:
        generated_text = response[0]["generated_text"]
        topics_start = generated_text.find("Topics:") + len("Topics:")
        topics = generated_text[topics_start:].strip()
        topic_list.append(topics)

    return topic_list
# Example query
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    output = extract_topics(user_prompt)
    print("\nModel Response:\n", output)