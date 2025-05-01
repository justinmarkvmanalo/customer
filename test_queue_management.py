import unittest
from queue import Queue


priority_queue = Queue()
regular_queue = Queue()


def add_customer(queue_type, customer_name):
    if queue_type == "VIP":
        priority_queue.put(customer_name)  # Add to VIP queue
    elif queue_type == "regular":
        regular_queue.put(customer_name)  # Add to regular queue
    else:
        raise ValueError("Invalid queue type! Use 'VIP' or 'regular'.")


def remove_customer():
    if not priority_queue.empty():
        return priority_queue.get()  # Remove from VIP queue if available
    elif not regular_queue.empty():
        return regular_queue.get()  # Remove from regular queue if VIP is empty
    else:
        return None  # Return None if both queues are empty


def display_queues():
    vip_queue = list(priority_queue.queue)  # Convert VIP queue to a list
    regular_queue_list = list(regular_queue.queue)
    return {"VIP": vip_queue, "Regular": regular_queue_list}


class TestQueueManagementSystem(unittest.TestCase):

    def setUp(self):
        global priority_queue, regular_queue
        priority_queue = Queue()  # Reset VIP queue
        regular_queue = Queue()  # Reset regular queue

    def test_add_customer_vip(self):
        add_customer("VIP", "Alice")
        self.assertEqual(
            list(priority_queue.queue),
            ["Alice"]
        )

    def test_add_customer_regular(self):
        add_customer("regular", "Bob")
        self.assertEqual(
            list(regular_queue.queue),
            ["Bob"]
        )

    def test_remove_customer_vip(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")
        removed = remove_customer()
        self.assertEqual(removed, "Alice")
        self.assertEqual(
            list(priority_queue.queue),
            []
        )
        self.assertEqual(
            list(regular_queue.queue),
            ["Bob"]
        )

    def test_display_queues(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")
        queues = display_queues()
        self.assertEqual(
            queues,
            {
                "VIP": ["Alice"],
                "Regular": ["Bob"]
            }
        )


if __name__ == "__main__":
    unittest.main()
