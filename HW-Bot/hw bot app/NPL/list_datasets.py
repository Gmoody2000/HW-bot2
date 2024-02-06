from datasets import list_datasets

def filter_datasets(keyword):
    all_datasets = list_datasets()
    filtered_datasets = [dataset for dataset in all_datasets if keyword.lower() in dataset.lower()]
    return filtered_datasets

if __name__ == "__main__":
    keyword = "homework"  # Change this keyword as needed
    filtered_datasets = filter_datasets(keyword)
    for dataset in filtered_datasets:
        print(dataset)
