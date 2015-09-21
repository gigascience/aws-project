$(document).ready(function () {
    // Parse galaxy url from attribute in cy element
    var galaxy_wf_id = $("#cy").attr("data-galaxy_wf_id");
    var galaxy_history_id = $("#cy").attr("data-galaxy_history_id");

    // Load data using HTTP GET request
    var wf = $.ajax({
        url: '/gigafig/galaxy2cytoscape/',
        type: 'GET',
        error: function (xhr, tStatus, err) {
            $('#cy').html(
                '<p>Problem retrieving galaxy workflow json</p>' +
                '<p>HTTP status: ' + xhr.status + '</p>' +
                '<p>' + tStatus + '</p>' +
                '<p>' + err + '</p>');
        },
        dataType: 'json',
        data: {
            //galaxy_wf_id: galaxy_wf_id
            galaxy_history_id: galaxy_history_id
        }
    });

    function inputDataPanelHtml(node_title, content) {
        return '<div class="panel panel-default panel-info">\
                            <div class="panel-heading">\
                            <h3 class="panel-title">' + node_title + '</h3></div>\
                            <div class="panel-body">' + content + '</div>\
                            </div>';
    }

    function outputDataPanelHtml(node_title, content) {
        return '<div class="panel panel-default panel-warning">\
                            <div class="panel-heading">\
                            <h3 class="panel-title">' + node_title + '</h3></div>\
                            <div class="panel-body">' + content + '</div>\
                            </div>';
    }

    function toolPanelHtml(node_title, content) {
        return '<div class="panel panel-default panel-success">\
                            <div class="panel-heading">\
                            <h3 class="panel-title">' + node_title + '</h3></div>\
                            <div class="panel-body">' + content + '</div>\
                            </div>';
    }

    // For creating panels to display node information
    function getNodePanel(nodes, id) {
        console.log("In getNodelPanel");
        for (var i = 0; i < nodes.length; i++) {
            if (nodes[i].data.id == id) {
                if (nodes[i].data.name == "data_input") {
                    return inputDataPanelHtml("Data input", nodes[i].data.dataset_id);
                }
                else if (nodes[i].data.name == "data_output") {
                    return outputDataPanelHtml("Data output", nodes[i].data.dataset_id);
                }
                else {
                    return toolPanelHtml(nodes[i].data.name, "Information about tool");
                }
            }
        }
    }

    // When workflow is loaded, init cy
    Promise.all([wf]).then(initCy);

    function initCy(then) {
        var loading = document.getElementById('loading');
        loading.classList.add('loaded');

        var expJson = then[0];
        var elements = expJson.elements;
        console.log(elements);

        // Copy tool params into tab panels
        var nodes = elements.nodes;
        var htmlString = "";
        var count = 1;
        for (var i = 0; i < nodes.length; i++) {
            if (nodes[i].data.type == "tool") {
                //Parse tool state information
                var state = nodes[i].data.tool_state;
                var params = '<table class="table">';
                for (var prop in state) {
                    // Check if parameter is a nested array
                    if (prop !== "__page__" && prop !== "chromInfo" && prop !== "__rerun_remap_job_id__") {
                        var param = JSON.parse(state[prop]);
                        if (param instanceof Object) {
                            var subtable = '<table class="table">';

                            for (var item in param) {
                                subtable += "<tr><td>" + item + "</td>";
                                subtable += "<td>" + param[item] + "</td></tr>";
                            }
                            subtable += "</table>";

                            params += '<tr data-toggle="collapse" data-target="#demo' + count + '" class="accordion-toggle"><td>' + prop + '</td><td><button class="btn btn-default btn-xs"><span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span></button></td></tr>';
                            params += '<tr><td class="hiddenRow"><div class="accordion-body collapse" id="demo' + count + '">' + subtable + '</div></td></tr>';
                            count = count + 1
                            //alert(params);
                        }
                        else {
                            params += "<tr><td>" + prop + "</td>";
                            params += "<td>" + state[prop] + "</td></tr>";
                        }
                    }
                }
                params += '</table>';
                htmlString += toolPanelHtml(nodes[i].data.name + "-" + nodes[i].data.tool_version, params);
            }
            else {
                htmlString += inputDataPanelHtml(nodes[i].data.name, 'stuff');
            }
        }
        $("#pane2").html(htmlString);

        // The graph
        var cy = window.cy = cytoscape({
            container: document.getElementById('cy'),
            layout: {
                name: 'dagre',
                directed: true,
                roots: '#a',
                padding: 10
                //rankDir: 'LR'
            },
            style: cytoscape.stylesheet()
                .selector('node')
                .css({
                    'content': 'data(name)',
                    'shape': 'circle',
                    'background-color': 'data(color)',
                    'font-size': 10,
                    'text-valign': 'bottom',
                    'color': '#6e6e6e'
                }
            )
                .selector('edge')
                .css({
                    'target-arrow-shape': 'triangle',
                    'width': 2,
                    'line-color': '#bfbfbf',
                    'target-arrow-color': '#bfbfbf'
                })
                .selector('.highlighted')
                .css({
                    'background-color': '#61bffc',
                    'line-color': '#61bffc',
                    'target-arrow-color': '#61bffc',
                    'transition-property': 'background-color, line-color, target-arrow-color',
                    'transition-duration': '0.5s'
                }),
            elements: elements,
            motionBlur: true,
            selectionType: 'single',
            boxSelectionEnabled: false,

            // Create events on clicking
            ready: function () {
                window.cy = this;
                cy.on("click", "node", function (evt) {
                    var node = this;
                    //console.log("%o", node);
                    console.log('Clicked node: ' + evt.cyTarget.id());
                    $("#pane2").html(getNodePanel(nodes, evt.cyTarget.id()));
                });

                cy.on("click", "edge", function (evt) {
                    var edge = this;
                    console.log("%o", edge);
                    console.log('Clicked edge: ' + evt.cyTarget.id());
                    $("#pane4").html("<p>Clicked edge: " + evt.cyTarget.id() + "</p>");
                });

                //cy.elements().bind("click", function(){
                //    this.css({
                //        content: "clicked"
                //    });
                //});

            }
        });
    }
}); // on dom ready