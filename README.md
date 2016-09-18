# habitica-github [![License](https://img.shields.io/github/license/niteshpatel/habitica-github.svg?maxAge=3600)](https://raw.githubusercontent.com/niteshpatel/habitica-github/master/LICENSE.txt) [![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](http://stackshare.io/niteshpatel/habitica-github)

[Habitica extension](http://habitica.wikia.com/wiki/GitHub_Score_Task_Integration) to score a Habitica Task when GitHub commits are pushed.  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/niteshpatel/habitica-github)

## Installation

1. Use the Deploy to Heroku button (note down the app name)
1. Set up webhooks for all your GitHub repositories you want to track (found under Settings &gt; Webhooks)
1. Set the payload url to https://&lt;heroku app name&gt;.herokuapp.com/tasks/&lt;[taskId or taskAlias](http://habitica.wikia.com/wiki/Task_Alias)&gt;/score/up
1. Leave the default setting of push event only
1. Done.
