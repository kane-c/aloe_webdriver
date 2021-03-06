# -*- coding: utf-8 -*-
"""Test step functions directly."""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import os
import unittest
from time import time

from selenium import webdriver

from aloe import world
from aloe_webdriver.util import (
    find_button,
    find_field,
    find_field_by_id,
    find_field_by_label,
    find_field_by_name,
    option_in_select,
    wait_for,
)

# pylint:disable=missing-docstring


class TestUtil(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        world.browser = webdriver.Firefox()

    def setUp(self):
        world.browser.get(
            'file://' +
            os.path.join(os.path.dirname(__file__),
                         'html_pages', 'basic_page.html')
        )

    @classmethod
    def tearDownClass(cls):
        world.browser.quit()
        delattr(world, 'browser')

    def test_find_by_id(self):
        assert find_field_by_id(world.browser, 'password', 'pass')

    def test_find_by_name(self):
        assert find_field_by_name(world.browser, 'submit', 'submit')
        assert find_field_by_name(world.browser, 'select', 'car_choice')
        assert find_field_by_name(world.browser, 'textarea', 'bio')

    def test_find_by_label(self):
        field = find_field_by_label(world.browser, 'text', 'Username:')
        self.assertEqual(field.get_attribute('id'), 'username')

    def test_no_label(self):
        assert not find_field_by_label(world.browser, 'text', 'NoSuchLabel')

    def test_find_field(self):
        assert find_field(world.browser, 'text', 'username')
        assert find_field(world.browser, 'text', 'Username:')
        assert find_field(world.browser, 'text', 'user')
        assert find_field(world.browser, 'text', 'ชื่อ:')

    def test_find_button(self):
        assert find_button(world.browser, 'submit')
        assert find_button(world.browser, 'Submit!')
        assert find_button(world.browser, 'submit_tentative')
        assert find_button(world.browser, 'Submit as tentative')
        assert find_button(world.browser, 'ส่งฟอร์ม')

    def test_option_in_select(self):
        assert option_in_select(world.browser, 'Favorite Colors:', 'Blue')
        assert option_in_select(world.browser, 'Favorite Colors:', 'ฟ้า')

    def test_wait_for(self):
        """
        Test that wait_for retries on assertion errors.
        """

        start_time = time()

        @wait_for
        def seconds_passed(seconds):
            """
            Test that at least the given number of seconds passed since the
            start of the test.
            """

            assert time() - start_time >= seconds
            return True

        # pylint:disable=unexpected-keyword-arg
        # wait_for decorator parses the argument

        with self.assertRaises(AssertionError):
            seconds_passed(3, timeout=1)

        start_time = time()
        assert seconds_passed(3, timeout=5)
