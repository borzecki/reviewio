
<p align="center">
  <img src="assets/reviewio-logo.png"><br>
  Take a sip of coffee, kick back and enjoy pull request stats from your project!
</p>


## Installation

### System

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```
$ pip install reviewio
```

Reviewio supports Python 3.4 and newer.

### Local and development

Make sure you have python and python-pip installed.
From the project folder run:

```
$ pip install -r requirements.txt
```

## Configuration

This tool uses `PyGithub` library for communication with GitHub. Authentication is handled by providing environmental variable `GITHUB_TOKEN` which should be generated using instructions from [github help pages](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

```
export GITHUB_TOKEN='{TOKEN}'
```

## Usage

In order to preview stats you'll need to supply project name.

Optionally you can filter by `open`, `closed` or `all` pull requests using `state` parameter.
If you want you can also filter by multiple labels by passing `label`.


```console
$ reviewio show django/django
Processing Pull Requests  [####################################]  100%

Reviewers ranking:
adamchainz           [######--------------------------------------]    15.4% (2)
apollo13             [######--------------------------------------]    15.4% (2)
jeffyancey           [###-----------------------------------------]     7.7% (1)
charettes            [###-----------------------------------------]     7.7% (1)
felixxm              [###-----------------------------------------]     7.7% (1)
MarkusH              [###-----------------------------------------]     7.7% (1)
levidyrek            [###-----------------------------------------]     7.7% (1)
auvipy               [###-----------------------------------------]     7.7% (1)
ryanhiebert          [###-----------------------------------------]     7.7% (1)
evildmp              [###-----------------------------------------]     7.7% (1)
jarshwah             [###-----------------------------------------]     7.7% (1)

Creators ranking:
claudep              [##------------------------------------------]     6.0% (9)
charettes            [#-------------------------------------------]     3.4% (5)
orf                  [#-------------------------------------------]     3.4% (5)
sir-sigurd           [--------------------------------------------]     2.0% (3)
jschneier            [--------------------------------------------]     2.0% (3)
codingjoe            [--------------------------------------------]     2.0% (3)
Windsooon            [--------------------------------------------]     1.3% (2)
alexh546             [--------------------------------------------]     1.3% (2)
...
```

### Hint

You can use this super secret commands:

* To get list of repositories

```
$ reviewio repos
```

* To get list of labels for given repository

```
$ reviewio labels django/django
```
