# Doughnut Service

This is a test service for researching using CDK for our AWS deployments.

All the code providing business logic for doughnuts (i.e. AWS Lambda handlers) lives [here](doughnut).

All the code providing scary AWS resources can be found [here](doughnut_service).

## How do I release a new version of this service?

Change the version [here](doughnut_service/pyproject.toml) and push to main - the goblins
in AWS will then build a new version and publish the artifacts to CodeArtifact.

## How do I deploy this service so that I can get a doughnut?

TODO - details to follow ASAP!