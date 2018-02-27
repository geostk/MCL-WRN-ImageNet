from wideresnet import WideResNet

class MCLImageNet(nn.Module):
	def __init__(self, name, nmodel):
		super(MCLImageNet, self).__init__()
		nclasses = 1000
		widefactor = 2
		droprate = 0.3
		self.nmodel = nmodel

		if model == 'wrn':
			self.model = nn.ModuleList([WideResNet(18, nclasses, widefactor, droprate) for _ in range(nmodel)])

	def forward(self, x):
		outputs = [self.model[i](x) for i in range(self.nmodel)]