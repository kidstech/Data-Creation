#!/usr/bin/bash
cd word-data

for f in * ; do
    dest=../word-data-json/"$(echo $f | sed 's/.txt$/.json/')"
    ../label_words.js "$f" > "$dest"
done
