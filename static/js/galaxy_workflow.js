function GalaxyWorkflow(name) {
    this.name = name;
}

GalaxyWorkflow.prototype.parse = function (wf_text) {
    var wf_obj = JSON.parse(wf_text);
    var steps = wf_obj["steps"];

    var elements_contents = {};
    var elements = {};

    // Create nodes
    var data_nodes = [];
    var data_edges = [];
    for (var count in steps) {
        var edge_data_contents = {};

        var node_data_contents = {};
        node_data_contents["id"] = "n" + steps[count].id;
        node_data_contents["name"] = steps[count].name;
        if (steps[count].type == "data_input") {
            node_data_contents["color"] = "#FCF8E3";
        }
        else { // The node is a tool
            node_data_contents["color"] = "#D9EDF7";
            // Create edge
            var input_connections = steps[count].input_connections;
            for (var input_connection_key in input_connections) {
                var input_connection = input_connections[input_connection_key];
                var edge_id = "n" + input_connection["id"] + "n" + count;
                edge_data_contents["id"] = edge_id;
                edge_data_contents["weight"] = "1";
                edge_data_contents["source"] = "n" + input_connection["id"];
                edge_data_contents["target"] = "n" + count;
            }
            data_edges.push({"data": edge_data_contents});
        }
        data_nodes.push({"data": node_data_contents});
    }

    elements_contents["nodes"] = data_nodes;
    elements_contents["edges"] = data_edges;
    elements["elements"] = elements_contents;
    //console.log(JSON.stringify(elements, null, 2));
    return JSON.stringify(elements, null, 2);
};

GalaxyWorkflow.prototype.write_cytoscape = function () {
    var data = {};
    return JSON.stringify(data);
};

