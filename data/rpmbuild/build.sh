#!/bin/bash -x

TARGET=$(grep Exclusive $1 | awk 'BEGIN {FS=":"} {gsub(" ", "", $2) ; print $2}')
if [ -z "$TARGET" ]; then
  TARGET=noarch
fi

#Check that target rpm does not already exist
if [ -e RPMS/$TARGET/$(basename $1 .spec).rpm ]; then
  echo toto
fi
package=$(basename $1 .spec)
resourcever=$(cat resources/${package}/VERSION)
  if [ -z "$resourcever" ]; then
    resourcever=0
  fi

  
  #rpmbuild -vv -bb --target $TARGET --clean --define "resourcever $resourcever" $1
  rpmbuild -vv -bb --target noarch --define "resourcever $resourcever" --define "_topdir /data/rpmbuild" --macros=/usr/lib/rpm/macros:/data/rpmbuild/macro/rpmmacros $1 

