$(function(){


		var response = null

	
		function getChannelDetails()
		{
			if(response)
			{
				return response['channels']
			}
		}


		function getProgramDetails()
		{
			if(response)
			{
				return response['programs']
			}
		}

		$.get("http://localhost:1234/query=comments-lastweek",function(data){   
		  
			console.log(data)
			response = data  

		}).done(function(){  

			$("#graph-container-programs").highcharts({

				title: {
	            			text: 'Last Week Comments'
	        		},

		        	subtitle: {
		        		text: "Source: Facebook"
		        	},
				
				// xAxis:{
				// 	title: {
				// 		text: "days	"
				// 	},
				// 	categories: (function(){
				// 		var date = new Date();
				// 		today = date.getDate();
				// 		console.log(today)
				// 		res = new Array();
				// 		for(i = 6; i >= 0; --i){
				// 			res.push(today - i);
				// 		}
				// 		return res
				// 	})()
				// },
				yAxis:{
					title: {
						text: "Comments"
					}
				},
				
				series: response
			})


		 }) 

		///////////////////////////////////////////////////////////
		$.get("http://localhost:1234/query=comments-percentage",function(data){   
		  
			console.log(data)
			response = data  

		}).done(function(){  


			$("#graph-container-comments").highcharts({
				chart:{
					plotShadow: true
				},

				title: {
	            			text: 'Comments in Percentage'
	        	},

	        	subtitle: {
	        		text: "Source: Facebook"
	        	},
				
				tooltip:{
					pointFormat: '{series.name}: <b>{point.percentage: .1f}%</b>'
				},

				plotOptions:{
					pie:{
						allowPointSelect: true,
						cursor: 'pointer',
						dataLabels:{
							enabled: true,
							color:'#000000',
							connectorColor: '#000000',
							format: '<b>{point.name}</b>: {point.percentage: .1f}%'

						}
					}
				},

				series: [{
					type: 'pie',
					name: 'Comments',
					data: response
				}]
			})


		 })
		
})