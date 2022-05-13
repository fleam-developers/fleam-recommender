import os
import click
import uvicorn


@click.group()
def cli():
    pass

@cli.group("runserver")
def server():
    pass

@server.command("development")
@click.option(
    "--log-level",
    default="info",
    type=click.Choice(["debug", "info", "warning", "error", "critical"]),
    help="Log level",
)
def run_server(log_level):
    uvicorn.run("src.app:app", log_level="debug", reload=True, host="0.0.0.0", port=8000)


