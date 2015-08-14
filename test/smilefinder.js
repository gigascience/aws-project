$(document).ready(function () {

    var cy = cytoscape({
        container: document.getElementById('cy'),

        style: cytoscape.stylesheet()
            .selector('node')
            .css({
                'content': 'data(name)',
                'shape': 'circle',
                'background-color': 'data(color)',
                'font-size': 10,
                'text-valign' : 'bottom',
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

        elements: {
            nodes: [
                {data: {id: 'a',
                        name: 'Select populations',
                        color:'#D9EDF7'}
                },
                {data: {id: 'b',
                        name: 'Count',
                        color:'#D9EDF7'}
                },
                {data: {id: 'c',
                        name: 'Filter',
                        color:'#D9EDF7'}
                },
                {data: {id: 'd',
                        name: 'Select first',
                        color:'#D9EDF7'}
                },
                {data: {id: 'e',
                        name: 'Remove beginning',
                        color:'#D9EDF7'}
                },
                {data: {id: 'f',
                        name: 'Sort',
                        color:'#D9EDF7'}
                },
                {data: {id: 'g',
                        name: 'Concatenate datasets',
                        color:'#D9EDF7'}
                },
                {data: {id: 'h',
                        name: 'SmileFinder',
                        color:'#D9EDF7'}
                },
                {data: {id: 'i',
                        name: 'Grapher',
                        color:'#D9EDF7'}
                },
                {data: {id: 'j',
                        name: 'graph',
                        color:'#FCF8E3'}
                }

            ],

            edges: [
                {data: {id: 'ab', weight: 1, source: 'a', target: 'b'}}, //Select populations > Count
                {data: {id: 'bc', weight: 2, source: 'b', target: 'c'}}, //Count > Filter
                {data: {id: 'cd', weight: 3, source: 'c', target: 'd'}}, //Filter > Select first
                {data: {id: 'ce', weight: 4, source: 'c', target: 'e'}}, //Filter > Remove beginning
                {data: {id: 'ef', weight: 5, source: 'e', target: 'f'}}, //Remove beginning > Sort
                {data: {id: 'dg', weight: 6, source: 'd', target: 'g'}}, //Select First > Concatenate datasets
                {data: {id: 'fg', weight: 6, source: 'f', target: 'g'}}, //Sort > Concatenate datasets
                {data: {id: 'gh', weight: 7, source: 'g', target: 'h'}}, //Concatenate datasets > SmileFinder
                {data: {id: 'hi', weight: 8, source: 'h', target: 'i'}}, //SmileFinder > Grapher
                {data: {id: 'ij', weight: 8, source: 'i', target: 'j'}}  //Grapher > graph
            ]
        },

        layout: {
            name: 'dagre',
            //name: 'breadthfirst',
            directed: true,
            roots: '#a',
            padding: 10
            //rankDir: 'LR'
        }
    });

}); // on dom ready