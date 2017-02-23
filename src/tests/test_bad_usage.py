# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestBadUsage(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_full_grounds_does_not_block_coffee(self):
        # You keep getting coffee even if the "Empty grounds" message is displayed. That said it's not a fantastic idea, you'll get ground everywhere when you'll decide to empty it.
        # Tags: priority:2
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # And I handle everything except the grounds
        self.actionwords.i_handle_everything_except_the_grounds()
        # When I take "50" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 50)
        # Then message "Empty grounds" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Empty grounds")
        # And coffee should be served
        self.actionwords.coffee_should_be_served()
