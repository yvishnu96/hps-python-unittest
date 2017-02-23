# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestSupportInternationalisation(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_no_messages_are_displayed_when_machine_is_shut_down(self):
        # Tags: priority:1
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I shutdown the coffee machine
        self.actionwords.i_shutdown_the_coffee_machine()
        # Then message "" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "")

    def messages_are_based_on_language(self, language, ready_message):
        # Well, sometimes, you just get a coffee.
        # Tags: priority:1
        # When I start the coffee machine using language "<language>"
        self.actionwords.i_start_the_coffee_machine_using_language_lang(lang = language)
        # Then message "<ready_message>" should be displayed
        self.actionwords.message_message_should_be_displayed(message = ready_message)

    def test_Messages_are_based_on_language_english(self):
        self.messages_are_based_on_language(language = 'en', ready_message = 'Ready')

    def test_Messages_are_based_on_language_french(self):
        self.messages_are_based_on_language(language = 'fr', ready_message = 'Pret')
