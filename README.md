# desu-telegram-bot
Simple telegram bot inspired by the word filter commonly used on imageboards. Whenever a user sends a message containing the word 'tbh', the bot replies with the same messege but with 'tbh' replaced to 'desu' for humorous purposes.
## Usage 
To use this bot follow these steps:
1. Create your new bot with the BotFather on Telegram
2. Put your bot's API token into dedicated place in the 'desu-bot.py' code
3. Deploy the python file on a cloud platform such as Heroku, or run it locally on your own machine
4. Invite your bot to the channel where you want to use it and give the bot admin rights
5. Done
## Functions and commands 
-```/start``` command: prints greetings -- meant for debugging purposes

-```process_message``` function: handles word replacement and sending messeges
