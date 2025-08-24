from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.text import Text

from backend import console
from backend.core.registrar import register_app
from backend.utils.timezone import timezone

_log_prefix = f'{timezone.to_str(timezone.now(), "%Y-%m-%d %H:%M:%S.%M0")} | {"INFO": <8} | - | '

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    console=console,
) as progress:
    console.print("do somethins")

console.print(Text(f'{_log_prefix}启动服务...', style='bold magenta'))

app = register_app()