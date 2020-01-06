import spacy
import re
from textstat import *

from spacy.tokenizer import Tokenizer


class ControlText:

    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load('en_core_web_sm')
        self.prefix_re = spacy.util.compile_prefix_regex(self.nlp.Defaults.prefixes)
        self.suffix_re = spacy.util.compile_suffix_regex(self.nlp.Defaults.suffixes)
        self.infix_re = re.compile(r'''[-~]''')

    def remove_meaningless_sentence(self):
        """
        Remove meaningless sentences from sentences received
        :return: meaning sentences
        """

        about_txt = self.nlp(self.text)
        sentences = list(about_txt.sents)
        meaning_sentence = ""
        for sentence in sentences:

            str_sentence = sentence.text
            check_trail = "\r\n\r\n" in str_sentence
            while check_trail:

                trail_index = str_sentence.find("\r\n\r\n")
                sub_sentence = str_sentence[:trail_index]
                sub_sentence = sub_sentence.replace("\r\n", "")
                sub_sentence = sub_sentence.strip()
                if sub_sentence.endswith("."):

                    meaning_sentence += " " + sub_sentence
                str_sentence = str_sentence[trail_index + 4:]
                check_trail = "\r\n\r\n" in str_sentence

            str_sentence = str_sentence.replace("\r\n", " ")
            str_sentence = str_sentence.strip()
            if str_sentence.endswith("."):
                meaning_sentence += " " + str_sentence

        return meaning_sentence

    def preprocess_text(self):
        """
        Remove all trailing whitespaces from text
        :return: text
        """

        regex = re.compile(r'[\n\r\t]')
        text = regex.sub(" ", self.text)

        return text

    def tokenize_word(self):
        """
        Tokenize sentences into word
        :return: words
        """

        self.nlp.tokenizer = self.customize_tokenizer()
        custom_tokenizer_about_doc = self.nlp(self.text)

        words = []
        for token in custom_tokenizer_about_doc:

            str_word = token.text
            if str_word == " ":
                continue
            else:
                if "About" in str_word:
                    str_word = str_word.replace("About", "")

                words.append(str_word)

        return words

    def customize_tokenizer(self):
        """
        Adds support to use `-` as the delimiter for tokenization
        :return: Tokenization
        """

        return Tokenizer(self.nlp.vocab, prefix_search=self.prefix_re.search, suffix_search=self.suffix_re.search,
                         infix_finditer=self.infix_re.finditer, token_match=None)


def count_loughran_words_in_token(lough_words, token_words):
    """
    Count loughran words from tokenized words
    :param lough_words: loughran word
    :param token_words: tokenized words
    :return: counts of loughran words as dict
    """

    cnt_lougran = {}
    for lough_name in lough_words:

        cnt_lougran[lough_name] = 0

        for token_word in token_words:

            if token_word.upper() in lough_words[lough_name]:

                cnt_lougran[lough_name] += 1

    return cnt_lougran


class ControlSentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def regularize_sentence(self):
        """
        Regularize sentences
        :return: sentence regularized
        """

        pattern = r"[^\w]"

        reg_sentences = re.sub(pattern, " ", self.sentence)

        return reg_sentences

    def measure_readibility(self):
        """
        Estimate number of all words, kincaid index and fog index
        :return: fog index, kincaid index, number of words
        """

        numword = textstat.lexicon_count(self.sentence, removepunct=True)
        kincaid_index = textstat.flesch_kincaid_grade(self.sentence)
        fog_index = textstat.gunning_fog(self.sentence)

        return fog_index, kincaid_index, numword
