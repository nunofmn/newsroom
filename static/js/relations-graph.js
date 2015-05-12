var entities;
var oldnodes = [];

$('#search-query').keyup(function(e) {
    if(e.keyCode == 13) {
        var query = $(this).val();

        if(oldnodes.length !== 0) {
            oldnodes.forEach(function(elem) {
                elem.attr("r", 10);
            });
        }

        oldnodes = [];

        if(query === "") {
            return;
        }

        entities.nodes.forEach(function(elem, index, data) {
            var name = elem.name.toLowerCase();

            if(name.includes(query.toLowerCase())) {
                var node = d3.selectAll(".node").filter(function(d, i) {
                    return i == index ? this : null;
                });
                node.attr("r", 20);

                oldnodes.push(node);
            }
        });


    }
});

var width = $("#graph").width();
var height = 600;

var color = d3.scale.category20();

var force = d3.layout.force()
.charge(-80)
.linkDistance(70)
.size([width, height]);

var svg = d3.select("#graph").append("svg")
.attr("width", width)
.attr("height", height);

d3.json("http://localhost:5000/entities/data", function(error, graph) {
    entities = graph;
    force
    .nodes(graph.nodes)
    .links(graph.links)
    .start();

    var link = svg.selectAll(".link")
    .data(graph.links)
    .enter().append("line")
    .attr("class", "link")
    .style("stroke-width", function(d) { return Math.sqrt(d.value); });

    var node = svg.selectAll(".node")
    .data(graph.nodes)
    .enter().append("circle")
    .attr("class", "node")
    .attr("r", 10)
    .style("fill", function(d) { return d3.rgb("#"+((1<<24)*Math.random()|0).toString(16)); })
    .call(force.drag);

    node.append("title")
    .text(function(d) { return d.name; });

    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

        node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .on("dblclick", function(d) { updateNodeInfo(d); });
    });
});

var updateNodeInfo = function(node) {
    $(".node-name").html(node.name);
    var nodelisting = "";

    entities.links.forEach(function(elem, index, data) {
        if(node.index == elem.source.index) {
            nodelisting = nodelisting + "<li>" + entities.nodes[elem.target.index].name +
                "<ul><li>Weight: " + elem.target.weight + "</li></ul></li>\n";
        }else if(node.index == elem.target.index) {
            nodelisting = nodelisting + "<li>" + entities.nodes[elem.source.index].name +
                "<ul><li>Weight: " + elem.target.weight + "</li></ul></li>\n";
        }
    });

    $(".node-relations").html(nodelisting);
    $(".node-info").show();
};
