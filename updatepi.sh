#! /usr/bin/env bash
echo it works
echo updating system pls wait
sudo apt --yes  update
echo updates completed commencing upgrade
sudo apt --yes  upgrade
echo upgrade completed cleaning...
sudo apt autoremove
echo cleaning completed installing spotyfi

while read-r  variable
do
sudo apt install variable
done <install.txt