#!/bin/sh

screen -dmS robot sh -c "$SPINALBOT_HOME/spinalbot.py $1 $2 $3 $4 2>$SPINALBOT_HOME/error.log"
