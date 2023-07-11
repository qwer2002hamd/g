# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="‹ حذف ›", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="كمل", callback_data="resume_cb"),
            InlineKeyboardButton(text="وقف", callback_data="pause_cb"),
            InlineKeyboardButton(text="تخطي", callback_data="skip_cb"),
            InlineKeyboardButton(text="ايقاف", callback_data="end_cb"),
            ],
            [
            InlineKeyboardButton("‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="‹ طريقه التفعيل ›", callback_data="fallen_cb hmd"), 
        InlineKeyboardButton(text="‹ اوامر التشغيل ›", callback_data="fallen_help"),
    ],
    [
        InlineKeyboardButton(text="‹ المطور ›", user_id=config.OWNER_ID),
    ],
    [
        InlineKeyboardButton(text="‹ قـناة السورس ›", url="https://t.me/ah07v"),
    ],
]

gp_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="‹ طريقه التفعيل ›", callback_data="fallen_cb hmd"), 
        InlineKeyboardButton(text="‹ اوامر التشغيل ›", callback_data="fallen_help"),
    ],
    [
        InlineKeyboardButton(text="‹ المطور ›", user_id=config.OWNER_ID),
    ],
    [
        InlineKeyboardButton(text="‹ قـناة السورس ›", url="https://t.me/ah07v"),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="‹ اوامر القنوات ›",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="‹ اوامر المجموعه ›", callback_data="fallen_cb sudo",
        )
    ],
    [
        InlineKeyboardButton(text="‹ اوامر بالانگليزي ›", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="‹ 🔙رجوع ›", callback_data="fallen_home"),
    ],
]


help_back = [
    [
        InlineKeyboardButton(text="‹ 🔙رجوع ›", callback_data="fallen_home"),
    ],
]
