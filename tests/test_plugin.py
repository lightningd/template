from pyln.testing.fixtures import *
import logging
import os
import sys


logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
test_path = os.path.dirname(__file__)
plugin_path = os.path.join(test_path, '..', 'src', 'plugin.py')


def test_plugin_start(node_factory):
    """Simply try to start a node with the plugin.
    """
    l1 = node_factory.get_node(options={'plugin': plugin_path})
    print(l1.rpc.getinfo())


def test_plugin_rpc_call(node_factory):
    """Test the `hello` RPC method exposed by the plugin.
    """
    l1 = node_factory.get_node(options={'plugin': plugin_path})

    # Test with the default parameter "world"
    r = l1.rpc.hello()
    assert(r == 'Hello world')

    # Test by overriding the default parameter
    r = l1.rpc.hello('my friend!')
    assert(r == 'Hello my friend!')


def test_plugin_option(node_factory):
    """The plugin adds a command-line options, let's test it.
    """
    # Notice that we skip the two dashes at the beginning:
    opts = {
        'plugin': plugin_path,
        'greeting': 'Ciao',
    }
    l1 = node_factory.get_node(options=opts)
    r = l1.rpc.hello()
    assert(r == 'Ciao world')


def test_payment(node_factory):
    """Let's just perform a test payment, without plugins this time.

    `node_factory` has a `line_graph` helper function that creates the very
    common line network for testing: it creates `n` nodes, and connects each
    one with the next one with a channel.

    """
    l1, l2 = node_factory.line_graph(2)

    # Create an invoice from node `l2` for `l1` to pay. Notice that label
    # needs to be unique since that's how you later look it up again. We only
    # care about the `bolt11`-encoded invoice.
    inv = l2.rpc.invoice(1337, "label", "description")['bolt11']

    # Now just let `l1` pay the invoice:
    l1.rpc.pay(inv)

    # Now check with `l2` that it marked the invoice as paid:
    invoices = l2.rpc.listinvoices("label")['invoices']

    # Since we provided a label we should only get one:
    assert(len(invoices) == 1)
    invoice = invoices[0]

    # Since l1 paid it, we should see it as paid:
    assert(invoice['status'] == 'paid')
