from invoke import task
from pathlib import Path
from os import path, chdir

abs_path = str(Path(__file__).parent)

PURPLE = '\033[0;35m'
NC = '\033[0m'


def print_color(color, text):
    print(color + text + NC)


@task
def build(ctx, type):
    print(type)
    if type != "en" and type != "cz":
        print_color(PURPLE, "No documentation build was selected! (pick: en, cz)")
        return

    build_dir = path.join(abs_path, f"docs/{type}/")
    doclink = path.join(abs_path, f"docs/{type}/build/html/index.html")

    chdir(build_dir)

    print_color(PURPLE, f"Building {type} documentation...")
    ctx.run("make html", pty=True)
    print_color(PURPLE, f"Done, link here: {doclink}")
