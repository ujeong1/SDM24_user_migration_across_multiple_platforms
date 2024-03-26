## Overview

At this time, Threads.net lacks a public API for retrieving or verifying user IDs for profiles. 

## Threads.net User IDs
- **Current Status**: Unavailable
- **Details**: Threads.net does not support the retrieval or confirmation of user IDs for any profile on its platform. This limitation extends to migrants from other platforms who use Threads.

## Mastodon Profile User IDs
- **Dependency**: Access Point
- **Details**: The user ID for a Mastodon profile varies based on the access point utilized to retrieve the user's ID. To provide consistency, we supply user IDs corresponding to the account's original Mastodon server, identified by its hostname (e.g., `mastodon_server_hostname`).

## Bluesky Profile User IDs
- **Dependency**: Access Point
- **Details**: During the time of our data collection, `bsky.app` stood as the sole access point for Bluesky Social, attributable to the ongoing development of the AT protocol. Consequently, all decentralized identifiers (DIDs) we have provided are specifically associated with `bsky.social`.
