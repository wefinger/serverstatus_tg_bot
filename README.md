# serverstatus_tg_bot

一个新手写的serverstatus对接TG的机器人，非职业程序员，完全个人喜好。代码质量很差，自用。

## 使用说明
> 本项目仅仅完成了serverstatus与TG机器人的对接，所以任何serverstatus引起的问题均无法解决。

### 使用条件

- TG_BOT密钥一枚，自行前往@BotFather处申请
- python3.6+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)库
- requests库
``
> 推荐使用`pip install pyTelegramBotAPI requests` 安装两个第三方库

运行项目前请在项目目录下新建`config.py`文件，并包含以下内容：

```python
# TG_BOT密钥
TOKEN = '@BotFather 处申请到的bot密钥'

# SERVERSTATUS服务端json地址
JSON_URL = "https://serverstatus地址/json/stats.json"

# v2订阅地址
V2_RSS_URL = "您的自定义订阅地址"
```