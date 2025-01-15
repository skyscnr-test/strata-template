FROM 325714046698.dkr.ecr.eu-west-1.amazonaws.com/skyscanner/node-edge:1.6.2 as node
FROM 325714046698.dkr.ecr.eu-west-1.amazonaws.com/skyscanner/python-edge:3.3.0


ARG ENV

USER root

COPY --from=node /usr/bin/exec_node /usr/bin/exec_node
COPY --from=node /usr/local/bin/node_bare /usr/local/bin/node_bare
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=node /usr/bin/options_parser /usr/bin/options_parser
RUN ln -s /usr/bin/exec_node /usr/local/bin/node && \
	ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm

USER skyscanner

COPY --chown=skyscanner \
	pip.conf \
	.npmrc /home/skyscanner/

RUN mkdir $SKYSCANNER_HOME/app
WORKDIR $SKYSCANNER_HOME/app
COPY --chown=skyscanner \
	app.py \
	requirements.txt \
	requirements-dev.txt \
	package.json \
	package-lock.json \
	cdk.json ./
ADD --chown=skyscanner ./replace-me-folder-name ./replace-me-folder-name

RUN PIP_CONFIG_FILE=/home/skyscanner/pip.conf pip install -r requirements.txt --compile
RUN if [ "$ENV" = "local" ]; then PIP_CONFIG_FILE=/home/skyscanner/pip.conf pip install -r requirements-dev.txt --compile; fi
RUN npm install --verbose
RUN rm -f /home/skyscanner/pip.conf /home/skyscanner/.npmrc

ENV PATH="$PATH:$SKYSCANNER_HOME/app/node_modules/aws-cdk/bin"

CMD strata ${ACTION}
