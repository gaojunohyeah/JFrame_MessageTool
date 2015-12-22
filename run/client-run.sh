#!/bin/bash
toolPath='/Users/rayjoy/gaojun/git/JFrame_MessageTool'
projectPath='/Users/rayjoy/gaojun/webstrom/JFrame_Client'

jsPath=$projectPath'/www/js'

outPath=$toolPath'/out/client/www/js'

#svn update $jsPath'/'
#git pull $toolPath
#git pull $projectPath

python $toolPath'/src/MessageBuilder.py'

echo "...................."
echo "copy files, start..."
echo ''
echo 'copy to'$jsPath'/enum/Enum_MsgType.js'
cp $outPath'/enum/Enum_MsgType.js'  $jsPath'/enum/'

echo ''
echo 'copy to'$jsPath'/util/reqMsg.js'
cp $outPath'/util/reqMsg.js'  $jsPath'/util/'

echo ''
echo "copy files, end...."



