import os
import glob

from utils.file_handling import ControlFile
from src.text_analysis import ControlSentence, ControlText, count_loughran_words_in_token


def get_files(_txt_dir_path, _loughran_path):
    """
    Get text files path and loughran words from text directory and loughran excel file.
    :param _txt_dir_path: text directory path
    :param _loughran_path: loughran excel file path
    :return: text files path, loughran words as dict
    """
    txt_files = glob.glob(os.path.join(_txt_dir_path, "*.txt"))
    loughran_words = ControlFile(_loughran_path).read_loughran_words()

    return txt_files, loughran_words


class GetInitInfo:

    def __init__(self, path):

        self.path = path

    def get_path(self):
        """
        Get various paths such as text directory path and so on
        :return: text directory path, output excel file path, loughran file path
        """

        txt_dir_path = os.path.join(self.path, 'input_txtfile')
        if not os.path.exists(txt_dir_path):
            os.mkdir(txt_dir_path)
        _excel_path = os.path.join(self.path, 'output_excelfile/ProjectTextOuput.xlsx')
        _loughran_path = os.path.join(self.path, 'utils/Loughran-McDonald Sentiment Word Lists.xlsx')

        return txt_dir_path, _excel_path, _loughran_path


class ExecuteAnalysis:

    def __init__(self, files, words, path):

        self.txt_files = files
        self.words = words
        self.execel_path = path

    def text_analysis(self):
        """
        Analyze text received according to loughran word
        :return: nothing, only write text analysis into excel file
        """

        file_control = ControlFile
        text_control = ControlText
        sentence_control = ControlSentence

        for i, txt_file_path in enumerate(self.txt_files):

            txt_file_name = file_control(txt_file_path).extract_file_name()
            print(txt_file_name)
            # if txt_file_name != '4722839':
            #     continue
            txt_file = open(txt_file_path, 'rb')
            text = txt_file.read()
            text = text.decode("utf-8", errors="ignore")
            meaning_sentence = text_control(text).remove_meaningless_sentence()
            print(meaning_sentence)
            regular_sentence = sentence_control(meaning_sentence).regularize_sentence()
            _fog_index, _kincard_index, _numword = sentence_control(meaning_sentence).measure_readibility()
            tokenized_words = text_control(regular_sentence).tokenize_word()
            cnt_loughran = count_loughran_words_in_token(self.words, tokenized_words)

            no = i + 1

            txt_dict = [no, txt_file_name, _fog_index, _kincard_index, _numword, cnt_loughran['NEGATIVE'],
                        cnt_loughran['POSITIVE'], cnt_loughran['UNCERTAINTY'], cnt_loughran['LITIGIOUS'],
                        cnt_loughran['STRONGMODAL'], cnt_loughran['WEAKMODAL'], cnt_loughran['CONSTRAINING']]

            file_control(self.execel_path).write_in_excel(txt_dict)
