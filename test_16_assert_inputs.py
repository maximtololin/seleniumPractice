def test_input_text(expected_result, actual_result):
    assert (expected_result == actual_result), f"expected {expected_result}, got {actual_result}"

# input 1 and input 2, 11 - 15


def test_substring(full_string, substring):
    assert (substring in full_string), f"expected '{substring}' to be substring of '{full_string}'"
# Sample Input 1:
#
# fulltext some_value
# Sample Output 1:
#
# expected 'some_value' to be substring of 'fulltext'
# Sample Input 2:
#
# 1 1
# Sample Output 2:
#
# Sample Input 3:
#
# some_text some
# Sample Output 3:
