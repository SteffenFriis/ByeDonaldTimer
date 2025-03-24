import tweepy
import datetime
import os
import sys

# Twitter API credentials
API_KEY = '#'
API_SECRET = '#'
ACCESS_TOKEN = '#'
ACCESS_TOKEN_SECRET = '#'

# Dynamically set the log file path to the script's directory (or a configurable location)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Directory where the script is located
LOG_FILE = os.path.join(SCRIPT_DIR, "twitter_countdown_log.txt")  # Generic log file in script directory

def log_message(message):
    """Writes log messages to a file immediately and prints them to console."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.datetime.now()} - {message}\n")
            log_file.flush()
        print(message)  # Also print to console for manual debugging
    except Exception as e:
        print(f"Logging failed: {e}")

def authenticate_twitter():
    """Authenticates with Twitter and logs the status."""
    try:
        # Log Tweepy version
        log_message(f"Tweepy version: {tweepy.__version__}")

        # Check Tweepy version and use appropriate authentication
        if tweepy.__version__.startswith('3'):
            auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            api.verify_credentials()
            log_message("Twitter authentication successful (Tweepy v3.x).")
            return api, 'v3'
        else:  # Assume v4.x or higher
            client = tweepy.Client(
                consumer_key=API_KEY,
                consumer_secret=API_SECRET,
                access_token=ACCESS_TOKEN,
                access_token_secret=ACCESS_TOKEN_SECRET
            )
            # Verify credentials (v4.x doesn't have a direct equivalent, so we assume success if no exception)
            log_message("Twitter authentication successful (Tweepy v4.x).")
            return client, 'v4'
    except Exception as e:
        log_message(f"Twitter authentication failed: {e}")
        sys.exit(1)  # Exit script on failure

def post_twitter_update(twitter_obj, version):
    """Posts a tweet and logs all details, including API response."""
    try:
        END_OF_TRUMP_TERM = datetime.date(2029, 1, 20)
        today = datetime.date.today()
        days_left = (END_OF_TRUMP_TERM - today).days

        message = f"There are now only {days_left} days until Trump is no longer President! 🗳️🇺🇸✨\n\n#USPolitics #Trump #Countdown #dkpol"
        log_message(f"Attempting to post tweet: {message}")

        # Post tweet based on Tweepy version
        if version == 'v3':
            response = twitter_obj.update_status(status=message)
            log_message(f"Tweet Response: {response._json}")
        else:  # v4
            response = twitter_obj.create_tweet(text=message)
            log_message(f"Tweet Response: {response.data}")

    except Exception as e:
        log_message(f"Error posting tweet: {e}")
        raise  # Re-raise to ensure the error is visible

# Run the script
log_message("Script started via Task Scheduler.")
twitter_obj, tweepy_version = authenticate_twitter()
post_twitter_update(twitter_obj, tweepy_version)
log_message("Script finished execution.")