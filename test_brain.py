from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection

n = FeedForwardNetwork()
in_layer = LinearLayer(2, name="input")
hidden_layer = SigmoidLayer(3, name="hidden")
out_layer = LinearLayer(1, name="output")

n.addInputModule(in_layer)
n.addModule(hidden_layer)
n.addOutputModule(out_layer)

in_to_hidden = FullConnection(in_layer, hidden_layer)
hidden_to_out = FullConnection(hidden_layer, out_layer)

n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)


n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

n.sortModules()

print n.activate([1,2])
