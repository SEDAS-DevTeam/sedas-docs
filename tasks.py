from invoke import task
from pathlib import Path
from os import path, chdir

import shutil
import yaml

from inference import Translator, RstIterator

abs_path = str(Path(__file__).parent)

PURPLE = '\033[0;35m'
NC = '\033[0m'


def print_color(color, text):
    print(color + text + NC)


def input_color(color, text):
    return input(color + text + NC)


def read_yaml_config(path):
    with open(path) as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(e)


def write_yaml_config(path, content):
    with open(path, "w") as file:
        yaml.dump(content, file, default_flow_style=False)


@task
def build(ctx, type):
    if type != "en" and type != "cs":
        print_color(PURPLE, "No documentation build was selected! (pick: en, cs)")
        return

    build_dir = path.join(abs_path, f"docs/{type}/")
    doclink = path.join(abs_path, f"docs/{type}/build/html/index.html")

    chdir(build_dir)

    print_color(PURPLE, f"Building {type} documentation...")
    ctx.run("make html", pty=True)
    print_color(PURPLE, f"Done, link here: {doclink}")


@task
def create_translation(ctx, type):
    en_doc_path = path.join(abs_path, "docs/en")
    sel_doc_path = path.join(abs_path, f"docs/{type}")

    print_color(PURPLE, "Copying resource files...")
    shutil.copytree(en_doc_path, sel_doc_path)

    print_color(PURPLE, "Changing configurations...")
    config_path = path.join(sel_doc_path, ".readthedocs.yaml")
    trans_config = read_yaml_config(config_path)

    # change some keys in translation config
    trans_config["python"]["install"][0]["requirements"] = f"docs/{type}/requirements.txt"
    trans_config["sphinx"]["configuration"] = f"docs/{type}/source/conf.py"

    write_yaml_config(config_path, trans_config)

    print_color(PURPLE, "Running model inference for automatic translation...")

    rst_sources_path = path.join(sel_doc_path, "source")
    model = Translator(type)
    iterator = RstIterator(rst_sources_path)
    iterator.iterate(model)

    print_color(PURPLE, "Done!")


@task
def delete_translation(ctx, type):
    print_color(PURPLE, f"Deleting translation: {type}")

    sel_doc_path = path.join(abs_path, f"docs/{type}")
    if input_color(PURPLE, f"Are you sure you want to remove {type}? (y/n): ") == "y": shutil.rmtree(sel_doc_path)
    else: print_color(PURPLE, "Operation cancelled by user")
