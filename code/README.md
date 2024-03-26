### Setup Instructions

Before executing the scripts in this package, ensure you have completed the following preparatory steps:

1. **Install Dependencies**: First, install the necessary Python dependencies specified in `requirements.txt`. Execute the command `pip install -r requirements.txt` in your terminal or command prompt to install these libraries. This step ensures that all required Python packages are installed and ready for use.

2. **Bluesky Account Setup**: For `crawl_bluesky_user_profiles.py`, you need an active account on Bluesky. Set up your account by visiting [bsky.social](https://bsky.social). This is a crucial step to access and use Bluesky's API features.

3. **Twitter API Tokens**: To run `crawl_twitter_user_profiles.py`, you must have your Twitter API tokens. These tokens are essential for authenticating your requests to Twitter's API. Apply for Twitter API access via the [Twitter Developer Platform](https://developer.twitter.com/). Due to the change in Twitter API's policy, crawling user profiles currently requires priced API tiers.

4. **Mastodon Access**: Using the Mastodon crawling script (assumed to be named `mastodon_data_crawler.py` for consistency) does not require a personal account. This script leverages Mastodon's REST API, which allows for unauthorized access via a generic access point provided by Mastodon, enabling the use of this script without a Mastodon account.

5. **Threads.net Access (not supported)**: Currently, there is no public API available for Threads.net, which means we cannot provide scripts for crawling data from this platform. For our research paper, we manually collected Threads.net data, following their terms of condition.

#### Important Notes

- Ensure compliance with each platform's API usage terms and conditions.
- Safeguard your API tokens and account information, avoiding unauthorized disclosures.
- This package is intended for educ
