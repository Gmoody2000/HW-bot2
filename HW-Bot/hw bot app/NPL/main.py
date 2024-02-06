import spacy
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from datasets import list_datasets, load_dataset

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load pre-trained GPT-2 model and tokenizer
gpt_model = GPT2LMHeadModel.from_pretrained("gpt2")
gpt_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def preprocess_text(text):
    # Tokenization and lemmatization
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    
    # Lowercasing
    tokens_lower = [token.lower() for token in tokens]
    
    # Remove extra whitespaces
    tokens_clean = [token.strip() for token in tokens_lower if token.strip()]
    
    # Join tokens back into a single string
    processed_text = ' '.join(tokens_clean)
    
    return processed_text

def analyze_user_input(processed_text):
    # Use GPT-2 to generate response
    input_ids = gpt_tokenizer.encode(processed_text, return_tensors="pt")
    output = gpt_model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True)
    response = gpt_tokenizer.decode(output[0], skip_special_tokens=True)
    
    return response

def load_homework_dataset(dataset_name):
    # Load the dataset
    dataset = load_dataset(dataset_name)
    return dataset

if __name__ == "__main__":
    # Example usage
    # Search for education-related datasets
    education_datasets = list_datasets()
    print("Available education-related datasets:")
    for dataset in education_datasets:
        if "education" in dataset.lower():
            print(dataset)
    
    # Load a specific dataset
    dataset_name = "your_dataset_name"  # Replace with the name of the dataset you want to load
    dataset = load_homework_dataset(dataset_name)
    
    # Continue with the rest of the code...
