# Save uploaded files

from pathlib import Path

from config.settings import DATA_PATH


def save_uploaded_path(
    uploaded_file
):
    
    save_path = Path(DATA_PATH) / uploaded_file.name

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return str(save_path)
