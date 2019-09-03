from random import randint
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from time import sleep


def write_msg(peer_id, attachment):
    vk.method('messages.send', {'peer_id': peer_id, 'attachment': attachment, 'random_id': randint(10 ** 6, 10 ** 9 + 7)})


token = "31f90f0ad49ad305bdc16b5ecfd1cccad1c2793775411e6a760a5bb303f8542ea9192000a87afa34c6262"
vk = vk_api.VkApi(token=token, scope="messages")
longpoll = VkBotLongPoll(vk, 181589153)
vk_api = vk.get_api()
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.from_id == 215447465:
            write_msg(event.obj.peer_id, "photo-181589153_457239018")