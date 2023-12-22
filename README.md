## Making a strata from this template? Your to-dos:

- Update any area marked `replace-me-strata-name` with your stratum repo name

- Update any area marked `replace-me-strata-description` with your stratum description

- Update any area marked `replace-me-folder-name` with the folder containing your stacks

- Update any area marked `your-squad` with your squad name

- .github/workflows/main.yml: runs the strata reusable workflow which will test your repo and then replicate it to CodeCommit

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