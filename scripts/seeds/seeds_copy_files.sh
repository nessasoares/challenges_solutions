#!/bin/bash


GREEN='\033[1;32m'
NC='\033[0m' # No Color

cd ../../Intelie/Projects/seeds

#Localização temporária de arquivos que são necessários para a build.
cp fixme_uncomitted_files/build.sh deploy
cp fixme_uncomitted_files/Dockerfile deploy
cp fixme_uncomitted_files/production.txt requirements
cp fixme_uncomitted_files/run tools

cd 
cd scripts/seeds/
cp dev_pocoweb.py /home/vanessa/Intelie/Projects/seeds/seeds/settings/dev_pocoweb.py
cp dev-uwsgi.ini /home/vanessa/Intelie/Projects/seeds/dev-uwsgi.ini
cp gen_deploy_package.sh /home/vanessa/Intelie/Projects/seeds/gen_deploy_package.sh

echo -e "COPY FILES: ${GREEN}OK!${NC}"