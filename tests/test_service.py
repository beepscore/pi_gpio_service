#!/usr/bin/env/python3

import unittest
from pi_gpio_service import service


class TestPiGpioService(unittest.TestCase):

    def test_input_pins(self):

        pins = {
            '23': {'name': 'IN_23', 'pin_direction': 'input'},
            '24': {'name': 'OUT_24', 'pin_direction': 'output'},
            '25': {'name': 'OUT_25', 'pin_direction': 'output'}
        }

        # call method under test
        self.assertEqual(service.input_pins(pins),
                         {'23': {'name': 'IN_23', 'pin_direction': 'input'}})

    def test_output_pins(self):

        pins = {
            '23': {'name': 'IN_23', 'pin_direction': 'input'},
            '24': {'name': 'OUT_24', 'pin_direction': 'output'},
            '25': {'name': 'OUT_25', 'pin_direction': 'output'}
        }

        expected = {'24': {'name': 'OUT_24', 'pin_direction': 'output'},
                    '25': {'name': 'OUT_25', 'pin_direction': 'output'}}

        # call method under test
        self.assertEqual(service.output_pins(pins), expected)
