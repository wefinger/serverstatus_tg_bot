import telebot
import logging
import function
from config import TOKEN
# 生产api
bot = telebot.TeleBot(TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

# start信息
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '我是233blog共享节点监控机器人')

# ping响应，检测机器人在线状态
@bot.message_handler(commands=['ping'])
def ping_pong(message):
    bot.send_message(reply_to_message_id=message.message_id, parse_mode="Markdown", chat_id=message.chat.id, text="`pong`")

# 获取节点服务器状态
@bot.message_handler(commands=['status'])
def send_status(message):
    message_text = message.text.split(' ')
    if len(message_text) == 1: # 无参数获取全部状态
        # 旧版
        # bot.send_message(reply_to_message_id=message.message_id, parse_mode="Markdown", chat_id=message.chat.id, text=function.server_base_info())
        # 新版
        bot.send_message(reply_to_message_id=message.message_id, parse_mode="Markdown", chat_id=message.chat.id, text=function.server_base_info_2())
    else: # 有参数，获取对应服务器详细状态
        del message_text[0]
        node_name = message_text[0]
        bot.send_message(reply_to_message_id=message.message_id, parse_mode="Markdown", chat_id=message.chat.id,
                         text=function.get_node_details(node_name))

# 获取节点信息
@bot.message_handler(commands=["get"])
def send_v2(message):
    message_text = message.text.split(' ')
    if len(message_text) == 1: # 获取随机节点
        bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id,
                         text=function.get_v2())
    else: # 获取订阅地址
        bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id,
                         text=function.get_v2(message_text[1]))

if __name__ == '__main__':
    # 出现异常无脑重启主程序
    def main_process():
        try:
            bot.polling(none_stop=True)
        except:
            main_process()
    
    main_process()