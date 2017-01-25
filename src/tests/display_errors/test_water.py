# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestWater(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # And I handle everything except the water tank
        self.actionwords.i_handle_everything_except_the_water_tank()

    def test_Message_Fill_water_tank_is_displayed_after_50_coffees_are_taken(self):
        # When I take "50" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 50)
        # Then message "Fill tank" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Fill tank")

    def test_It_is_possible_to_take_10_coffees_after_the_message_Fill_water_tank_is_displayed(self):
        # Given I take "60" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 60)
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
        # When I take a coffee
        self.actionwords.i_take_a_coffee()
        # Then coffee should not be served
        self.actionwords.coffee_should_not_be_served()

    def test_When_the_water_tank_is_filled_the_message_disappears(self):
        # Given I take "55" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 55)
        # When I fill the water tank
        self.actionwords.i_fill_the_water_tank()
        # Then message "Ready" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Ready")
