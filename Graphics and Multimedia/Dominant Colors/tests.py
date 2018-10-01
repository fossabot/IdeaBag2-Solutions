#!/usr/bin/env python3
import unittest

from dominant_colors import dominant_colors, convert_to_color_dict_list


class Test(unittest.TestCase):

    def test_dominant_colors(self):
                         [(51, 77, 6), (64, 95, 1), (65, 103, 0)])

    def test_convert_to_color_dict_list(self):
        self.assertEqual(convert_to_color_dict_list([(51, 77, 6), (64, 95, 1), (65, 103, 0)]),
        [{'rgb': (51, 77, 6), 'hsl': [0.23, 41.5, -0.88], 'hsv': [0.23, 0.92, 77], 'hex': ['33', '4d', '06']}, {'rgb': (64, 95, 1), 'hsl': [0.22, 48.0, -1.0], 'hsv': [0.22, 0.99, 95], 'hex': ['40', '5f', '01']}, {'rgb': (65, 103, 0), 'hsl': [0.23, 51.5, -1.02], 'hsv': [0.23, 1.0, 103], 'hex': ['41', '67', '00']}])


if __name__ == "__main__":
    unittest.main()