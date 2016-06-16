# voglbot

Every VOGL's favorite assistant! A Telegram bot to assist attendance management for freshmen and OGLs.

Made for USP FOP 2016, NUS.

## Requirements
Python 3.4

`telepot`

`mongodb` and `pymongo`

## Deployment
1. Ensure Telegram bot API key is inside `settings_secret.py`. Use the example file `settings_secret_example.py` as a template.

2. Ensure that the `mongod` daemon is running in the background.

3. Run the bot using
```
python3 voglbot.py
```

## User Management
Manage the whitelist in `authorized.py` by adding the person's Telegram chat ID and an identifer (usually their name) to the address book dictionary. You will also need to add them to the corresponding group, e.g. `safety` or `cogls`.
