<script>
    // Sample data
    var data = [{
        x: {{x }},
        y: {{y }},
        mode: 'markers',
        type: 'scatter'
    }];

    // Layout settings
    var layout = {
        title: "Dataset {{name}}",
        xaxis: {
            title: 'X-axis'
        },
        yaxis: {
            title: 'Y-axis'
        }
    };

    // Create the plot
    Plotly.newPlot('scatter-plot', data, layout);
</script>
