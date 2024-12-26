import time
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, FloodWaitError
from telethon.tl.types import PeerUser

# Constants
API_ID = ''  # Replace with your own API ID
API_HASH = ''  # Replace with your own API Hash
PHONE_NUMBER = ''  # Replace with your phone number

# Initialize the client
client = TelegramClient('session_name', API_ID, API_HASH)

async def send_message_to_users():
    # Read the message from the message.txt file
    with open('message.txt', 'r', encoding='utf-8') as f:
        message = f.read().strip()

    # Read usernames from usernames.txt file
    with open('usernames.txt', 'r', encoding='utf-8') as f:
        usernames = [line.strip() for line in f.readlines() if line.strip()]

    # Loop through the usernames and send the message
    for username in usernames:
        try:
            # Get user information by username
            user = await client.get_entity(username)
            
            # Send the message
            await client.send_message(user, message)
            print(f"Message sent to {username}")

            # Wait for 300 seconds before sending the next message
            time.sleep(300)

        except FloodWaitError as e:
            print(f"Flood wait error, sleeping for {e.seconds} seconds")
            time.sleep(e.seconds)

        except Exception as e:
            print(f"Error sending message to {username}: {e}")

async def main():
    # Start the client session
    await client.start(phone=PHONE_NUMBER)

    # Send messages
    await send_message_to_users()

# Run the client
client.loop.run_until_complete(main())
