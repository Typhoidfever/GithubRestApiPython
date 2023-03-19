#!/bin/bash

REPORT_PATH="$PWD/Report"
pytest --alluredir "$REPORT_PATH"
allure serve "$REPORT_PATH"
