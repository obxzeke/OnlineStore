# Testing Review

## Tests Reviewed

- **Test Source File:** [tests/core_tests.py](../../tests/core_tests.py)
  - **Test Function Name:** `test_session_starting_cart`
    - **Date Reviewed:** 08/10/2023
    - **Comments:**
      - test looks good, tests if the cart starts empty

- **Test Source File:** [tests/core_tests.py](../../tests/core_tests.py)
  - **Test Function Name:** `test_session_cart_add_item`
    - **Date Reviewed:** 08/10/2023
    - **Comments:**
      - test looks good, tests if the cart has the item in it using the test item id
      - would test starting with an item in a cart then adding a new item to test

- **Test Source File:** [tests/core_tests.py](../../tests/core_tests.py)
  - **Test Function Name:** `test_session_cart_price`
    - **Date Reviewed:** 08/10/2023
    - **Comments:**
      - only tests with one item, if testing for whole cart price there should me more items in cart

- **Test Source File:** [tests/db_tests.py](../../tests/db_tests.py)
  - **Test Function Name:** `test_check_product_rating_review`
    - **Date Reviewed:** 08/10/2023
    - **Comments:**
      - tests looks good, in the future would add a test for most recent review on product
