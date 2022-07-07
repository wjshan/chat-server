import typer
import uvicorn

from .config import settings
from .services import Group
import asyncio

cli = typer.Typer(name="chat_server API")



@cli.command(name="run")
def run(
        port: int = settings.server.port,
        host: str = settings.server.host,
        log_level: str = settings.server.log_level,
        reload: bool = settings.server.reload,
        worker: int = 1
):  # pragma: no cover
    """Run the API server."""
    uvicorn.run(
        "chat_server.app:app",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
        workers=worker,
    )


@cli.command()
def add_group(name: str, id: str):
    """Add new chat group"""
    asyncio.run(Group.add_group(name, id))
    print(f"created {name}@{id}")
    return
