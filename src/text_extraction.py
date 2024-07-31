
import os
from imutils import paths
from image_processing import extract_text_from_image
from pdf_processing import extract_text_from_pdf
from utils import save_text_to_file, setup_logging
from visualizations import generate_word_cloud, plot_statistics

def main():
    setup_logging()

    image_paths = list(paths.list_images('images'))
    pdf_paths = list(paths.list_files('pdfs', validExts=('.pdf')))

    if image_paths:
        for image_path in image_paths:
            text = extract_text_from_image(image_path)
            filename = os.path.join('output', os.path.basename(image_path) + '.txt')
            save_text_to_file(text, filename)
            # Generate word cloud for each image
            wordcloud_file = os.path.join('output', os.path.basename(image_path) + '_wordcloud.png')
            generate_word_cloud(text, wordcloud_file)

    if pdf_paths:
        for pdf_path in pdf_paths:
            text = extract_text_from_pdf(pdf_path)
            filename = os.path.join('output', os.path.basename(pdf_path) + '.txt')
            save_text_to_file(text, filename)
            # Generate word cloud for each PDF
            wordcloud_file = os.path.join('output', os.path.basename(pdf_path) + '_wordcloud.png')
            generate_word_cloud(text, wordcloud_file)

    if image_paths and pdf_paths:
        combined_text = ""
        for image_path in image_paths:
            combined_text += extract_text_from_image(image_path) + "\n\n"
        for pdf_path in pdf_paths:
            combined_text += extract_text_from_pdf(pdf_path) + "\n\n"
        save_text_to_file(combined_text, 'output/combined_output.txt')
        # Generate word cloud for combined text
        wordcloud_file = os.path.join('output', 'combined_wordcloud.png')
        generate_word_cloud(combined_text, wordcloud_file)

if __name__ == "__main__":
    main()
