from backend.utils.console import console
from backend.common.i18n import i18n

__version__ = '1.0.0'


def get_version() -> None:
    console.print(f'[cyan]{__version__}[/]')

i18n.load_locales()