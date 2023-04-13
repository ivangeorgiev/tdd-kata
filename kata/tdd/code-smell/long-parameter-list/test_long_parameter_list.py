from unittest import TestCase

from parameterized import parameterized_class

from . import long_parameter_list
from . import long_parameter_list_refactored


@parameterized_class(
    ("class_under_test",),
    [
        (long_parameter_list.Order, ""),
        (long_parameter_list_refactored.Order, ""),
    ],
)
class TestOrder(TestCase):
    def test_initializer_should_set_attributes(self):
        order = self.class_under_test(
            id="abc",
            customer_id="customer-1",
            customer_address="address-2",
            product_ids=["product-3"],
            is_premium_customer=True,
        )

        assert isinstance(order, self.class_under_test)
        assert order._id == "abc"
        assert order.get_customer_id() == "customer-1"
        assert order._customer_address == "address-2"
        assert order.get_product_ids() == ["product-3"]
        assert order._has_priority
