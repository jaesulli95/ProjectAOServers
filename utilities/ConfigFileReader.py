def get_configuration(config_file, delimeter):
    config = dict()
    with open(config_file, 'r', encoding="utf8") as settings:
        for setting in settings:
            setting = setting.rstrip()
            setting_pcs = setting.split(delimeter)
            config[setting_pcs[0]] = setting_pcs[1]
    return config
