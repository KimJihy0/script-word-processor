from docx import Document

from src import utils
from src.content_replacer import replace_iterating_paragraphs

INPUT_FILE_NAME = "LOI FOR SPLIT BILL OF LADING (THE CONSIGNEE’S FORMAT).docx"
OUTPUT_FILE_NAME = "LOI FOR SPLIT BILL OF LADING (THE CONSIGNEE’S FORMAT).docx"

TEXT_REPLACE_MAP = {
    '[insert name of vessel, such as "M/V COSCO HAMBURG"]': 'test1',
    '[insert Voyage Number, such as "016E"]': 'test2',
    '[insert original Booking Number/, such as "6178400005"]': 'test3',
    '[insert Port of Loading and Port of Discharging as stated in the Bill of Lading, such as "XIAMEN, CHINA/NAPLES"]': 'test4',
    # todo remaining items.
}


if __name__ == '__main__':
    input_file_path = utils.get_input_file_path(INPUT_FILE_NAME)
    doc = Document(input_file_path)

    doc = replace_iterating_paragraphs(doc, TEXT_REPLACE_MAP)

    output_file_path = utils.get_output_file_path(OUTPUT_FILE_NAME)
    doc.save(output_file_path)