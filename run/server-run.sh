#!/bin/bash
toolPath='/Users/rayjoy/gaojun/git/JFrame_MessageTool'
projectPath='/Users/rayjoy/gaojun/webstrom/JFrame'

apiPath=$projectPath'/app/api'
msgPath=$projectPath'/app/message/msg'
srvPath=$projectPath'/app/service'

outPath=$toolPath'/out/server'
outApiPath=$outPath'/app/api'
outMsgPath=$outPath'/app/message/msg'
outSrvPath=$outPath'/app/service'

#svn update $apiPath'/'
#svn update $msgPath'/'

python $toolPath'/src/MessageBuilder.py'

echo "...................."
echo "copy files, start..."
apiFileList=`ls $outApiPath`
for apiName in $apiFileList
do
  echo ''
  echo 'packageName='$apiName
  proApiPath=$apiPath'/'$apiName

  if [ ! -d "$proApiPath" ]; then
		mkdir "$proApiPath"
	fi

	logicFileList=`ls $outApiPath'/'$apiName`
	for logicName in $logicFileList
	do
    echo 'logicName='$logicName
	  proLogicPath=$apiPath'/'$apiName'/'$logicName
	  if [ ! -f "$proLogicPath" ]; then
	    echo 'copy '$outApiPath'/'$apiName'/'$logicName' to '$proLogicPath
      cp $outApiPath'/'$apiName'/'$logicName $proLogicPath
    else
      echo $proLogicPath' is exist, ignore'
	  fi
	done
done

echo ''
echo 'copy to '$msgPath'/'
cp $outMsgPath'/'*.js  $msgPath'/'

echo ''
echo 'copy to'$srvPath'/message.js'
cp $outSrvPath'/message.js'  $srvPath'/'
echo "copy files, end...."



