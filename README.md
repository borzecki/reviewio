<p align="center">
  <img src="https://github.com/borzecki/reviewio/raw/master/assets/reviewio-logo.png"><br>
  Provides meaningful insights into your pull requests since 2018
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

This tool uses `PyGithub` library for communication with GitHub. Authentication is handled by providing the environmental variable `GITHUB_TOKEN` which should be generated using instructions from [github help pages](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

```
export GITHUB_TOKEN='{TOKEN}'
```

## Usage

In order to calculate stats, you'll need to supply the project name.

The most basic usage:

```
$ reviewio show REPO_NAME
```

#### Filters

It's possible to filter out only the pull requests you're interested in by using following set of parameters.

| name            | options                       | default | description                                                                                                                                                                          |
| --------------- | ----------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `state`         | open, closed, all             | open    | Select only pull requests with a given state.                                                                                                                                        |
| `weight-method` | changes, simple               | changes | By default weights of pull requests are calculated based on introduced number of changes (sum of additions and deletions). Simple option counts each pull request with equal weight. |
| `younger-than`  | week, month, year, all        | month   | Taking into account pull requests younger than a specified period.                                                                                                                   |
| `label`         | labels used in the repository |         | Allows you to filter pull requests using multiple labels.                                                                                                                            |

#### Examples

```console
$ reviewio show django/django
Processing Pull Requests  [####################################]  100%

Reviewers ranking:
$ reviewio show django/django
Processing Pull Requests  [####################################]  100%

Reviewers ranking:
adamchainz             [#######-------------------------------------]    16.0% (649)
evildmp                [####----------------------------------------]    10.9% (440)
charettes              [####----------------------------------------]     9.3% (376)
auvipy                 [###-----------------------------------------]     7.7% (314)
apollo13               [###-----------------------------------------]     7.2% (290)
gilmarsoares-luizalabs [##------------------------------------------]     6.6% (268)
vitorcapuano-luizalabs [##------------------------------------------]     6.6% (268)
ariadyne-luizalabs     [##------------------------------------------]     6.6% (268)
carltongibson          [##------------------------------------------]     6.1% (248)
jarshwah               [##------------------------------------------]     5.9% (241)
felixxm                [##------------------------------------------]     4.9% (197)
MarkusH                [##------------------------------------------]     4.6% (185)
claudep                [#-------------------------------------------]     3.1% (126)
rochacbruno            [#-------------------------------------------]     2.7% (111)
ryanhiebert            [--------------------------------------------]     1.1% (46)
levidyrek              [--------------------------------------------]     0.6% (26)

Creators ranking:
orf                    [####----------------------------------------]    10.8% (2332)
evildmp                [##------------------------------------------]     5.2% (1133)
arthurio               [#-------------------------------------------]     3.7% (806)
codingjoe              [#-------------------------------------------]     3.6% (784)
chris-griffin          [#-------------------------------------------]     3.6% (770)
claudep                [#-------------------------------------------]     3.3% (713)
charettes              [#-------------------------------------------]     3.1% (674)
dspechnikov            [#-------------------------------------------]     3.0% (643)
tarkatronic            [#-------------------------------------------]     2.4% (523)
santiagobasulto        [--------------------------------------------]     2.3% (487)
atombrella             [--------------------------------------------]     2.2% (466)
luto                   [--------------------------------------------]     2.0% (440)
srinivasreddy          [--------------------------------------------]     2.0% (425)
astandley              [--------------------------------------------]     1.8% (389)
...
```

### Hint

You can use this super-secret commands:

- To get a list of repositories

```
$ reviewio repos
```

- To get a list of labels for a given repository

```
$ reviewio labels django/django
```
