$(function(){


		var response = null

		// This is the required format from the server
		response = {'channels':[{
					name : 'colors TV',
					data : [100,300,400,500,200]
				},
				{
					name : 'Star plus',
					data : [10,800,460,560,185]
				}],
			    'programs':[{
					name : 'Comedy nights',
					data : [1000,3000,4030,5300,11200]
				},
				{
					name : 'Sasural something',
					data : [10,800,460,560,185]
				}]	
			}

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

		// $.get("/server",function(data){   <- uncomment this line
			/*
				This is the data format 
				data = {
					'channels':[{ // This is the list of channels
							name : 'channel name',
							data : [no of comments array of each day] <- this is an array
						   }]
							
					'programs' : [{  // This is the list of programs
							name : 'program name',
							data : [no of comments array of each day] <- this is an array
					}]
				}
			*/
			// console.log("data recvd")  <- Uncomment this line 
			// response = $.parseJSON(data);  <- Uncomment this line
		// }).done(function(){    <- Uncomment this line


			$("#graph-container-channels").highcharts({
				
				 title: {
	            			text: 'Channels'
	        		},
				xAxis:{
					categories:['14 nov','15 nov','16 nov','17 nov','18 nov','19 nov','20 nov']
				},
				yAxis:{
					title: {
						text: "Comments"
					}
				},
				// series:[{
				// 	name : 'colors TV',
				// 	data : [100,300,400,500,200]
				// },
				// {
				// 	name : 'Star plus',
				// 	data : [10,800,460,560,185]
				// }]	
				series : getChannelDetails()
			})


			$("#graph-container-programs").highcharts({

				title: {
	            			text: 'Individual Programs'
	        		},

				
				xAxis:{
					categories:['14 nov','15 nov','16 nov','17 nov','18 nov','19 nov','20 nov']
				},
				yAxis:{
					title: {
						text: "Comments"
					}
				},
				// series:[{
				// 	name : 'Comedy nights',
				// 	data : [1000,3000,4030,5300,11200]
				// },
				// {
				// 	name : 'Sasural something',
				// 	data : [10,800,460,560,185]
				// }]	
				series: getProgramDetails()
			})




			$("#graph-container-programs").hide()



			$("button").on('click',function(e){
				if($(this).attr('id') == 'p')
				{
					$("#graph-container-channels").fadeIn()
					$("#graph-container-programs").fadeOut()

				}
				else
				{
					$("#graph-container-channels").fadeOut()
					$("#graph-container-programs").fadeIn()
				}
			})

		// }) <- Uncomment this line too

		
})