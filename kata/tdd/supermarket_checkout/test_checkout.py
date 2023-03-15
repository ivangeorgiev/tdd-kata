import unittest
from .checkout import Checkout


class TestCheckoutClass(unittest.TestCase):
    def setUp(self):
        self.checkout = Checkout()
        self.checkout.addItemPrice("a", 1)
        self.checkout.addItemPrice("b", 2)

    def test_can_calculate_the_current_total(self):
        # Setup
        self.checkout.addItem("a")
        # Act
        total = self.checkout.calculateTotal()
        # Assert
        self.assertEqual(total, 1)

    def test_can_calculate_correct_total_with_muliple_items(self):
        self.checkout.addItem("a")
        self.checkout.addItem("b")
        # Act
        total = self.checkout.calculateTotal()
        # Assert
        self.assertEqual(total, 3)

    def test_can_add_discount(self):
        self.checkout.addDiscount("a", 3, 2)

    def test_can_apply_discount_rules_to_total(self):
        self.checkout.addDiscount("a", 3, 2)
        self.checkout.addItem("a")
        self.checkout.addItem("a")
        self.checkout.addItem("a")
        self.checkout.addItem("a")
        # Act
        total = self.checkout.calculateTotal()
        # Assert
        self.assertEqual(total, 3)

    def test_exception_is_thrown_when_adding_item_without_price(self):
        with self.assertRaises(KeyError):
            self.checkout.addItem("c")
