from django.test import TestCase

from portal_core.utils.text_tools import shortnate, get_words, mask_email


class ShortnateTests(TestCase):
    """ 文字を規定文字数までに切り詰める """

    def test_shortnate(self):
        test_cases = [
            ('吾輩は猫である。名前はまだない。', 16, '吾輩は猫である。名前はまだない。'),
            ('吾輩は猫である。名前はまだない。', 8, '吾輩は猫...'),
            ('吾輩は猫である。名前はまだない。', 4, '...'),
        ]
        for long_text, length, short_text in test_cases:
            self.assertEqual(shortnate(long_text, length), short_text)


class GetWordsTests(TestCase):
    """ 与えられたテキストを形態素解析して、含まれる名詞のリストを返す """

    def test_get_words(self):
        test_cases = [
            ('すもももももももものうち', ['すもも', 'もも', 'もも'])
        ]
        for texts, words in test_cases:
            self.assertEqual(get_words(texts), words)


class MaskEmailTests(TestCase):
    """ メールアドレスをマスクする """

    def test_mask_email(self):
        test_cases = [
            ('test@example.com', 't**@example.com'),
            ('test+test@example.com', 't*******@example.com'),
            ('a@example.jp', 'a@example.jp'),
            ('test_example.com', 'test_example.com'),
        ]
        for email, masked_email in test_cases:
            self.assertEqual(mask_email(email), masked_email)
