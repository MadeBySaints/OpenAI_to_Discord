import discord
import openai
from discord.ext import commands

# Function to read tokens from BotKeys.txt
def read_tokens():
    tokens = {}
    with open('BotKeys.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            tokens[key] = value
    return tokens

# Read tokens
tokens = read_tokens()
openai.api_key = tokens['GPT_TOKEN']

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Make sure to enable this in the Discord Developer Portal

# Initialize the Discord bot with the specified command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def chatgpt(ctx, *, prompt):
    # Restrict bot to a specific channel
    if ctx.channel.id == 'your_channel_id_here':
        try:
            # Call OpenAI API with the user's prompt
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=10,
                temperature=0.1
            )
            # Send the response back to the Discord channel
            await ctx.send(response.choices[0].text.strip())
        except openai.error.RateLimitError as e:
            # Log rate limit errors to the console
            print(f"Rate limit exceeded: {e}")
        except openai.error.OpenAIError as e:
            # Log other OpenAI API errors to the console
            print(f"OpenAI API error: {e}")
        except Exception as e:
            # Log unexpected errors to the console
            print(f"Unexpected error: {e}")

# Run the bot using your Discord bot token read from BotKeys.txt
bot.run(tokens['BOT_TOKEN'])
