#!/bin/bash
#small script to install openyoudao
install -g users -o root -m 755 -d debian/openyoudao/usr/bin
install -g users -o root -m 755 -d debian/openyoudao/usr/lib/openyoudao
install -g users -o root -m 777 -d debian/openyoudao/usr/share/openyoudao
install -g users -o root -m 755 -d debian/openyoudao/usr/share/applications
install -g users -o root -v -m 755 -t debian/openyoudao/usr/bin      scripts/openyoudao
install -g users -o root -v -m 644 -t debian/openyoudao/usr/lib/openyoudao ./*.py
install -g users -o root -v -m 644 -t debian/openyoudao/usr/share/applications  desktop/openyoudao.desktop
cp -rf cache/* debian/openyoudao/usr/share/openyoudao
chmod -R 777 debian/openyoudao/usr/share/openyoudao/*
