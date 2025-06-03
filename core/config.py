import toml

STANDARD_CONFIG_FILE = "pyconfig.toml"

class Config:
    """
    Cria um objeto com os dados de configuração em 'pyconfig.toml'
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def print_dict(self):
        print(self.__dict__)
            
def get_config(config_path: str = STANDARD_CONFIG_FILE) -> Config:
    config_file = toml.load(config_path)
    return Config(**config_file)