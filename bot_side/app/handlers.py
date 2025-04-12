import requests
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot_side.app.keyboard import inline_main, inline_category

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.reply_photo(photo='https://i0.wp.com/www.sifascorner.com/wp-content/uploads/2020/09/Best-Online'
                                    '-Clothing-Stores-for-Budget-Shopping-Sifas-Corner-2-scaled.jpg?fit=2560%2C1866'
                                    '&ssl=1',
                              caption=f'Hello, {message.from_user.full_name}!\n'
                                      f'Welcome to our clothing shop! Explore a wide range of stylish outfits, make pu'
                                      f'rchases, and enjoy a seamless shopping experience!', reply_markup=inline_main)


# Global variable to store the message ID for editing
edited_message_id = None


@router.callback_query(F.data == 'help')
async def cmd_help(callback: CallbackQuery):
    await callback.answer()
    global edited_message_id  # Use the global variable
    # Send the initial help message
    message = await callback.message.reply_photo(
        photo='https://d2vrvpw63099lz.cloudfront.net/ecommerce-chatbot/header.png',
        caption='What exactly is this bot❓\n'
                'This is a Telegram bot🤖 for shopping clothes🛒. Users👥 can browse '
                'a variety of clothing items🛍 and make purchases💵💸 directly '
                'through the chat💬'
    )
    edited_message_id = message.message_id  # Store the message ID for later editing




@router.callback_query(F.data == 'category')
async def cmd_category(callback: CallbackQuery):
    await callback.answer()
    global edited_message_id  # Use the global variable
    # Send the initial category message with inline buttons
    message = await callback.message.reply(
        "The list of categories:",
        reply_markup=await inline_category()
    )
    edited_message_id = message.message_id


categories = []
category_data = []
response = requests.get('http://127.0.0.1:8000/api/v1/category/')
for i in response.json():
    categories.append(i['id'])
    category_data.append(i)


products = []
products_url = requests.get('http://127.0.0.1:8000/api/v1/')
for product in products_url.json():
    products.append(product)


@router.callback_query(F.data)
async def handle_callback(callback: CallbackQuery):
    global edited_message_id
    try:
        callback_data = int(callback.data)

        if callback_data in categories:
            await callback.answer()

            filtered_products = [p for p in products if p['category'] == callback_data]
            keyboard = InlineKeyboardBuilder()

            if filtered_products:
                for p in filtered_products:
                    keyboard.add(InlineKeyboardButton(text=p['name'], callback_data=str(p['id'])))

                back_button = InlineKeyboardButton(text="🔙 Back", callback_data='back_to_categories')
                keyboard.add(back_button)

                if edited_message_id is not None:
                    await callback.message.bot.edit_message_text(
                        chat_id=callback.message.chat.id,
                        message_id=edited_message_id,
                        text=f"Products in {next(c['name'] for c in category_data if c['id'] == callback_data)} category:",
                        reply_markup=keyboard.as_markup()
                    )
                else:
                    edited_message = await callback.message.answer(
                        f"Products in {next(c['name'] for c in category_data if c['id'] == callback_data)} category:",
                        reply_markup=keyboard.as_markup()
                    )
                    edited_message_id = edited_message.message_id

            else:
                if edited_message_id is not None:
                    await callback.message.bot.edit_message_text(
                        chat_id=callback.message.chat.id,
                        message_id=edited_message_id,
                        text="No products found in this Category.",
                        reply_markup=None
                    )

        elif callback.data == 'back_to_categories':
            if edited_message_id is not None:
                await callback.message.bot.edit_message_text(
                    chat_id=callback.message.chat.id,
                    message_id=edited_message_id,
                    text="The list of categories:",
                    reply_markup=await inline_category()
                )

        else:
            await callback.answer("Invalid category", show_alert=True)

    except ValueError:
        await callback.answer("Invalid input", show_alert=True)


async def inline_category():
    keyboard = InlineKeyboardBuilder()
    for category in category_data:
        keyboard.add(InlineKeyboardButton(text=category['name'], callback_data=str(category['id'])))
    return keyboard.adjust(1).as_markup()