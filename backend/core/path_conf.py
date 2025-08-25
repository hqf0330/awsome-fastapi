from pathlib import Path

# 项目根目录
BASE_PATH = Path(__file__).resolve().parent.parent

# 国际化文件目录
LOCALE_DIR = BASE_PATH / 'locale'

# 日志文件路径
LOG_DIR = BASE_PATH / 'log'