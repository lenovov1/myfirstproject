import requests
from bs4 import BeautifulSoup
import time

# URL of the website where the tire is available
url = "https://kavirtire.ir/"

while True:
    # Send a request to the website
    response = requests.get(url)

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Check if the tire is available
    tire_element = soup.find("div", {"class": "tire", "data-size": tire_info["size"], "data-brand": tire_info["brand"],
                                     "data-model": tire_info["model"]})
    if tire_element:
        # If the tire is available, click the "Add to Cart" button
        add_to_cart_button = tire_element.find("button", {"class": "add-to-cart"})
        if add_to_cart_button:
            add_to_cart_button.click()

            # Navigate to the checkout page
            checkout_url = soup.find("a", {"class": "checkout"})["href"]
            response = requests.get(checkout_url)

            # You can now perform any necessary actions on the checkout page, such as entering payment information
            print("Checkout page reached!")
            break

    # Wait for a few seconds before checking again
    time.sleep(5)