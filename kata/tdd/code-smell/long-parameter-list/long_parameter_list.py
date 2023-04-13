from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def get_identifier() -> str:
        pass

    @abstractmethod
    def get_address() -> str:
        pass

    @abstractmethod
    def has_premium_subscription() -> bool:
        pass


class Order:
    _id: str
    _customer_id: str
    _customer_address: str
    _has_priority: bool
    _product_ids: list[str]

    def __init__(self, id: str, customer_id: str, customer_address: str, product_ids: list[str], is_premium_customer: bool) -> None:
        self._id = id
        self._customer_id = customer_id
        self._customer_address = customer_address
        self._product_ids = product_ids.copy()
        self._has_priority = is_premium_customer

    def get_product_ids(self):
        return self._product_ids

    def get_customer_id(self) -> str:
        return self._customer_id

