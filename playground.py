
"""

descriptions = {"at_entity": [
        {
        "afternoon_morning_and_night": {
            "rain_and_sun": {
                "bad" :["test1"]
            }
        }
    },
{
        "rain": {
            "noon_andnight": {
                "good_or_bad" :["test2"]
            }
        }
    },
    ]
}
import random
current_time = "noon"
current_weather = "rain"
current_vibe = "bad"
def get_description(descriptions_dic, description_type):
    description_to_return = []
    for descriptions_dic in descriptions.get(description_type):
        if not descriptions_dic:
            raise ValueError("test123")
        while isinstance(descriptions_dic, dict):
            for desc_key, nested_dic in descriptions_dic.items():
                if current_time in desc_key:
                    descriptions_dic = nested_dic
                if current_weather in desc_key:
                    descriptions_dic = nested_dic
                if current_vibe in desc_key:
                    descriptions_dic = nested_dic
        description_to_return.append(random.choice(descriptions_dic))
    return description_to_return

print(get_description(descriptions, "at_entity"))

"""

import random

descriptions = {
    "at_entity": [
        {
            "afternoon_morning_and_night": {
                "rain_and_sun": {
                    "bad": ["test1"]
                }
            }
        },
        {
            "rain": {
                "noon_and_night": {
                    "good_or_bad": ["test2"]
                }
            }
        },
    ]
}

current_time = "noon"
current_weather = "rain"
current_vibe = "bad"


def get_description(descriptions_dic, description_type):
    description_to_return = []

    for description_entry in descriptions_dic.get(description_type, []):
        current_dic = description_entry
        while isinstance(current_dic, dict):
            found = False
            for desc_key, nested_dic in current_dic.items():
                if (current_time in desc_key or
                        current_weather in desc_key or
                        current_vibe in desc_key):
                    current_dic = nested_dic
                    found = True
                    break
            if not found:
                break

        if isinstance(current_dic, list):
            description_to_return.append(random.choice(current_dic))

    return description_to_return


print(get_description(descriptions, "at_entity"))