# voglbot

Every VOGL's favorite assistant! A Telegram bot to assist attendance management for freshmen and OGLs.

Made for USP FOP 2016, NUS.

## Requirements
Python
`pip` package manager
`redis-server`

## Supported Functions

## How to Run

1. Install dependencies
```pip install -r requirements.txt```

2. Insert Telegram bot API key into `settings_secret.py`. An example is provided in the repository.

3. Insert your chat ID into the `authorized.py` file so that you can use the bot.

4. Start the `redis` server
```redis-server```

The default hostname is `localhost` listening on port 6379

5. Start VOGLBot
```python voglbot.py```
