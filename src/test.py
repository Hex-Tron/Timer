import time

from rich.progress import Progress
x=10
with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=x)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=1)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(1)
