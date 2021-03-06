from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import vk_api

token = "YOUR_TOKEN"

def write_msg(user_id, message, random_id):
    vk.messages.send(
        user_id=user_id,
        random_id=0,
        message=message,
    )

def write_k_msg(user_id, message, random_id, keyboard):
    vk.messages.send(
        user_id=user_id,
        random_id=0,
        message=message,
        keyboard=keyboard
    )

def getrealuid(user_id):
    res = vk.users.get(
        user_ids=user_id
    )
    real_uid = res[0]['id']
    return real_uid

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session, mode=2)


            
