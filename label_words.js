#!/usr/bin/env node
// imports
//We can use wordpos or pos. I don't know which one is better, but wordpos offers fewer categories which seems simpler for starting off.
var wordpos = require('wordpos');
wordpos = new wordpos({stopwords: false});
var fs = require('fs');

var processFil = function(datafile){
    content = fs.readFileSync(datafile, 'utf-8');
    wordpos.getPOS(content).then(createJSON);
}

renamePOS = {
    verbs : "verb",
    nouns : "noun",
    adjectives: "adjective",
    adverbs : "adverb",
    rest : "other"
}

var processWord = function(word, pos){
    var json = {
        'name' : word,
        'wordType' : renamePOS[pos],
        'userCreated' : false
    }
    return json;
}

var flatten = function(arr){ return [].concat.apply([], arr) };

var createJSON = function(labeledWords){
    var json = Object.keys(labeledWords).map( function(partOfSpeech){
        return labeledWords[partOfSpeech].map( function (word){
            return processWord(word, partOfSpeech);
        });
    });

    json = flatten(json)
    console.log(JSON.stringify(json));
}

var main = function() {
    var args = process.argv.slice(2);
    args.forEach(processFil);
}

main()
