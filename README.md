Certainly! Here's the updated README with the addition that users need to manually input their username and password during the login process for multiple accounts.

---

# Telegram Contact and Group Automation

This Python script automates the process of adding contacts to a Telegram group using Selenium WebDriver. It allows you to manage contacts and add them to specific groups, all while mimicking human-like interaction with random delays between actions to avoid detection.

## Features
- Reads phone numbers and names from an Excel file and validates phone number format.
- Logs into Telegram Web using Selenium WebDriver. The script opens a login page where the user manually enters their username and password for each account.
- Adds new contacts to Telegram with provided phone numbers and names.
- After adding the contact, it navigates to a specified Telegram group and attempts to add the contact to the group.
- Handles errors gracefully with retries and waits for elements to load.
- Implements random timing delays between actions to simulate human behavior and avoid detection.

## Requirements

To run this script, you'll need the following dependencies:

- **Python 3.x**
- **Selenium**: Web automation tool for browser interaction.
- **Pandas**: For reading data from Excel files.
- **Chrome WebDriver or GeckoDriver**: Depending on your browser choice, either ChromeDriver (for Google Chrome) or GeckoDriver (for Firefox) is required.

You can install the necessary Python packages using `pip`:

```bash
pip install selenium pandas
```

Additionally, download and install the appropriate WebDriver for your browser from one of the following:

- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

Make sure the WebDriver is in your system's PATH or specify the full path in the script.

## Setup

1. **Excel File with Contacts**: Prepare an Excel file (e.g., `numbers.xlsx`) with two columns: `name` and `phone`. The script will read these columns to create new contacts.
   - Column 1: Contact Name
   - Column 2: Contact Phone Number (must start with 9 and be followed by 9 digits, in line with the Iranian phone number format).

2. **Configure WebDriver Path**: In the script, specify the path to your WebDriver. Update the `webdriver_path` variable to point to the location of your downloaded WebDriver:

```python
webdriver_path = '/path/to/your/webdriver'
```

3. **Set Group URL**: The script is designed to add contacts to a specific Telegram group. Update the `page_loader` function with the URL of your target group:

```python
page_loader(drivers[driver_name], 'https://t.me/your-group-name')
```

4. **Login Credentials**: The script will open the Telegram login page where you will need to manually enter your username and password. It supports logging into multiple Telegram accounts by opening separate browser windows for each account. For each account, you will need to log in manually by entering the required credentials when prompted.

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/telegram-contact-group-automation.git
cd telegram-contact-group-automation
```

2. Run the script:

```bash
python telegram_contact_group_automation.py
```

This will start the automation process. The script will:
- Open multiple browser windows (based on the `num_drivers` variable).
- Open the Telegram login page for each browser window where you'll be prompted to manually enter your username and password.
- After successful login, the script will proceed to add contacts from the Excel file to Telegram.
- It will then add those contacts to the specified Telegram group.

The script will handle retries, refreshes, and any pop-ups that appear during the process.

## Customization

- **Number of Browser Instances**: You can adjust the `num_drivers` variable to run multiple browser instances concurrently. This can speed up the process if you're working with a large number of contacts.

- **Delays and Timing**: The script includes functions like `one_to_five_sec`, `one_min`, `two_hour`, etc., to introduce delays between actions. You can customize these delays according to your needs.

- **Error Handling**: If the script encounters any issues (e.g., missing elements, login failures), it will try again or move on to the next task, ensuring the automation continues smoothly.

## Important Notes

- **Telegram Limits**: Be mindful of Telegram's anti-bot measures and potential rate limits. Running this script on a large scale may result in temporary account restrictions.
  
- **Phone Number Format**: The phone numbers should be in the format accepted by Telegram. The script only accepts phone numbers that begin with `9` followed by 9 digits (for Iranian numbers).

- **Webdriver Version**: Ensure that the WebDriver version is compatible with your browser version. If you encounter issues, check for updates on the WebDriver page.


## Disclaimer

This script is intended for educational and personal use. Ensure that you comply with Telegram's terms of service and privacy policies when using automation tools.