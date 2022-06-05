#!/usr/bin/env bash
virtualenv .virtualenv/`basename $(pwd)`
source .virtualenv/`basename $(pwd)`/bin/activate
