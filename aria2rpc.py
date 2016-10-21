import json, sys, os
from urllib import request
from argparse import ArgumentParser
from collections import defaultdict

parser = ArgumentParser()
parser.add_argument('-c', '--cookie', help='use cookies', type=str, default='', metavar='COOKIES', dest='cookies')
parser.add_argument('-o', '--output', help='output name', type=str, default='', metavar='NAME', dest='output')
parser.add_argument('-r', '--referer', help='referer', default='', type=str, metavar='URL', dest='referer')
parser.add_argument('-R', '--rpc', help='aria2 rpc', type=str, default='http://127.0.0.1:6800/jsonrpc', metavar='URL', dest='rpc')
parser.add_argument('URIs', nargs='+', help='URIs', type=str, default='', metavar='URI')
opts = parser.parse_args()
jsondict = {'jsonrpc':'2.0', 'id':'aria2rpc', 'method':'aria2.addUri'}
jsondict['params'] = []
jsondict['params'].append(opts.URIs)

aria2optsDefault={'continue':'true', 'max-connection-per-server':10, 'split':10, 'min-split-size':'1M'}
aria2opts = defaultdict(lambda:[])
aria2opts.update(aria2optsDefault)
if '.baidu' in opts.URIs[0]:
	aria2opts.update({'user-agent':'netdisk;5.3.4.5;PC;PC-Windows;5.1.2600;WindowsBaiduYunGuanJia'})
if opts.output:
	aria2opts['out'] = opts.output
if opts.referer:
	aria2opts['referer'] = opts.referer
if opts.cookies:
	aria2opts['header'].append('Cookie: {0}'.format(opts.cookies))

jsondict['params'].append(aria2opts)
jsonreq = json.dumps(jsondict).encode('utf-8')
request.urlopen(opts.rpc, jsonreq)
