#!/usr/bin/env python
from collections import Counter
from functools import reduce

import click
from colorama import Fore
from github import Github, UnknownObjectException


def print_bar(iteration, total, prefix='', length=44):
    percent = round(100 * (iteration / float(total)), 1)
    filled = int(length * iteration // total)
    bar = '#' * filled + '-' * (length - filled)
    click.echo('{}{:<20}{} [{}] {:>7}% ({})'
               .format(Fore.GREEN, prefix, Fore.RESET, bar, percent, iteration))


def print_list_item(item):
    click.echo(' • {}{}{}'.format(Fore.GREEN, item, Fore.RESET))


def extract_reviewers(pull_request):
    sources = [
        set([rev.user for rev in pull_request.get_reviews() if rev.state in ['APPROVED', 'REQUEST_CHANGES']]),
        set([rev for rev in pull_request.get_review_requests()[0]]),
        set([rev for rev in pull_request.get_review_requests()[1]])
    ]
    return reduce(set.union, sources)


def display_user_counter(counter, headline):
    total_sum = sum(counter.values())
    click.echo()
    click.echo(headline)
    for item, i in sorted(counter.items(), key=lambda pair: pair[1], reverse=True):
        print_bar(i, total_sum, prefix=item.login)


@click.group()
@click.option('--token', envvar='GITHUB_TOKEN')
def cli(token):
    if not token:
        raise click.ClickException('Please provide env variable `GITHUB_TOKEN`')
    cli.token = token


@cli.command()
@click.argument('name')
@click.option('--label', 'labels', multiple=True)
@click.option('--state', default='open')
def show(name, labels, state):
    """Display reviewers stats for given repository"""
    g = Github(cli.token)

    try:
        pull_requests = g.get_repo(name).get_pulls(state)
    except UnknownObjectException:
        raise click.ClickException('Repository not found!')

    pull_requests_length = pull_requests.totalCount
    review_counter = Counter()
    creator_counter = Counter()

    if labels:
        labels = set(labels)
        pull_requests = [p for p in pull_requests if
                         labels <= set(l.name for l in p.labels)]
        pull_requests_length = len(pull_requests)

    with click.progressbar(pull_requests, length=pull_requests_length,
                           show_eta=False, label='Processing Pull Requests') as pull_requests_bar:
        for pull in pull_requests_bar:
            review_counter.update(extract_reviewers(pull))
            creator_counter.update({pull.user: 1})
    display_user_counter(review_counter, 'Reviewers ranking:')
    display_user_counter(creator_counter, 'Creators ranking:')


@cli.command()
@click.argument('name')
def labels(name):
    """Display list of labels for given repository."""
    g = Github(cli.token)
    for label in g.get_repo(name).get_labels():
        print_list_item(label.name)


@cli.command()
def repos():
    """Show list of your repos."""
    g = Github(cli.token)
    for repo in g.get_user().get_repos():
        print_list_item(repo.full_name)


if __name__ == '__main__':
    cli()
