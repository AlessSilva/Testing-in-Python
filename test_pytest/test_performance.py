import pytest
import time


def find_element(element, data):
    return element in data


def test_find_element_performance():
    data = list(range(1000000))
    element_to_find = 999999

    start_time = time.time()
    result = find_element(element_to_find, data)
    end_time = time.time()

    elapsed_time = end_time - start_time
    assert result == True
    assert elapsed_time < 0.05

    print(f"Tempo de execução: {elapsed_time:.5f} segundos")
