# Testing Review

## Tests Reviewed

- **Test Source File:** [tests/db_tests.py](../../tests/auth_tests.py)
  - **Test Function Name:** `test_is_admin_by_username`
    - **Date Reviewed:** 08/10/2023
    - **Comments:** creates a new user to test admin, doesnt test a user already in the database.
      - 
- **Test Source File:** [tests/db_core.py](../../tests/core_tests.py)
  - **Test Function Name:** `test_reset_user_password`
    - **Date Reviewed:** 08/10/2023
    - **Comments:** tests the reset user password on a preset test user in the starting data schema, which could miss problems with current admins
      - 
- **Test Source File:** [tests/db_core.py](../../tests/core_tests.py)
  - **Test Function Name:** `test_set_user_password`
    - **Date Reviewed:** 08/10/2023
    - **Comments:** tests resetting password on preset test user, but doesnt use having a known password to make the error log more readable, returns hashes instead.
