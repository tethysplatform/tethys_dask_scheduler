#!/bin/bash
coverage run --rcfile coverage.cfg setup.py test
coverage report -m
flake8