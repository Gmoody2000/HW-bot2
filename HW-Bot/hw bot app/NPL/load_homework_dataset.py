from datasets import load_dataset

# Load the dataset
dataset = load_dataset("LNL/AI_homeworkcorrecting_0907")

# Get information about the dataset
print("Dataset name:", dataset.name)
print("Dataset description:", dataset.description)
print("Dataset size:", len(dataset))

# List the features in the dataset
print("Features:", dataset.features)

# Get the number of examples in each split
for split in dataset.keys():
    print("Number of examples in split", split + ":", len(dataset[split]))

# Print the first few examples in the dataset
print("First few examples:")
for example in dataset["train"][:5]:
    print(example)
