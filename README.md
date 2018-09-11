
<p align="center">
  <img src="assets/reviewio-logo.png" alt="bat - a cat clone with wings"><br>
  Take a sip of coffee, kick back and enjoy pull request stats from your project!
</p>


## Installation

Make sure you have python and python-pip installed.
From the project folder run:

```
sudo pip install -r requirements.txt
```

## Configuration

This tool uses `PyGithub` library for communication with GitHub. Authentication is handled by providing environmental variable `GITHUB_TOKEN` which should be generated using instructions from [github help pages](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

```
export GITHUB_TOKEN='{TOKEN}'
```

## Usage

In order to preview stats you'll need to supply project name.

Optionally you can filter by `open`, `closed` or `all` pull requests.
If you want you can also filter by `label` name.


```console
$ reviewio show django/django
Processing Pull Requests  [####################################]  100%

Reviewers ranking:
adamchainz           [#######-------------------------------------]    16.7% (2)
apollo13             [#######-------------------------------------]    16.7% (2)
charettes            [###-----------------------------------------]     8.3% (1)
MarkusH              [###-----------------------------------------]     8.3% (1)
felixxm              [###-----------------------------------------]     8.3% (1)
levidyrek            [###-----------------------------------------]     8.3% (1)
auvipy               [###-----------------------------------------]     8.3% (1)
ryanhiebert          [###-----------------------------------------]     8.3% (1)
evildmp              [###-----------------------------------------]     8.3% (1)
jarshwah             [###-----------------------------------------]     8.3% (1)
```

### Hint

You can use this super secret command to get a list of all your repositories.

```
reviewio list_repos
```
