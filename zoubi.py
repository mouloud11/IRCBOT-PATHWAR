#!/usr/bin/env python2
# -*- coding: utf8 -*-

import irclib
import ircbot
 
class Bot(ircbot.SingleServerIRCBot):
    def __init__(self):
        ircbot.SingleServerIRCBot.__init__(self, [("irc.pathwar.net", 6667)],
                                           "Zboubi", "Suck me.")
    def on_welcome(self, serv, ev):
        serv.join("#pathwar-fr")
    def on_pubmsg(self, serv, ev):
        message = ev.arguments()[0]
        if "coupon: " in message or "coupon: " in message:
            var = message[0:40]
            serv.privmsg("#pathwar-fr", "Tu arrive trop tard pour valider "+var + "  PD VA!")
    def on_kick(self, serv, ev):
        serv.join("#pathwar-fr")
if __name__ == "__main__":
    Bot().start()
