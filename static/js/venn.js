var sets = [ {sets: ['A'], size: 12},
             {sets: ['V'], size: 12},
             {sets: ['A','V'], size: 2}];

var chart = venn.VennDiagram();
d3.select("#venn").datum(sets).call(chart);
