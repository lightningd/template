#!/usr/bin/env python3
"""This is a small demo plugin
"""
from pyln.client import Plugin
import time


plugin = Plugin()


# Functions decorated with `@plugin.method()` or `@plugin.async_method()` are
# registered with the JSON-RPC exposed by `lightningd` and relayed to the
# plugin that registered them. The `hello` function below for example can be
# called like this:
#
# ```bash
# $ lightning-cli hello "my friend!"
# Hello my friend!
# ```
#
# As you can see this RPC passthrough also allows using default values and the
# returned object is converted into a JSON object and returned by the call
# from the client.
@plugin.method("hello")
def hello(plugin, name="world"):
    """This is the documentation string for the hello-function.

    It gets reported as the description when registering the function
    as a method with `lightningd`.

    It will also be returned if you call `lightning-cli help hello`.

    """
    greeting = plugin.get_option('greeting')
    s = '{} {}'.format(greeting, name)
    plugin.log(s)
    return s


# The special function decorated with `@plugin.init()` is called by
# `lightningd` once it has finished initializing, the options have been parsed
# and the RPC is now available. To make interacting with the JSON-RPC easier
# `plugin` has an automatically configured RPC-client under `plugin.rpc`, so
# you could for example retrieve information about the node using the
# following
#
# ```python3
# info = plugin.rpc.getinfo()
# print(info['id'])
# ```
@plugin.init()
def init(options, configuration, plugin, **kwargs):
    plugin.log("Plugin helloworld.py initialized")


# TODO Document
@plugin.subscribe("connect")
def on_connect(plugin, id, address, **kwargs):
    plugin.log("Received connect event for peer {}".format(id))


@plugin.subscribe("disconnect")
def on_disconnect(plugin, id, **kwargs):
    plugin.log("Received disconnect event for peer {}".format(id))

# TODO Document
@plugin.hook("htlc_accepted")
def on_htlc_accepted(onion, htlc, plugin, **kwargs):
    plugin.log('on_htlc_accepted called')
    time.sleep(20)
    return {'result': 'continue'}


# Options registered before the call to `plugin.run()` will be exposed by
# `lightningd` as if they were its own options. The option defined below
# allows you to start `lightningd` like this:
#
# ```bash
# $ lightningd --plugin=/path/to/plugin.py --greeting=Ciao
# ```
#
# And the option will be passed to the plugin, where it can be accessed using
# `plugin.get_option()` like in the `hello()` function above.
plugin.add_option('greeting', 'Hello', 'The greeting I should use.')


# After setting everything up it's time to give the plugin control of the
# script by calling `plugin.run()`. It takes control of stdin/stdout and
# starts communicating with `lightningd`.
plugin.run()
