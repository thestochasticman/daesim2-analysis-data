import gdown
import os

def download_google_drive_folder(folder_url, output_path):
  if not os.path.exists(output_path): os.makedirs(output_path)
  
  # Use gdown to download the folder
  gdown.download_folder(folder_url, quiet=False, use_cookies=False, output=output_path)
  print(f"Folder downloaded successfully to {output_path}")

if __name__ == "__main__":
  # Replace with your folder's shareable link
  folder_url = 'https://drive.google.com/drive/u/0/folders/1NnQ1_8bRx3BOgycdsPKavbrmcWK3zpdb'
  output_path = 'DAESim_forcing_data'
  if not os.path.exists(output_path): os.mkdir(output_path)
  download_google_drive_folder(folder_url, output_path)
