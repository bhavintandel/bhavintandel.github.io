"""
Script to manage blogs.
"""

import click
import os
from shutil import copyfile
import subprocess


BLOG_BUCKET_NAME = "exploring-ml-tools"
REGION = "eu-west-2"


@click.group()
def cli():
    """
    Main class to manage blogs development.

    :return:
    """

    print("Context of the main.")


@cli.command()
@click.argument('name')
def init(name):
    """
    Initialize the blog creation

    :return:
    """

    if os.path.exists(name):
        print("Blog with name {name} already exists.".format(name=name))
        exit()
    else:
        print("Initializing project {project_name}.".format(project_name=name))
        os.makedirs(os.path.join(name, 'assets'))
        copyfile("blogs-template.md", os.path.join(name, "exploring-ml-tools-{name}.md".format(name=name)))


@cli.command()
def sync_s3():
    """
    Sync exploring ml tool to s3

    :return:
    """

    subprocess.run(["aws", "s3", "sync", "./", "s3://{0}".format(BLOG_BUCKET_NAME)])


if __name__ == "__main__":
    cli()
