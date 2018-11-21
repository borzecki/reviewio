
<p align="center">
  <img src="https://github.com/borzecki/reviewio/raw/master/assets/reviewio-logo.png"><br>
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

By default weights of pull requests are calculated based on introduced number of changes (sum of additions and deletions).
However you can specify this method explicitly using `--weight-method` option.


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

You can use this super secret commands:

* To get list of repositories

```
$ reviewio repos
```

* To get list of labels for given repository

```
$ reviewio labels django/django
```
