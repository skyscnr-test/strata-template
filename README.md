## template-strata readme
- .catalog.yml      - update component info with your strata info

- .drone.yml        - ensure replicate step has your repo name and add tests here.

- requirements.txt  - make sure this is up to date - cdk should be at least 1.55.0, and add in any requirements here that your project needs specifically.

- app.py                            - replace all occurrences of template with your strata name.

- cdk.json          -  this is the CDK metadata and normally doesn't require modification

## Environment Vars
export AWS_REGION=eu-west-2


## Requirements for test
``` 
nvm install 14.11

npm install -g aws-cdk

pip install -r requirements.txt

cdk diff

You can check cdk version and config with 

cdk doctor
```

For further questiond please flag @cassini-gf 