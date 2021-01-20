# cd to a folder that you want to create the virtual env
# ...

# create virtual env
python3 -m venv virtual_env_rest_api

# actiavte the virtual env (to deactiavte, run 'deactiavte')
. virtual_env_rest_api/bin/activate

# install django (it will be installed in virtual_env_rest_api/lib/python3.6/dist-packages)
pip3 install django
