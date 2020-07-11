#!/usr/bin/env bash

until cd app && pip3 install -r test.txt && export FLASK_ENV=development && flask run --host=0.0.0.0
do
    echo "Retrying  install"
done

