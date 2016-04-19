$(function() {
    $('#run-button').click(function() {
        $('#run-button').prop('disabled', true);
        $.ajax({
            url: 'run-simulation',
            type: 'POST',
            data: JSON.stringify({
                num_simulations: $('#num_simulations').val(),
                time_horizon: $('#time_horizon').val(),
                num_timesteps: $('#num_timesteps').val(),
                exp_simple_ret: $('#exp_simple_ret').val(),
                vol: $('#vol').val(),
                starting_price: $('#starting_price').val()
            }),
            dataType: 'json',
            success: function(response) {
                var layout = {
                    xaxis: {
                        title: 'Time (Years)'
                    },
                    yaxis: {
                        title: 'Price'
                    },
                    showlegend: false,
                    margin: {
                        l: 50,
                        r: 10,
                        t: 30
                    }
                };

                simulation = document.getElementById('plotly-simulation');

                //https://plot.ly/javascript/plotlyjs-function-reference/
                Plotly.newPlot(simulation, response, layout, {displaylogo: false});
                $('#run-button').prop('disabled', false);
            },
            error: function(error) {
                $('#run-button').prop('disabled', false);
                console.log(error);
            }
        });
    });
});