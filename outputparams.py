#!/usr/bin/env python

'''
Output the parameters that makemodel supports with their ranges
'''

import makemodel, argparse
import json
from collections import OrderedDict

#extract from arguments to makemodel
opts = makemodel.getoptions()
file="config.json"
f=open(file,"w")
d=OrderedDict()
for (name,vals) in sorted(opts.items()):
	param=name
	paramtype=type(vals).__name__
	paramsize=1
	if paramtype=="tuple":
		l=list(vals)
		paramtype=type(l[1]).__name__
		if paramtype=="str":
			options=vals
			paramtype="enum"
			data=OrderedDict([("name",param), ("type", paramtype), ("size", paramsize),("options",options)])
		else:
			paramtype="int"
			parammin=min(l)
			parammax=max(l)
			data=OrderedDict([("name",param), ("type", paramtype), ("min", parammin), ("max", parammax), ("size", paramsize)])
	else:
		paramtype="float"
		if param=="weight_decay_exp":
			parammin=-10
			parammax=0
		if param=="ranklossmult":
			parammin=0
			parammax=1
		if param=="momentum":
			parammin=0
			parammax=1
		if param=="loss_penalty":
			parammin=0
			parammax=5
		if param=="loss_gap":
			parammin=0
			parammax=5
		if param=="loss_delta":
			parammin=0
			parammax=8
		if param=="base_lr_exp":
			parammin=-10
			parammax=0
		data=OrderedDict([("name",param), ("type", paramtype), ("min", parammin), ("max", parammax), ("size", paramsize)])
	d[param]=data
f.write(json.dumps(d, indent=4))
f.close()
