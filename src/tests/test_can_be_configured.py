# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestCanBeConfigured(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_display_settings(self):
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I switch to settings mode
        self.actionwords.i_switch_to_settings_mode()
        # Then displayed message is:
        self.actionwords.displayed_message_is(free_text = "Settings:\n - 1: water hardness\n - 2: grinder")

    def test_default_settings(self):
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I switch to settings mode
        self.actionwords.i_switch_to_settings_mode()
        # Then settings should be:
        self.actionwords.settings_should_be(datatable = "| water hardness | 2      |\n| grinder        | medium |")
