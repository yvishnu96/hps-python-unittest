# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestBeans(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # And I handle everything except the beans
        self.actionwords.i_handle_everything_except_the_beans()

    def test_message_fill_beans_is_displayed_after_38_coffees_are_taken(self):
        # Tags: priority:0
        # When I take "38" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 38)
        # Then message "Fill beans" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Fill beans")

    def test_it_is_possible_to_take_40_coffees_before_there_is_really_no_more_beans(self):
        # Tags: priority:2
        # Given I take "40" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 40)
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
        # When I take a coffee
        self.actionwords.i_take_a_coffee()
        # Then coffee should not be served
        self.actionwords.coffee_should_not_be_served()
        # And message "Fill beans" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Fill beans")

    def test_after_adding_beans_the_message_fill_beans_disappears(self):
        # Tags: priority:0
        # Given I take "40" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 40)
        # When I fill the beans tank
        self.actionwords.i_fill_the_beans_tank()
        # Then message "Ready" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Ready")
