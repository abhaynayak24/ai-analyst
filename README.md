# ai-analyst

## Pre-requisits

python version >= 3.9
docker

## create virtual env
python3 -m venv venv
source venv/bin/activate

## Run setup script
sh setup.sh

The setup script will download latest docker mysql image and load sample database into it. You can then run prompts against the data loaded in pandas frame from the mysql db.