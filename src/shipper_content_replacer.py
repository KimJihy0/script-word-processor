from docx import Document

from src import utils
from src.content_replacer import replace_iterating_paragraphs

INPUT_FILE_NAME = "LOI FOR SPLIT BILL OF LADING (THE SHIPPER’S FORMAT).docx"
OUTPUT_FILE_NAME = "LOI FOR SPLIT BILL OF LADING (THE SHIPPER’S FORMAT).docx"

TEXT_REPLACE_MAP = {
    # todo key : value
}


if __name__ == '__main__':
    input_file_path = utils.get_input_file_path(INPUT_FILE_NAME)
    doc = Document(input_file_path)

    doc = replace_iterating_paragraphs(doc, TEXT_REPLACE_MAP)

    output_file_path = utils.get_output_file_path(OUTPUT_FILE_NAME)
    doc.save(output_file_path)