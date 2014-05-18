$(function(){


		var response = null
		var channel_names = []
		var series_data = []

		function init()
		{
			if(response)
			{

				$.each(response,function(index,element){
					var temp_object = {}
					channel_names.push(element['name'])
					temp_object['name'] = element['name']
					temp_object['data'] = element['data']['tweets_per_day']
					series_data.push(temp_object)
				})
			}
		}
		
		

		function getDataRatio()
		{
			var data = []
			if(response)
			{
				$.each(response,function(index,element){

					var temp = []
					temp.push(element['name'])

					var ratio = element['data']['tweets_per_day'].reduce(function(previousValue, currentValue, index, array){
  						return previousValue + currentValue;
					}) / element['data']['tweet_count']
					console.log(ratio)
					// var ratio = element['data']['tweet_count'] / element['data']['followers_count']
					temp.push( ratio)
					data.push(temp)
				})
				
			}
			return data
		}

		function getDataFollowers()
		{
			var data = []
			if(response)
			{
				$.each(response,function(index,element){

					var temp = []
					temp.push(element['name'])
					temp.push(element['data']['followers_count'])
					data.push(temp)
				})
				
			}
			return data
		}


		$.get("http://localhost:1234",function(data){   
		  	response = data

		}).done(function(){  

			// console.log(response[0].data.tweets_per_day)
			init()
			console.log(getDataFollowers())
			
			// console.log(getDataRatio())
			// console.log(series_data)
			// console.log(response[0]['dates'])
			$("#graph-container-retweets").highcharts({
				title: {
	            			text: 'Retweet count of each day of the user over the week'
	        		},

		        	subtitle: {
		        		text: "Source: twitter"
		        	},
				
				xAxis:{
					title: {
						text: "days	"
					},
					categories: response[0]['dates']
				},
				yAxis:{
					title: {
						text: "Retweets perday"
					}
				},
				series : series_data
			})
			
			// Pie charts
			Highcharts.getOptions().colors = Highcharts.map(Highcharts.getOptions().colors, function(color) {
			    	return {
			       		radialGradient: { cx: 0.5, cy: 0.3, r: 0.7 },
				        stops: [
				            [0, color],
				            [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
				        ]
			    	}
			})

			
			$("#graph-container-tweets-followers").highcharts({
				chart: {
             		 	 	plotBackgroundColor: null,
                			plotBorderWidth: null,
               	 			plotShadow: false
            			},

				title : {
					text : "Popularity of tweets"
				},
				subtitle: {
	       				text: "Source: Twitter"
	       			},
	       			plotOptions: {

			                pie: {
			                    allowPointSelect: true,
			                    cursor: 'pointer',
			                    dataLabels: {
			                        enabled: true,
			                        color: '#000000',
			                        connectorColor: '#000000',
			                        formatter: function() {
			                            return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';
			                        }
			                    }
			                }
			        },
	       			
	       			series : [{
	       				type:'pie',
	       				name : 'Number of retweets per tweet!',
	       				data : getDataRatio()
	       			}]

			})
			

			$("#graph-container-followers").highcharts({
				chart: {
             		 	 	plotBackgroundColor: null,
                			plotBorderWidth: null,
               	 			plotShadow: false
            			},

				title : {
					text : "Popularity of news channels"
				},
				subtitle: {
	       				text: "Source: Twitter"
	       			},
	       			plotOptions: {

			                pie: {
			                    allowPointSelect: true,
			                    cursor: 'pointer',
			                    dataLabels: {
			                        enabled: true,
			                        color: '#000000',
			                        connectorColor: '#000000',
			                        formatter: function() {
			                            return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';
			                        }
			                    }
			                }
			        },
	       			
	       			series : [{
	       				type:'pie',
	       				name : 'Number of followers',
	       				data : getDataFollowers()
	       			}]

			})

			

		 }) 

})