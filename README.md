# arbitrary-dateparser

Parses arbitrary strings to get dates or ranges of dates (periods). Some
of this behavior, such as whether it always returns periods, is configurable
(for now, see the code) -- that defaults to true by the way.

## Installation

- ```bash
  pip install git+https://github.com/nottheswimmer/arbitrary-dateparser@0.0.0
  ```
  Replacing `@0.0.0` with the desired version, or removing it for the latest
  
## Usage
```python
>>> from arbitrary_dateparser import DateParser
>>> parser = DateParser()
>>> parser("jul 1 to jul 7")
<Period [2019-07-01T00:00:00+00:00 -> 2019-07-07T00:00:00+00:00]>
>>> parser("today")
<Period [2019-08-02T00:00:00-04:00 -> 2019-08-02T23:59:59.999999-04:00]>
>>> parser("last week to next friday")
<Period [2019-07-22T00:00:00-04:00 -> 2019-08-09T00:00:00-04:00]>
```

As mentioned, there are a few custom parameters you can pass to the parser, 
and a few things you can override that are set in `__init__` to customize the 
behavior as well.

## Contributing

1) Fork it!
2) Clone it!
  ```bash
  git clone https://github.com/<your-fork>/arbitrary-dateparser
  cd arbitrary-dateparser
  ```
3) Install it!
  ```
  pip install -e .
  ```
  This tells pip to find setup.py in the current directory and install it in 
  editable or development mode. Editable mode means that as you make changes 
  to your local code, you’ll only need to re-install if you change the 
  metadata about the project, such as its dependencies.
4) Change it!
5) Test it!
  ```bash
  # Assumes you're in the arbitrary-dateparser directory
  python -m tests.test_dateparser
  ```
6) Submit a pull request!
