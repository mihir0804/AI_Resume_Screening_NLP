import os

def load_text_from_file(file_path):
    """
    Loads text from a file.

    Args:
        file_path: Path to the file.

    Returns:
        The text content as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_all_from_directory(directory_path):
    """
    Loads all text files from a directory.

    Args:
        directory_path: Path to the directory.

    Returns:
        A dictionary where keys are filenames and values are the text content.
    """
    data = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            data[filename] = load_text_from_file(file_path)
    return data
