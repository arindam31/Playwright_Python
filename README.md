# Installation

## Packages
pip intall pytest-playwright

## Browsers (this will install chromium)
playwright install

## Generate example code
playwright codegen

## Running tests and see the actual browser running
Use --headed to see the browser. Avoid to run in headless mode.

E.g: pytest test_wikipedia.py::test_has_title --headed

## Tests with report
pytest --html=report.html

## Run tests on multiple browsers
pytest test_calendar.py --browser chromium --browser webkit

## Test against mobile viewports:
pytest test_calendar.py --device="iPhone 13"

## Test with branded browsers
pytest test_calendar.py --browser-channel msedge 
Note: Longest run time was observed with this browser.