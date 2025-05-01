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


if __name__ == "__main__":
    unittest.main()
