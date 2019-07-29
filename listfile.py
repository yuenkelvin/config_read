import glob

CONFIG_DIR = '/root/ASW_config/*'

onlyfiles = glob.glob(CONFIG_DIR)
print(onlyfiles)
