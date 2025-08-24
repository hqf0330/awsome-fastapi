import asyncio
from dataclasses import dataclass
from typing import Annotated

from watchfiles import PythonFilter
from backend.core.conf import settings
from rich.panel import Panel
from rich.text import Text

import granian
import cappa

from backend import console, get_version

class CustomReloadFilter(PythonFilter):
    """
    自定义重载过滤器
    """
    def __init__(self):
        super().__init__(extra_extensions=['.json', '.yaml', '.yml'])

    
def run(host: str, port: int, reload: bool, workers: int | None) -> None:
    url = f'http://{host}:{port}'
    docs_url = url + settings.FASTAPI_DOCS_URL
    redoc_url = url + settings.FASTAPI_REDOC_URL
    openapi_url = url + (settings.FASTAPI_OPENAPI_URL or "")

    panel_content = Text()
    panel_content.append(f'📝 Swagger 文档: {docs_url}\n', style='blue')
    panel_content.append(f'📚 Redoc   文档: {redoc_url}\n', style='yellow')
    panel_content.append(f'📡 OpenAPI JSON: {openapi_url}\n', style='green')
    panel_content.append(
        '🌍 fba 官方文档: https://fastapi-practices.github.io/fastapi_best_architecture_docs/',
        style='cyan',
    )

    console.print(Panel(panel_content, title='fba 服务信息', border_style='purple', padding=(1, 2)))

    granian.Granian(
        target='backend.main:app',
        interface='asgi',
        address=host,
        port=port,
        reload=not reload,
        reload_filter=CustomReloadFilter,
        workers=workers or 1
    ).serve()


@cappa.command(help='运行 API 服务')
@dataclass
class Run:
    host: Annotated[
        str,
        cappa.Arg(
            long=True,
            default='127.0.0.1',
            help='提供服务的主机 IP 地址，对于本地开发，请使用 `127.0.0.1`。'
                 '要启用公共访问，例如在局域网中，请使用 `0.0.0.0`',
        ),
    ]
    port: Annotated[
        int,
        cappa.Arg(long=True, default=8000, help='提供服务的主机端口号'),
    ]
    no_reload: Annotated[
        bool,
        cappa.Arg(long=True, default=False, help='禁用在（代码）文件更改时自动重新加载服务器'),
    ]
    workers: Annotated[
        int | None,
        cappa.Arg(long=True, default=None, help='使用多个工作进程，必须与 `--no-reload` 同时使用'),
    ]

    def __call__(self):
        run(host=self.host, port=self.port, reload=self.no_reload, workers=self.workers)


@cappa.command(help='一个高效的 fba 命令行界面')
@dataclass
class FbaCli:
    version: Annotated[
        bool,
        cappa.Arg(short='-V', long=True, default=False, show_default=False, help='打印当前版本号'),
    ]
    subcmd: cappa.Subcommands[Run | None] = None  # 只保留 Run 命令

    async def __call__(self):
        if self.version:
            get_version()

def main() -> None:
    output = cappa.Output(error_format='[red]Error[/]: {message}\n\n更多信息，尝试 "[cyan]--help[/]"')
    asyncio.run(cappa.invoke_async(FbaCli, output=output))