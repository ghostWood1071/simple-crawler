from util.config_generator import ConfigGenerator
import sys

if __name__ == "__main__":
    # config_path = sys.argv[1]
    config_path =  "config\generator\config.json"
    generator = ConfigGenerator(config_path)
    generator.load_config()
    generator.execute()