import csv
import os
import pytest
from pages.login_page import LoginPage
from datetime import datetime

def load_users_from_csv():
    filepath = os.path.join(os.path.dirname(__file__), '../data/users.csv')
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

@pytest.mark.parametrize("user_data", load_users_from_csv())
def test_login(driver, user_data):
    login_page = LoginPage(driver)
    login_page.load()

    print(f"\n Probando login con: {user_data['username']} ({user_data['expected']})")

    login_page.login(user_data['username'], user_data['password'])

    try:
        if user_data['expected'] == "success":
            assert login_page.is_logged_in(), f"Expected login to succeed for {user_data['username']}"
        else:
            assert login_page.has_error_message(), f"Expected login to fail for {user_data['username']}"
    except AssertionError as e:
        # Si falla, sacar screenshot
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshots/failure_{user_data['username']}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(filename)
        print(f"Test falló. Screenshot guardado en: {filename}")
        raise e  # relanza el error para que PyTest lo reporte
