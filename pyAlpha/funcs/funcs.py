from telethon import events

# Custom function for advanced filtering
def alpha_cmd(patterns=None, **kwargs):
    owner_only = kwargs.get("owner_only", False)
    groups_only = kwargs.get("groups_only", False)
    admins_only = kwargs.get("admins_only", False)
    # Add more custom filter options as needed

    def decorator(func):
        async def wrapper(event):
            # Custom filtering logic goes here
            # Check the event properties and filter messages based on your requirements

            # Example: Check the event type and apply filters accordingly
            if isinstance(event, events.NewMessage):
                # Check if the message is from a group
                if groups_only and not event.is_group:
                    return

                # Check if the message is from an admin or the group creator
                if admins_only and not (event.chat.admin_rights or event.chat.creator):
                    return

                # Check if the message is from the owner or a sudo user
                if owner_only or sudo_users_only:
                    user_id = event.sender_id
                    if user_id not in owner_and_sudos():
                        return

                # Check if the message matches any of the specified patterns
                if patterns and event.message:
                    message_lower = event.message.message.lower()
                    if not any(pat in message_lower for pat in patterns):
                        return

            elif isinstance(event, events.CallbackQuery):
                # Add filtering logic for CallbackQuery events
                pass

            elif isinstance(event, events.InlineQuery):
                # Add filtering logic for InlineQuery events
                pass

            # Add filtering logic for other event types if needed

            # If the event passes all custom filters, call the original event handler function
            await func(event)

        # Add the custom filter as an event handler with the specified parameters
        events.dispatcher.add_event_handler(wrapper, events.NewMessage(**kwargs))
        events.dispatcher.add_event_handler(wrapper, events.CallbackQuery(**kwargs))
        events.dispatcher.add_event_handler(wrapper, events.InlineQuery(**kwargs))

        # Add more event handlers for other event types if needed

    return decorator

'''# Example
@custom_filter(patterns=['/hello', '/hi'], owner_only=True, groups_only=True)
async def hello_handler(event):
    await event.reply("Hello!")

# Start the client
client.start()
client.run_until_disconnected()'''
