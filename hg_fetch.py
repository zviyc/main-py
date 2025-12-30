import requests as Req
from json import dumps

# 0.0.1 12-30-2025
# Launch to process JSON data from server
def fetch_hg(URL: str, file_name: str) -> object:
    """
    Fetch and save Hugging Face dataset rows to a local JSON file.

    Args:
        url: Hugging Face API endpoint for dataset rows.
        file_name: Target output path (JSON).
    output: 
        object {}
    """
    get = Req.get(URL)

    if get.status_code == 200:
        data: object = get.json()
        with open(file_name, "w") as file:
            file.write(dumps(data, indent=3, sort_keys=True))

        # Message successful
        print(f"Your data is already saved in the file {file_name} in JSON format!")
    elif get.status_code == 404:
        print("Failed to fetch the server with status 404!")
    else:
        pass

if __name__ == "__main__":
    fetch_hg("https://datasets-server.huggingface.co/rows?dataset=nvidia%2FNemotron-Pretraining-Dataset-sample&config=Nemotron-CC-Diverse-QA&split=train&offset=0&length=100", "Nemotron-CC-Diverse-QA.json")

