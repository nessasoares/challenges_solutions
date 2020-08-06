#!/bin/bash

echo "INIT RELOAD DATABASE..."

cd $HOME/Intelie/Projects/seeds

psql -U postgres -c 'drop database seeds_dev_3;'; 
psql -U postgres -c 'create database seeds_dev_3;'; 


zcat ../../dumps/dump_seeds_qa-2020-06-17.sql.gz | psql -U postgres seeds_dev_3; 
#zcat ../../dumps/seeds-dump-20200701.gz | psql -U postgres seeds_dev; 
python manage.py migrate facts; 

#python manage.py createsuperuser; 
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('vanessa', '', '123')" | python manage.py shell


clear

## colors
GREEN='\033[1;32m'
NC='\033[0m' # No Color

echo -e "CREATE AND DROP DATABASE: ${GREEN}OK!${NC}" 
echo -e "MIGRATE RECORDS: ${GREEN}OK!${NC}" 
echo -e "MIGRATE FACTS: ${GREEN}OK!${NC}"
echo -e "CREATE SUPER USER DJANGO: ${GREEN}OK!${NC}" 

./seeds_copy_files.sh

echo -e "RUNNING DJANGO PROJECT: ${GREEN}SEEDS${NC}" 

#python manage.py runserver localhost:8001 --settings=seeds.settings.development
