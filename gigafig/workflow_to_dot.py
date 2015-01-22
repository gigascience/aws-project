#!/usr/bin/python

"""
Usage:

"""

try:
    import simplejson as json
except ImportError:
    import json
import argparse
import sys
from textwrap import wrap, fill

parser = argparse.ArgumentParser(description="Convert Galaxy workflow JSON to graphviz dot")
parser.add_argument("workflow_file", type=file, help="Galaxy workflow description (JSON format)")
parser.add_argument('--label_unnamed_data', action='store_true', default=False,
                    help="Label datasets even if they have no explicit name (rename dataset action)")
parser.add_argument('--nodes_are_analyses', action='store_true', default=False,
                    help="Graph nodes are analyses (by default they are datasets)")
parser.add_argument('--no_graph_name', action='store_true', default=False, help="Omit the name of the graph")
parser.add_argument('--output_filename', help="Output filename (default is to print to stdout)")
args = parser.parse_args()

if args.label_unnamed_data and not args.nodes_are_analyses:
    sys.stderr.write('Warning: --label_unnamed_data does nothing if graph nodes are datasets\n')

if args.output_filename:
    output = open(args.output_filename, 'w')
else:
    output = sys.stdout

nodes = dict()
edges = dict()
free_edges = set()
edge_aliases = dict()
out_edges = []
datasets = dict()
max_width = 15


def print_edge(start, end, edge_name, label_unnamed_edges):
    start = '\\n'.join(wrap(start, max_width))
    end = '\\n'.join(wrap(end, max_width))
    edge_label = '\\n'.join(wrap(edge_aliases.get(edge_name, edge_name), max_width))
    edge_string = '\t"{0}" -> "{1}"'.format(start, end)
    if label_unnamed_edges or edge_name in edge_aliases:
        edge_string = ''.join((edge_string, '[label="{0}", fontcolor="#0000ff"]'.format(edge_label)))
    edge_string += '\n'
    output.write(edge_string)


workflow = json.load(args.workflow_file)
if workflow["format-version"] != "0.1":
    sys.stderr.write("Unknown format version {0}, continuing anyway\n".format(workflow['format-version']))

name = workflow['name']
graph_str = 'digraph '
if not args.no_graph_name:
    graph_str += '"{0}" '.format(name)
graph_str += '{\n'
output.write(graph_str)
steps = workflow['steps']
input_count = 0
num_steps = len(steps)
for step in sorted(steps, key=int):
    if steps[step]['name'] == 'Input dataset':
        input_count += 1
        name = "input{0}".format(input_count)
        if "name" in steps[step]["tool_state"]:
            name = json.loads(steps[step]["tool_state"])["name"]
        edge_name = "{0}:output".format(step)
        edge_aliases[edge_name] = name
        free_edges.add(edge_name)
        nodes[step] = 'Start'
    else:
        name = steps[step]['name']
        nodes[step] = name
        inputs = set()
        for input_name in steps[step]['input_connections']:
            start_step_num = unicode(steps[step]['input_connections'][input_name]['id'])
            edge_data = steps[step]['input_connections'][input_name]['output_name']
            edge_name = '{0}:{1}'.format(start_step_num, edge_data)
            if edge_name in free_edges:
                free_edges.remove(edge_name)
            if nodes[start_step_num] == 'Start':
                start_node_name = 'Start'
            else:
                start_node_name = "{0}:{1}".format(start_step_num, nodes[start_step_num])
            end_node_name = "{0}:{1}".format(step, name)
            edges[edge_name] = [start_step_num, step]
            if args.nodes_are_analyses:
                print_edge(start_node_name, end_node_name, edge_name, args.label_unnamed_data)
            inputs.add(edge_name)
        for action in steps[step]['post_job_actions']:
            if action.startswith('RenameDatasetAction'):
                edge_name = "{0}:{1}".format(step, steps[step]['post_job_actions'][action]['output_name'])
                edge_aliases[edge_name] = steps[step]['post_job_actions'][action]['action_arguments']['newname']
        for output_dataset in steps[step]['outputs']:
            edge_name = '{0}:{1}'.format(step, output_dataset['name'])
            datasets[edge_name] = dict(source=name, inputs=inputs)
            free_edges.add(edge_name)

for edge_name in free_edges:
    step = unicode(edge_name.split(':')[0])
    start_node_name = "{0}:{1}".format(step, nodes[step])
    if args.nodes_are_analyses:
        print_edge(start_node_name, 'End', edge_name, args.label_unnamed_data)


def print_analysis_edge(start, end, label):
    start = '\\n'.join(wrap(start, max_width))
    end = '\\n'.join(wrap(end, max_width))
    label = '\\n'.join(wrap(label, max_width))
    edge_string = '\t"{0}" -> "{1}" [ fontcolor="blue", label="{2}" ];\n'.format(start, end, label)
    output.write(edge_string)


for dataset_name in datasets:
    output_name = edge_aliases.get(dataset_name, dataset_name)
    for input_dataset in datasets[dataset_name]['inputs']:
        # edge is analysis.
        input_name = edge_aliases.get(input_dataset, input_dataset)
        if not args.nodes_are_analyses:
            print_analysis_edge(input_name, output_name, datasets[dataset_name]['source'])

output.write('}\n')