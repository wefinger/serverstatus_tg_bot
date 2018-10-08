#!/usr/bin/python
# coding utf-8

import requests
import base64
import time
from random import choice
from config import JSON_URL,V2_RSS_URL


# 读取serverstatus节点信息，格式化输出
# 旧版格式
def server_base_info():
    json_content = requests.get(JSON_URL).json()
    req = []
    for i in json_content['servers']:
        if i['online4'] == True:
            traffic_in = round(int(i['network_in'])/(1024**3),2)
            traffic_out = round(int(i['network_out'])/(1024**3),2)
            traffic = str(traffic_in) + 'G/' + str(traffic_out) + 'G'
            req.append("{name}\n    状态：{online4}\n    下行：{traffic_in}G \n    上行：{traffic_out}G \n".format(name="*" + i['name'] + "*",online4="`"+str(i['online4'])+"`",traffic_in=traffic_in,traffic_out=traffic_out))
        else:
            req.append("{name}\n"
                       "    状态：{online4}"
                       .format(name="*" + i['name'] + "*",online4="已离线，具体原因请咨询管理员\n"))
    last_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(json_content['updated'])))
    return "最后更新时间：{last_time}\n".format(last_time=last_time)+"".join(req)

# 新版输出格式
def server_base_info_2():
    json_content = requests.get(JSON_URL).json()
    req = []
    for i in json_content['servers']:
        if i['online4'] == True:
            traffic_in = round(int(i['network_in'])/(1024**3),2)
            traffic_out = round(int(i['network_out'])/(1024**3),2)
            traffic = str(traffic_in) + 'G/' + str(traffic_out) + 'G'
            req.append("{name}-{online4}-{traffic_out}G\n".format(name="*" + i['name'] + "*",online4="`"+str(i['online4'])+"`",traffic_out=traffic_out))
        else:
            req.append("{name}"
                       "-{online4}"
                       .format(name="*" + i['name'] + "*",online4="`OFF`\n"))
    last_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(json_content['updated'])))
    return "最后更新时间：{last_time}\n".format(last_time=last_time)+"".join(req)

# 读取具体节点信息
def get_node_details(node_name):
    json_content = requests.get(JSON_URL).json()
    for i in json_content['servers']:
        if i['name'] == node_name:
            if i['online4'] == True:
                if i['network_rx'] > 1000*1024:
                    network_rx = str(round(int(i['network_rx']) / (1024 ** 2), 2)) + "MB/S"
                else:
                    network_rx = str(round(int(i['network_rx']) / (1024 ** 1), 2)) + "KB/S"
                if i['network_tx'] > 1000*1024:
                    network_tx = str(round(int(i['network_tx']) / (1024 ** 2), 2)) + "MB/S"
                else:
                    network_tx = str(round(int(i['network_tx']) / (1024 ** 1), 2)) + "KB/S"
                traffic_in = round(int(i['network_in']) / (1024 ** 3), 2)
                traffic_out = round(int(i['network_out']) / (1024 ** 3), 2)
                return "{name}\n" \
                       "    状态：{online4}\n" \
                       "    虚拟化：{type}\n" \
                       "    开机时间：{uptime}\n" \
                       "    负载：{load}\n" \
                       "    实时下行：{network_rx}\n" \
                       "    实时上行：{network_tx}\n" \
                       "    总下行：{traffic_in}G\n" \
                       "    总上行：{traffic_out}G\n"\
                    .format(name="*" + i['name'] + "*",online4="`"+str(i['online4'])+"`",type=i['type'],uptime=i['uptime'],load=i['load'],network_rx=network_rx,network_tx=network_tx,traffic_in=traffic_in,traffic_out=traffic_out)
            else:
                return "{name}\n" \
                       "    状态：{online4}" \
                       .format(name="*" + i['name'] + "*",online4="已离线，具体原因请咨询管理员")
    return "暂无此节点，请告诉我正确的节点名。"

# 读取订阅信息
def get_v2(type="rand"):
    if type == "url":
        return "订阅地址：{}\n".format(V2_RSS_URL)
    else:
        all_node = str(base64.b64decode(requests.get(V2_RSS_URL).text),'utf8').split("\n")
        return "随机节点：\n"+choice(all_node)+"\n获取全部节点请使用`url`参数"

if __name__ == '__main__':
    print(server_base_info())