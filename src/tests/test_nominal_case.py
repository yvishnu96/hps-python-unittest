# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestNominalCase(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_Simple_use(self):
        # Well, sometimes, you just get a coffee.
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I take a coffee
        self.actionwords.i_take_a_coffee()
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()

    def messages_are_based_on_language(self, lang, ready_message):
        # Well, sometimes, you just get a coffee.
        # When I start the coffee machine "<lang>"
        self.actionwords.i_start_the_coffee_machine(lang = lang)
        # Then message "<ready_message>" should be displayed
        self.actionwords.message_message_should_be_displayed(message = ready_message)

    def test_Messages_are_based_on_language_english(self):
        self.messages_are_based_on_language(lang = 'en', ready_message = 'Ready')

    def test_Messages_are_based_on_language_french(self):
        self.messages_are_based_on_language(lang = 'fr', ready_message = 'Pret')



    def test_No_messages_are_displayed_when_machine_is_shut_down(self):
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I shutdown the coffee machine
        self.actionwords.i_shutdown_the_coffee_machine()
        # Then message "" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "")
