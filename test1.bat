SERVER="172.17.0.56"
USR="ut"
ssh $USR@$SERVER

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

if [ -e /tomcat/webapps/ROOT.war ]
then
    sudo rm -rf /tomcat/webapps/ROOT.war
fi
if [ -d /tomcat/webapps/ROOT ]
then
    sudo rm -rf /tomcat/webapps/ROOT
fi
echo Enter build date
read build_date
scp ut@172.17.20.32:/stable-builds/PackingList/master-$build_date/artifacts/PackingList1-5.war /tomcat/webapps/ROOT.war
sleep 15
cp -R /tomcat/webapps/ROOT /home/ut/ALL_FILES/RUN/webapps/ROOT/
sudo python /home/ut/ALL_FILES/RUN/EPL-Config.py
rm -R /home/ut/deploy/*
cp -a /home/ut/ALL_FILES/RUN/webapps/ROOT/. /home/ut/deploy/
cd /home/ut/
sudo bash new_test.sh
echo Done