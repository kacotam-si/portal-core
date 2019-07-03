from django.core.exceptions import ValidationError
from django.test import TestCase
from django.test.utils import isolate_apps

from portal_core import validators


class CommaSeparatedListValidatorTests(TestCase):
    def test_comma_separated_list_validator(self):
        valid_values = [
            'joe,René,ᴮᴵᴳᴮᴵᴿᴰ,أحمد',
            'joe'
        ]
        invalid_values = [
            'add mig,,',
            'apple, ()'
        ]
        v = validators.CommaSeparatedListValidator()
        for valid in valid_values:
            with self.subTest(valid=valid):
                v(valid)
        for invalid in invalid_values:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValidationError):
                    v(invalid)


class KanaValidatorTests(TestCase):
    def test_kana_validator(self):
        valid_kanas = ['ふりがな', 'がっこう', 'ささき']
        invalid_kanas = [
            'フリガナ', '振り仮名', 'hurigana', 'ｈｕｒｉｇａｎａ'
        ]
        v = validators.KanaValidator()
        for valid in valid_kanas:
            with self.subTest(valid=valid):
                v(valid)
        for invalid in invalid_kanas:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValidationError):
                    v(invalid)


class PhoneNumberValidatorTests(TestCase):
    def test_phone_number_validator(self):
        valid_values = ['000-0000-0000', '000-000-0000', '0000-00-0000']
        invalid_values = ['09000000000', '(03)252-2222']
        v = validators.PhoneNumberValidator()
        for valid in valid_values:
            with self.subTest(valid=valid):
                v(valid)
        for invalid in invalid_values:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValidationError):
                    v(invalid)


class PostCodeValidatorTests(TestCase):
    def test_postcode_validator(self):
        valid_values = ['000-0000', '001-0035']
        invalid_values = ['0000000', '000-000-0000']
        v = validators.PostcodeValidator()
        for valid in valid_values:
            with self.subTest(valid=valid):
                v(valid)
        for invalid in invalid_values:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValidationError):
                    v(invalid)
