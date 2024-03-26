import pandas as pd
import requests
from tqdm import tqdm

def get_user_profile(host, user_id):
    url = f'https://{host}/api/v1/accounts/{user_id}'
    try:
        user = requests.get(url)
        user_json = user.json()
        return user_json
    except Exception as e:
        return e


output_filename = "{your_output_filename}.csv"
df = pd.read_csv("../data/twitter_mastodon_user_ids_mapped.csv")
mastodon_user_profiles = []
for i, row in tqdm(df.iterrows(), total=len(df)):
    try:
        user_id = row['mastodon_user_id']
        hostname = row['mastodon_server_hostname']
        user_profile = get_user_profile(hostname, user_id)
    except Exception as e:
        user_profile = {}
        print(e)
    mastodon_user_profiles.append(user_profile)

df["mastodon_user_profile"] = mastodon_user_profiles
df.to_csv(output_filename, index=False)
