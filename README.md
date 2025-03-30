# Twitter Countdown Generator

A lightweight Python script that generates a countdown tweet for any event, with customizable end dates and log file locations. Originally created to track the days until Donald Trump is no longer President, this tool can be adapted for any countdown. It logs each tweet to a file and is designed to run automatically via Windows Task Scheduler.

## Features
- Calculates days remaining until a specified end date.
- Generates tweets with emojis and hashtags.
- Saves logs to a file in the script's directory (portable across systems).
- Easily customizable for any event or countdown.

## Prerequisites
- **Python 3.x** installed on your Windows machine ([Download Python](https://www.python.org/downloads/)).
- Basic familiarity with Windows Task Scheduler.

## Setup
1. **Clone or Download the Repository**  
   - Click the green "Code" button and download the ZIP, or clone it with:  
     ```
     git clone https://github.com/SteffenFriis/X-Bot-Trump-Countdown.git
     ```
   - Extract the files to a folder (e.g., `C:\Users\YourName\TwitterCountdown`).

2. **Install Dependencies**  
   - This script uses only Python’s built-in libraries (`datetime` and `os`), so no additional installations are required.
   - Install Tweepy via pip:  
     ```
     pip install tweepy
     ```
3. **Set Up Twitter API Credentials**  
   - Go to the [Twitter Developer Portal](https://developer.twitter.com/), create an app, and generate:  
     - API Key  
     - API Secret  
     - Access Token  
     - Access Token Secret  
   - Open `TrumpCountdown.py` and replace the placeholder values (`your_api_key`, etc.) with your credentials.
  
4. **Customize the Script**  
   - Open `TrumpCountdown.py` in a text editor (e.g., Notepad or VS Code).
   - Modify the `END_DATE` variable to your desired countdown end date (e.g., `datetime(2029, 1, 20)` for Trump’s hypothetical term end).
   - Optionally, tweak the tweet text, emojis, or hashtags in the `tweet` string.

## Running the Script
- To test manually, open a Command Prompt in the script’s folder and run:  

- The script will output a tweet and log it to `twitter_countdown_log.txt` in the same directory.

## Automating with Windows Task Scheduler
1. **Open Task Scheduler**  
 - Press `Win + S`, type "Task Scheduler," and hit Enter.

2. **Create a New Task**  
 - Click "Create Task" (not "Create Basic Task") in the right-hand Actions pane.
 - **General Tab**:  
   - Name: `TwitterCountdown` (or any name you prefer).  
   - Check "Run whether user is logged on or not" (optional, for background running).  
   - Check "Run with highest privileges" if needed.

3. **Triggers Tab**  
 - Click "New" and set a schedule (e.g., "Daily" at 8:00 AM).  
 - Adjust the frequency (e.g., repeat every 1 day) and click OK.

4. **Actions Tab**  
 - Click "New" and set:  
   - Action: `Start a program`.  
   - Program/script: Full path to Python (e.g., `C:\Python39\python.exe`).  
   - Add arguments: Full path to your script (e.g., `C:\Users\YourName\TwitterCountdown\TrumpCountdown.py`).  
   - Start in: Folder containing your script (e.g., `C:\Users\YourName\TwitterCountdown`).  
   - Click OK.

5. **Conditions/Settings Tabs**  
 - Adjust as needed (e.g., uncheck "Start the task only if the computer is on AC power" for laptops).  
 - Click OK and enter your Windows password if prompted.

6. **Test the Task**  
 - Find your task in the Task Scheduler Library, right-click it, and select "Run."  
 - Check `twitter_countdown_log.txt` to confirm it logged the tweet.

## Customization
- Change `END_DATE` in the script for any event (e.g., elections, holidays).  
- Modify the tweet format, emojis, or hashtags to suit your needs.  
- Update `LOG_FILE` if you want logs saved elsewhere.

## Contributing
Feel free to fork this repo, submit pull requests, or open issues with suggestions!

## License
This project is open-source and free to use under the [MIT License](license.md).
