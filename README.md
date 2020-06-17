# c-lightning Project Template

Getting started with a new project can be a daunting task, especially on a
complex project like a Lightning node. This template tries to get you going as
fast as possible, by providing a couple of utilities and a preconfigured
environment. The environment consists of a fully fledged python project
including tests, so you can start on your implementation without having to
learn all the obscure incantations first.

## Who is this template for?

Everybody! While primarily created to get a number of academic projects going,
it provides an easy to extend base that can be built upon:

 - Researchers trying to investigate the Lightning Network can create
   controlled network setups that highlight the aspects that they are looking
   into.
 - Plugin developers that want to extend c-lightning have a template of a
   plugin that can be incrementally changed to add new cool features.
 - Application developer that need a working test network they can use to test
   their applications against.

## Getting Started

Out of the box this template provides a number of pieces that should get you
started right away:

 - A sample plugin in `src/plugin.py` that shows you how easy it is to write a
   plugin to extend the existing functionality in c-lightning
 - Some tests that show how a network can be bootstrapped, and each node can
   be configured, with or without plugins.
 - A docker image that contains the required dependencies, so you can test and
   develop in isolation.
 - A `Makefile` that provides shortcuts to run tests and build artifacts.

