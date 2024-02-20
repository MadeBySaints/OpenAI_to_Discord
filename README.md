# OpenAI_to_Discord
Leverage the power of open AI in your discord server

# ChatGPT Discord Bot

This Discord bot integrates with OpenAI's ChatGPT to provide AI-powered responses within a specified Discord channel. The bot is designed to listen for commands in Discord, forward those commands to ChatGPT, and relay ChatGPT's responses back into the Discord channel. It is built using Python, leveraging the `discord.py` library for Discord bot functionality and the `openai` Python package to interact with the OpenAI API.

## Features

- **AI-Powered Chat**: Leverage ChatGPT's powerful language model for generating responses to user inputs.
- **Channel Restriction**: Ensures the bot only operates within a specified Discord channel to control its usage.
- **External Configuration**: API keys and bot tokens are stored externally in a `BotKeys.txt` file for security.

## Prerequisites

- Python installed on your system.
- A Discord Bot Token.
- An OpenAI API Key.

## Setup

### 1. Prepare Your Environment

Ensure you have Python installed on your system. This bot was developed with Python 3.9+, so compatibility with earlier versions is not guaranteed.

### 2. Install Dependencies

Install the required Python packages by running the following command:

pip install discord openai

### 3. Configure API Keys
Create a file named BotKeys.txt in the same directory as your bot script with the following content:

GPT_TOKEN=your_openai_api_key_here
BOT_TOKEN=your_discord_bot_token_here

### 4. Bot Permissions
Ensure your bot has the following permissions in your Discord server:

Read Messages
Send Messages
Read Message History
Additionally, enable the necessary intents in the Discord Developer Portal:

#### MESSAGE CONTENT INTENT
### 5. Running the Bot
Execute the bot script with Python:

python gptbot.py

### Usage
Once the bot is running and invited to your Discord server, use it by typing commands in the designated channel:

!chatgpt <Your question or prompt here>

The bot will forward your prompt to ChatGPT and send back the generated response.

# Contributing
Contributions to this bot are welcome. Please ensure to follow best practices for code contributions and adhere to the existing coding style.

# License
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) page for details.

# Disclaimer
This project is not affiliated with OpenAI or Discord. It uses publicly available APIs from both services to demonstrate the integration capabilities. Always adhere to the terms of service for both platforms.


