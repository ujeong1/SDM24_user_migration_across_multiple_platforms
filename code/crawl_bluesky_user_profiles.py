import pandas as pd
import json
from atproto import Client, CAR, models
from tqdm import tqdm

def profile_to_dict(profile_obj):
    return {x: str(profile_obj[x]) for x in dir(profile_obj) if '_' not in x}
    
at_client = Client()
USERNAME = "{your_username}"
PASSWD = "{your_account_password}"
at_client.login(USERNAME, PASSWD)

output_filename = "{your_output_filename}.csv"
df = pd.read_csv('../data/twitter_bluesky_user_ids_mapped.csv')
bluesky_user_profiles = []
for i, row in tqdm(df.iterrows(), total=len(df)):
    try:
        user_did = row['bluesky_user_did']
        params = models.AppBskyActorGetProfile.Params(actor=user_did)
        user_profile_obj = at_client.app.bsky.actor.get_profile(params)
        user_profile = profile_to_dict(user_profile_obj)
    except Exception as e:
        user_profile = {}
        print(e)

    bluesky_user_profiles.append(user_profile)

df["bluesky_user_profile"] = mastodon_user_profiles
df.to_csv(output_filename, index=False)
