#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/8 12:44
# @Author     : fany
# @Project    : PyCharm
# @File       : python死锁解决方案.py
# @description:
# 银行家算法解决死锁
class BankerAlgorithm:
    def __init__(self, processes, resources):
        self.processes = processes
        self.resources = resources
        self.allocated = [[0] * len(resources) for _ in range(len(processes))]
        self.max_need = [[0] * len(resources) for _ in range(len(processes))]

    def request_resources(self, process_id, requested_resources):
        if all(requested <= need and requested <= available
               for requested, need, available in zip(requested_resources, self.max_need[process_id], self.resources)):
            self.resources = [available - requested for available, requested in zip(self.resources, requested_resources)]
            self.allocated[process_id] = [allocated + requested for allocated, requested in zip(self.allocated[process_id], requested_resources)]
            return True
        else:
            return False

    def release_resources(self, process_id):
        self.resources = [available + allocated for available, allocated in zip(self.resources, self.allocated[process_id])]
        self.allocated[process_id] = [0] * len(self.resources)

# Example usage
processes = 5
resources = [10, 5, 7]
banker = BankerAlgorithm(processes, resources)

# Process 0 requests resources
if banker.request_resources(0, [7, 4, 3]):
    print("Resources allocated.")
else:
    print("Resources request denied.")

# Process 1 releases resources
banker.release_resources(1)

# 方案2
import threading


def request_resources_with_timeout(banker, process_id, requested_resources):
    event = threading.Event()

    def request():
        if banker.request_resources(process_id, requested_resources):
            event.set()

    request_thread = threading.Thread(target=request)
    request_thread.start()

    # Wait for the request to complete or timeout
    event.wait(timeout=5)  # Set the timeout value

    if event.is_set():
        print("Resources allocated.")
    else:
        print("Resources request timed out.")


# Example usage
processes = 5
resources = [10, 5, 7]
banker = BankerAlgorithm(processes, resources)

# Process 2 requests resources with timeout
request_resources_with_timeout(banker, 2, [3, 2, 2])
