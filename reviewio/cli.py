#!/usr/bin/env python
import click
from github import Github
from colorama import Fore
from functools import reduce
from collections import Counter


def print_bar(iteration, total, prefix='', length=44):
    percent = round(100 * (iteration / float(total)), 1)
    filled = int(length * iteration // total)
    bar = '#' * filled + '-' * (length - filled)
    click.echo('{}{:<20}{} [{}] {:>7}% ({})'\
         .format(Fore.GREEN, prefix, Fore.RESET, bar, percent, iteration))

def extract_reviewers(pull_request):
    sources = [
        set([ rev.user for rev in pull_request.get_reviews() if rev.state in ['APPROVED', 'REQUEST_CHANGES']]),
        set([ rev for rev in pull_request.get_review_requests()[0]]),
        set([ rev for rev in pull_request.get_review_requests()[1]])
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
@click.option('--label')
@click.option('--state', default='open')
def show(name, label, state):
    """Display reviewers stats for given repository"""
    if not name:
        raise click.ClickException('Provide repository name')

    g = Github(cli.token)
    my_id = g.get_user().id
    pull_requests = g.get_repo(name).get_pulls(state)
    pull_requests_length = pull_requests.totalCount
    review_counter = Counter()
    creator_counter = Counter()

    if label:
        pull_requests = [p for p in pull_requests if
                         any(filter(lambda l: l.name == label, p.labels))]
        pull_requests_length = len(pull_requests)
    with click.progressbar(pull_requests, length=pull_requests_length,
                           show_eta=False, label='Processing Pull Requests') as pull_requests_bar:
        for pull in pull_requests_bar:
            review_counter.update(extract_reviewers(pull))
            creator_counter.update({pull.user:1})
    display_user_counter(review_counter, 'Reviewers ranking:')
    display_user_counter(creator_counter, 'Creators ranking:')

@cli.command()
def list_repos():
    """Show list of your repos."""
    g = Github(cli.token)
    for repo in g.get_user().get_repos():
        click.echo(repo.name)

if __name__ == '__main__':
    cli()
