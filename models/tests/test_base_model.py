#!/usr/bin/env python3
from models.base_model import BaseModel


class my_model(BaseModel):
    pass


def test_base(my_model):
    sample_model = my_model()
    sample_model.name = "my first model"
    sample_model.id = 98
    print("my first sample: ", sample_model)
    print("\n####\n")
    print(sample_model.id)
    print()
    print(type(sample_model.created_at))
    print("---")
    print()
    sample_model.save()
    print()
    print("saved model: ", sample_model)
    sample_model_json = sample_model.to_dict()
    print("Json sample: ", sample_model_json)
    print("##")
    for key in sample_model_json.keys():
        print("\t{}: ({}) - {}".format(key,
                                       type(sample_model_json[key]), sample_model_json[key]))


test_base(my_model)
