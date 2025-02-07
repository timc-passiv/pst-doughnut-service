#!/usr/bin/env bash

set -e

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
TOKEN=$(aws codeartifact get-authorization-token --domain pst-cloud-services --domain-owner "${ACCOUNT_ID}" --query authorizationToken --output text)
INDEX_URL=https://aws:${TOKEN}@pst-cloud-services-${ACCOUNT_ID}.d.codeartifact.eu-west-2.amazonaws.com/pypi/pst-cloud-services/simple/

echo $INDEX_URL

uv sync --verbose --refresh --all-packages --index "${INDEX_URL}"
