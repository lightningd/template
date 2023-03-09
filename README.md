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

You can get started with this template by checking it out, and start hacking:

```bash
$ git clone https://github.com/lightningd/template.git my-awesome-project
$ cd my-awesome-project
```

Alternatively you can also download a snapshot and start with that:

```bash
$ wget https://github.com/lightningd/template/archive/master.zip -O my-awesome-project.zip
$ unzip my-awesome-project.zip
$ cd my-awesome-project
```

The template comes with some canned tests to illustrate how you can create a
network, perform some actions on it, test some things, and then tear down the
network again after the test ran. These tests can be run either directly, or
with the provided docker image, if you don't want to install the
dependencies. The following builds the docker image:

```bash
make docker-image
```

And the following runs the tests in a docker container:

```bash
make docker-test
```

## Where to go next?

Once you have familiarized yourself with how your tests can be run it's time
to dig deeper. The following resources should help you on your journey:

 - The c-lightning [Plugin API docs][plugin-docs] describe the communication
   between c-lightning and your plugin.
 - The [pyln-client docs][pyln-client-docs] describe the JSON-RPC API client
   (`LightningRpc`) and the `Plugin` API used to talk to c-lightning over the
   JSON-RPC or to implement a plugin. 🚧 These docs are still under
   construction 🚧
 
 
[plugin-docs]: https://lightning.readthedocs.io/PLUGINS.html
[pyln-client-docs]: https://pyln-client.readthedocs.io/en/pyln/api.html
