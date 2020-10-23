Automatic Delivery Aid
======================

**Automatic Delivery Aid** (Ada for short) is a system that automates collective ordering of food using the Discord platform as a communication method.

## Description

Once launched, the program connects to the Discord and listens for text commands
(state `SLEEP`) and waits for the appropriate time to start the ordering. 
When the ordering process begins, the program collects the names of
restaurants to be voted on (`GATHER` status).
Then a list of choosen restaurants is drawn up and performed
voting process (`VOTE` state) followed by the winner being displayed.
Order placement begins (state `ORDER`), after which it is printed
a summary containing a list of orders placed and proposals of people who
should order. There is a waiting for someone to come forward to order
(`SUMMARY` state). After all, a summary is displayed and follows
possibility to make additional corrections (state `ADJUST`), after which
you can end the whole process and go back to waiting (`SLEEP` state).

## Documentation

The documentation is divided into individual files:

* [`docs/discord.md`] (docs/discord.md) -
  description of how to register the bot on the Discord platform
* [`docs/diagrams/states.dia`] (docs/diagrams/states.dia) -
  application state diagram with individual transitions
* [`docs/diagrams/database.dia`] (docs/diagrams/database.dia) -
  application database schema
* [`docs/commands.md`] (docs/commands.md) -
  a list of all commands that can be issued to the bot
* [`docs/examples.md`] (docs/examples.md) -
  sample conversations with the bot and descriptions of how the bot will behave
* [`docs/install.md`] (docs/install.md) -
  description of installation, configuration and starting work with the program
* [`docs/notes.md`] (docs/notes.md) -
  loose notes and notes describing the behavior of the program
* [`docs/database.md`] (docs/database.md) -
  database schema with its description
* [`docs/stages.md`] (docs/stages.md) -
  description of the states in which the program/delivery may be located
* [`docs/references.md`] (docs/references.md) -
  links and references to external sources

