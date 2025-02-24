from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

#Load LLama model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")

# Define the inference pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)  

# Function to query the model
def extract_topics(prompt):
    response = pipe(f"Read the text below and list up to 3 topics. Each topic should contain fewer than 3 words. Ensure you return three topics, separated by commas, and nothing more.{prompt}\n", 
                    max_length=50, do_sample=False)
    topic_numbers = int(response[0]["generated_text"].strip().split()[-3])  # Extract last numbers
    return topic_numbers

# Example query
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    output = extract_topics(user_prompt)
    print("\nModel Response:\n", output)