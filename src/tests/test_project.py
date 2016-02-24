# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestCoffeeMachineHiptestPublisherSample(unittest.TestCase):
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

    def test_Water_runs_away(self):
        # Simple scenario showing that after 50 coffees, the "Fill tank" message is displayed but it is still possible to have coffee until the tank is fully empty.
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When fifty coffees have been taken without filling the tank
        self.actionwords.fifty_coffees_have_been_taken_without_filling_the_tank()
        # Then message "Fill tank" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Fill tank")
        # When I take a coffee
        self.actionwords.i_take_a_coffee()
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
        # When I take "10" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 10)
        # Then coffee should not be served
        self.actionwords.coffee_should_not_be_served()
        # And message "Fill tank" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Fill tank")
        # When I fill the water tank
        self.actionwords.i_fill_the_water_tank()
        # Then message "Ready" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Ready")

    def test_Beans_run_out(self):
        # Simple scenario showing that after 38 coffees, the message "Fill beans" is displayed but it is possible to take two coffees until there is no more beans.
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When thirty eight coffees are taken without filling beans
        self.actionwords.thirty_eight_coffees_are_taken_without_filling_beans()
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
        # And message "Fill beans" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Fill beans")
        # When I take "2" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 2)
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
        # And message "Fill beans" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Fill beans")
        # When I take a coffee
        self.actionwords.i_take_a_coffee()
        # Then coffee should not be served
        self.actionwords.coffee_should_not_be_served()

    def test_Full_grounds_does_not_block_coffee(self):
        # You keep getting coffee even if the "Empty grounds" message is displayed. That said it's not a fantastic idea, you'll get ground everywhere when you'll decide to empty it.
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I take "29" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 29)
        # Then message "Ready" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Ready")
        # When I take a coffee
        self.actionwords.i_take_a_coffee()
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
        # And message "Empty grounds" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Empty grounds")
        # When I fill the water tank
        self.actionwords.i_fill_the_water_tank()
        # And I fill the beans tank
        self.actionwords.i_fill_the_beans_tank()
        # And I take "20" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 20)
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
        # And message "Empty grounds" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Empty grounds")

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
