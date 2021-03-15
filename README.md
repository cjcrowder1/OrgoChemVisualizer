![47d984de31e64f669c95f8e403c3d202](https://user-images.githubusercontent.com/71831387/110709907-fc3a7b00-81ca-11eb-90d0-c10a076c5330.png)

# OrgoChemVisualizer

[![Documentation Status](https://readthedocs.org/projects/orgochemvisualizer/badge/?version=latest)](https://orgochemvisualizer.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/cjcrowder1/OrgoChemVisualizer.svg?branch=main)](https://travis-ci.com/cjcrowder1/OrgoChemVisualizer)

This code is used to visualize chemical reactions from Organic Chemistry. It is intended to be a teaching tool for college students taking undergraduate Organic Chemistry.

## Usage

## Installations

## Screenshots

## Development / Contributing

Make sure you are in the top-level directory ("OrgoChemVisualizer"). 

To run the main program, type (`$` refers to command line prompt)

`$ python orgochemvisualizer`

To run all unit tests, type

`$ python -m unittest -v`

(the `-v` option stands for "verbose" and lists each test that is run)

We will eventually probably use sphynx for documentation. 

### To run local server for online interface

Start the built-in Python HTTP server by

`$ python -m http.server`

The default port is 8000. To specify another port, e.g. 8080:

`$ python -m http.server 8080`

Then load http://localhost:<port>/index.html in the browser address bar. This will display the website as would be rendered online.
