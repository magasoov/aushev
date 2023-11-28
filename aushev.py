import datetime
import logging
import threading
import os
import ctypes
from random import randint
from typing import List
from googletrans import Translator
from time import perf_counter
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
from io import StringIO
from config import *
from function import *
from time import sleep, perf_counter

logger = logging.getLogger(__name__)


def register(cb):
    cb(fake_ping())


class fake_ping(loader.Module):
    """Подпишись на @magaasov"""
    strings = {'name': 'fake ping v4'}
    
    async def write_command_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Введите текст разработчик => @magaasov")
    m = await message.reply_text("Печатает...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Загрузка...")
    await m.delete()
    await message.reply_photo(hand)

    
