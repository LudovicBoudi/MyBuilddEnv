#!/bin/bash

usage() {
  echo $0 package_dir
}


if [ $# -ne 1 ];then
  usage
  exit -1
fi

#Stripping path separator
package=${1%%/} 

if [ ! -e $package/VERSION ];then
  echo "$package/VERSION couldn't be found. Aborting!"
  exit -1
fi

version=$(cat $package/VERSION)
theversion=$(echo $version | awk 'BEGIN {FS="-"} {print $1}')
therelease=$(echo $version | awk 'BEGIN {FS="-"} {print $2}')
if [ -z "$therelease" ]; then
  therelease=0
fi

echo "Generating ../SOURCES/${package}_resource-$theversion.tgz"
tar czfC ../SOURCES/${package}_resource-$theversion.tgz $package --exclude archive --exclude "*.contrib*" --exclude "*.keep*" --exclude VERSION .
