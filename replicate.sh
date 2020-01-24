#!/bin/sh -e
apk add --no-cache git
apk add --no-cache openssh
ls -ltha

git config --global user.name "$CODECOMMIT_USER"
git config --global user.password "$CODECOMMIT_PW"
git remote add codecommit https://$CODECOMMIT_USER:$CODECOMMIT_PW@git-codecommit.eu-west-2.amazonaws.com/v1/repos/public-dns-strata
git push codecommit master