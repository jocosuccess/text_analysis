import os
from src.execute import ExecuteAnalysis, GetInitInfo, get_files
from utils.file_handling import ControlFile


def init_():
    """

    :return:
    """
    _cur_dir = os.path.dirname(os.path.abspath(__file__))
    get_init_info = GetInitInfo(path=_cur_dir)
    text, excel, loughran = get_init_info.get_path()
    text_files, loughran_words = get_files(text, loughran)
    ControlFile(excel).create_excel_file()
    ExecuteAnalysis(text_files, loughran_words, excel).text_analysis()


if __name__ == '__main__':

    init_()
