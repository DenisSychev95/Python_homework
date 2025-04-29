import json
from random import choice


def gen_person_dict():

    chars = "abcdefghijklmnopqrstuvwxyz"
    nums = "1234567890"
    key = "".join(choice(nums) for el in range(10))
    name = "".join(choice(chars) for el in range(7))
    tel = "".join(choice(nums) for el in range(10))
    person_dict = {key: {"name": name, "tel": tel}}
    return person_dict


def write_json(person_dict):
    try:
        data = json.load(open("persons_test.json"))
    except FileNotFoundError:
        data = {}
    data.update(person_dict)
    with open("persons_test.json", "w") as fw:
        json.dump(data, fw, indent=2)


for i in range(5):
    write_json(gen_person_dict())
