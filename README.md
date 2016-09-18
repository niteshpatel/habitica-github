# habitica-github [![License](https://img.shields.io/github/license/niteshpatel/habitica-github.svg?maxAge=3600)](https://raw.githubusercontent.com/niteshpatel/habitica-github/master/LICENSE.txt) [![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](http://stackshare.io/niteshpatel/habitica-github)


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/niteshpatel/habitica-github)

## Installation

1. Use the Deploy to Heroku button
1. Set up a new webhook here https://github.com/[username]/[repository]/settings/hooks
1. Set the payload url to https://[heroku-app-name].herokuapp.com/tasks/[taskId/taskAlias]/score/[direction]
1. Leave the default setting of push event only
1. Done.

### Notes

* Set up the webhook on any additional repositories you want to track
* What is a taskId or taskAlias? http://habitica.wikia.com/wiki/Task_Alias
* direction should be up or down, presumably up in this case :)
