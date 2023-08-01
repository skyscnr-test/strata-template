## Making a strata from this template? Your to-dos:

- Update any area marked `replace-me` with your stratum repo name and / or stratum description

- Update any area marked `your-squad` with your squad name

- .drone.yml: ensure you _keep_ the replicate step as this is what triggers deployment

- app.py: replace all occurrences of `template` with your stratum name

- .catalog.yml: update all the information here so that Tower is updated

- Dockerfile: update the folder name on this line `ADD --chown=skyscanner ./template ./template`

## Other files of note

- requirements.txt: this is generated with `make freeze`

- cdk.json: this is the CDK metadata and normally doesn't require modification

- local_config.yml: contains instructions on which account to diff changes against (usually will be a test account)

## Environment Vars
export AWS_REGION=eu-west-2


## Running tests locally
``` 
make artifactory-login
make freeze-dev
make build
make test-ci
```

For further questions please raise a ticket with Cassini GF