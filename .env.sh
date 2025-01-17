#How to debug using vscode
##https://github.com/tiangolo/full-stack-fastapi-template/issues/503


#export USERNAME=doc1024Admin
#export FIRST_SUPERUSER_PASSWORD=iSyFZ5szgSX3JuXewBOwROiNE9HzO9Y6MEZaoi6f2h0
#export SECRET_KEY=FYtH_L7z1RQA7en1vX3KIPZVa2a1LoG7ll7TOOpWrls

#Project vars
export ENVIRONMENT=production


#Traefik Vars
export USERNAME=admin
export PASSWORD=changethis
export DOMAIN=localhost
export EMAIL=admin@example.com


#Postgres Vars
export PASSWORD=changethis
export HASHED_PASSWORD=$(openssl passwd -apr1 $PASSWORD)
echo $HASHED_PASSWORD

#Troubleshooting
##Netshoot: https://github.com/nicolaka/netshoot
###docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock nicolaka/netshoot ctop