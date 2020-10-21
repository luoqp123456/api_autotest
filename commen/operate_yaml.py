import yaml
from config.confi import depend_data_yaml_path


def load_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


def write_yaml(yaml_path, option, key, value):
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data[option][key] = value
    with open(yaml_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)


if __name__ == '__main__':
    # data1 = load_yaml(depend_data_yaml_path)
    # print(data1)
    # # data12 = load_json(depend_data_yaml_path)
    # # print(data12)
    # token = {'data_source_id': 999}
    #
    # # data1['test_add_fuel_card_normal'].update(token)
    # print(data1)
    # write_yaml(depend_data_yaml_path,token)
    write_yaml(depend_data_yaml_path,'data_source_121212',999)