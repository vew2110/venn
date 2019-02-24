var sets = [ {sets: ['A'], size: 12},
             {sets: ['B'], size: 12},
             {sets: ['A','B'], size: 2}];

var chart = venn.VennDiagram()
d3.select("#venn").datum(sets).call(chart);
