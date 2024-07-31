import os
import logging

def save_text_to_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

def setup_logging():
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(filename='logs/extraction.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
