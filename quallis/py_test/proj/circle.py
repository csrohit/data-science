class InsufficientException(Exception):
    pass

class MobileInventory:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = {}

        if not isinstance(inventory, dict):
            raise TypeError("Input inventory must be a dictionary")
        else:
            self.balance_inventory = inventory
            for key in self.balance_inventory.keys():
                if not isinstance(key, str):
                    raise ValueError("Mobile model name must be a string")
            for val in self.balance_inventory.values():
                if (not isinstance(val, int)) or val < 0:
                    raise ValueError("No. of mobiles must be a positive integer")


    def add_stock(self, new_stock):
        if not isinstance(new_stock, dict):
            raise TypeError("Input stock must be a dictionary")
        else:
            for key in new_stock.keys():
                if not isinstance(key, str):
                    raise ValueError("Mobile model name must be a string")
            for val in new_stock.values():
                if (not isinstance(val, int)) or val < 0:
                    raise ValueError("No. of mobiles must be a positive integer")
            for key, val in new_stock.items():
                if key in self.balance_inventory.keys():
                    self.balance_inventory[key] = self.balance_inventory.get(key) + val
                else:
                    self.balance_inventory[key] = val

    def sell_stock(self, requested_stock):
        if not isinstance(requested_stock, dict):
            raise TypeError("Requested stock must be a dictionary")
        else:
            for key in requested_stock.keys():
                if not isinstance(key, str):
                    raise ValueError("Mobile model name must be a string")
            for val in requested_stock.values():
                if (not isinstance(val, int)) or val < 0:
                    raise ValueError("No. of mobiles must be a positive integer")
            for key in requested_stock.keys():
                if key in self.balance_inventory.keys():
                    if requested_stock.get(key) > self.balance_inventory.get(key):
                        raise InsufficientException("insufficient Stock")
                else:
                    raise InsufficientException("No stock, New Model Request")

