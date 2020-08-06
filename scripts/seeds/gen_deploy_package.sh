GREEN='\033[1;32m'
NC='\033[0m' # No Color

cd
source .virtualenvs/seeds/bin/activate
echo -e "${GREEN}VIRTUALENV: OK!${NC}"

#cd /tmp

cd 
cd /home/vanessa/Intelie/Projects/seeds
timestamp=$(date +%Y%m%d_%H%M%S)

tmp_dir="seedsdeploy${timestamp}"

#mkdir "$tmp_dir"

#cd $tmp_dir

source_branch=$1
new_tag=$2

echo -e "${GREEN}Branch escolhida: $source_branch ${NC}"
echo -e "${GREEN}Versão a ser criada: $new_tag ${NC}"

#Criar um novo clone sem alterações de desenvolvimento.
#git clone git@gitlab.intelie.com:petrobras/seeds.git
#cd seeds
#git submodule update --init
#git checkout $source_branch

#echo -e "${GREEN}CLONE REPOSITORY: OK!${NC}"

#Localização temporária de arquivos que são necessários para a build.
cp /home/vanessa/Intelie/Projects/seeds/fixme_uncomitted_files/build.sh /home/vanessa/Intelie/Projects/seeds/deploy
cp /home/vanessa/Intelie/Projects/seeds/fixme_uncomitted_files/Dockerfile /home/vanessa/Intelie/Projects/seeds/deploy
cp /home/vanessa/Intelie/Projects/seeds/fixme_uncomitted_files/production.txt /home/vanessa/Intelie/Projects/seeds/requirements
cp /home/vanessa/Intelie/Projects/seeds/fixme_uncomitted_files/run /home/vanessa/Intelie/Projects/seeds/tools

echo -e "${GREEN}COPY FILES: OK!${NC}"

cd tools

file_id=""
if [ -z "$new_tag" ]
then
    # Usando timestamp para identificar o arquivo pois não estamos gerando versão:
    file_id=$timestamp
else
    # Gerando versão: Criar da tag localmente e no repositório
    git tag -a $new_tag -m "Nova tag criada na versão ${new_tag}"
    git push origin --tags
    version_number=${new_tag//v}    
    file_id=$version_number
fi
echo -e "${GREEN}TAG CREATED: OK!${NC}"

# Gerar pacote:
fab build:version=$file_id
cd /tmp
sudo mv seeds-${file_id}.tar.gz ~/

echo -e "${GREEN}GENERATE BUILD: OK!${NC}"

#Limpar o diretório com o clone feito
#rm -rf $tmp_dir

#echo -e "${GREEN}REMOVE FILE: OK!${NC}"
