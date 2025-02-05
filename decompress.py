import zipfile
import os

def decompress_zips_to_one_folder(zip_folder, extract_to=None):
    """
    Extracts all ZIP files in a given folder into a single extraction directory.
    
    :param zip_folder: Path to the folder containing ZIP files.
    :param extract_to: Path where all files will be extracted. Defaults to `zip_folder/extracted/`.
    """
    if extract_to is None:
        extract_to = os.path.join(zip_folder, "extracted")

    os.makedirs(extract_to, exist_ok=True)

    # Iterate through all ZIP files in the folder
    for file in os.listdir(zip_folder):
        if file.endswith(".zip"):
            zip_path = os.path.join(zip_folder, file)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)  # Extract all files to the same folder

            print(f"Extracted: {file} -> {extract_to}")

# Example Usage
decompress_zips_to_one_folder("path/to/folder")

# Example Usage
decompress_zips_to_one_folder(
  'FAST_results/Rutherglen_1971_test/compressed_parameters', 
  'FAST_results/Rutherglen_1971_test/parameters' )
