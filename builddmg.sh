#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/PDFMerger.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/PDFMerger.dmg" && rm "dist/PDFMerger.dmg"
create-dmg \
  --volname "PDFMerger" \
  --volicon "assets/icon.icns"
  --window-pos 200 120 \
  --window-size 600 300 \
  --hide-extension "PDFMerger.app" \
  --app-drop-link 425 120 \
  "dist/PDFMerger.dmg" \
  "dist/dmg/"