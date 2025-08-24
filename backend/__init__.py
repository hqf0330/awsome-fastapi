from backend.utils.console import console

__version__ = '1.0.0'

def get_version() -> str | None:
    console.print(f'[cyan]{__version__}[/]')