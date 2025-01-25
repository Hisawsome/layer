import requests
import json
import random
import time
import string

# Function to generate a random Ethereum wallet address
def generate_random_wallet_address():
    chars = string.hexdigits  # Hexadecimal characters (0-9, a-f)
    address = '0x' + ''.join(random.choice(chars) for _ in range(40)).lower()
    return address

# Get the referral code from user input
def get_referral_code():
    referral_code = input("Enter your referral code: ").strip()
    return referral_code

# Define the URL with the referral code
def generate_url(referral_code):
    return f"https://referral.layeredge.io/api/referral/register-wallet/{referral_code}"

# Set the headers for the POST request
def get_headers():
    return {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://dashboard.layeredge.io',
        'Referer': 'https://dashboard.layeredge.io/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

# Function to log responses and errors to a log file
def log_to_file(log_file, message):
    with open(log_file, "a") as file:
        file.write(message)

# Main function to send requests and handle the process
def register_wallet(referral_code, log_file):
    url = generate_url(referral_code)
    headers = get_headers()

    while True:
        wallet_address = generate_random_wallet_address()  # Generate a new wallet address
        payload = json.dumps({"walletAddress": wallet_address})

        try:
            # Send POST request
            response = requests.post(url, headers=headers, data=payload)

            # Prepare log entry
            log_entry = f"BY RIDI | Wallet: {wallet_address} | Status: {response.status_code} | Response: {response.text}\n"
            print(log_entry)

            # Log the response to file
            log_to_file(log_file, log_entry)

            # If rate limit is hit, pause for 5 minutes
            if response.status_code == 429:
                print("Rate limit reached. Pausing for 5 minutes... BY RIDI")
                time.sleep(300)

        except Exception as e:
            # Handle any exception that occurs during the request
            error_message = f"BY RIDI | Error occurred for {wallet_address}: {str(e)}\n"
            print(error_message)
            log_to_file(log_file, error_message)

        # Introduce a random delay (between 60 and 100 seconds) between requests
        delay = random.randint(60, 100)
        print(f"BY RIDI | Next request in {delay} seconds...")
        time.sleep(delay)

# Entry point of the script
if __name__ == "__main__":
    print("Starting Wallet Registration Script - BY RIDI")
    referral_code = get_referral_code()  # Get referral code from user input
    log_file = "api_requests.log"  # Define log file
    register_wallet(referral_code, log_file)  # Start the wallet registration process
          
