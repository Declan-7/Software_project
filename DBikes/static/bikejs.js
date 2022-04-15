
var map;
function prediction() {
                 var station= document.getElementById("param2").value;
                 var date = document.getElementById("param1").value;
                 var time = document.getElementById("param3").value;



                 
                 
                 $.getJSON("http://127.0.0.1:5000/prediction_/" + station+ "/"+ date + "/" + time, function (id) {
                 console.log("predict");
                 document.getElementById("prediction-bikes").innerHTML = document.getElementById("prediction-bikes").innerHTML = id+ " bikes available at Station " + station  +"  on  " +date+ " at " +time;;
    })
                 
             }
 document.getElementById("id01").innerHTML = "<table><tr><th>Station Selected: </th><td>  N/A </td><th> Available Bike Stands:                  </th><td> N/A </td><th>Available Bikes:     </th><td> N/A </td></tr></table>";






function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 53.349835, lng: -6.260310 },
    zoom: 12,
  });
}
fetch("/weather").then(response => {
    return response.json();
    }).then(weather => {
    weather.forEach(weather => {
        var f =weather.feels_like;
       // document.getElementById("weather").innerHTML=f;
         document.getElementById("weather").innerHTML = "<table><tr><th>Temperature:     </th><td>"  +weather.temp+ "&deg;C </td><th> Humidity:  </th><td>" + weather.humidity+ "%</td><th>Windspeed:  </th><td>"+weather.wind_speed +     "km/h</td><th>Weather Description</th><td>"+weather.weather_description+"</td></tr></table>";
    
})})






fetch("/stations").then(response => {
           return response.json();
    }).then(info => {
    var infowindow = new google.maps.InfoWindow();
    var subjectSel = document.getElementById("stationid");
    
    
    
    
    
    

    
    
    var stat =  "<option id= list1>---------------------Select Station------------------</option><br></select>";
stationslist = []
   info.forEach(station => {
                
            
                stationslist.push(station)
               // subjectSel.options = new Option(station.name)
                var clicked = false
                var current = false
                var c = station.available_bikes
                var d = station.available_bikes+station.available_bike_stands
                var q = (station.position_lat)
                var f = (station.position_lng)
                if (c > d/2) {
                    var x = "http://maps.google.com/mapfiles/ms/icons/green-dot.png"
                }
                else {
                    var x = "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                }
                const marker = new google.maps.Marker({
                icon: {
                    url: x
                  },                                     
                position: { lat: parseFloat(q), lng: parseFloat(f)},
                map: map,

                })
                //const list = d
               // var s = station.last_update;
                
       
       
       
    
             
                stat += "<option value=" + station.number + ">" + station.name +"   (No."+station.number+")" + "</option><br></select>";
           document.getElementById("Station").innerHTML = stat;
           
            var space ="<br><br><br><br><br>" 
            document.getElementById("id03").innerHTML=space;
            var form = document.getElementById("Station");

            document.getElementById("submit").addEventListener("click", function () {
            var t = "";
          //  t = "<p>'"+(station.name).selectedIndex+"'</p>" ;
            //document.getElementById("Station").selectedIndex=t;
            var x =document.getElementById("Station").selectedIndex;
            var u = document.getElementById("Station").options;
            if (x>=1) {
            document.getElementById("id01").innerHTML = "<table><tr><th>Station Selected:     </th><td>"+info[x-1].name+"  No ( "+info[x-1].number+" ) </td><th> Available Bike Stands:                  </th><td>"+info[x-1].available_bike_stands+"</td><th>Available Bikes:     </th><td>"+info[x-1].available_bikes+"</td></tr></table>";
            }
            else {
                document.getElementById("id01").innerHTML="<table><tr><th>Station Selected:     </th><td> N/A </td><th> Available Bike Stands:                  </th><td>N/A</td><th>Available Bikes:     </th><td>N/A</td></tr></table>";
            }
            
                
            var space2 ="<br><br><br><br><br>" 
            document.getElementById("id04").innerHTML=space2;
            //p = "<table><th>Highest Rate Per 100,000: </th><th>Lowest Rate Per 100,000:  </th> "
        //p+= "<tr><td>"+county_max+"</td><td>"+county_min+"</td></tr>"
        //document.getElementById("id011").innerHTML = p
                

            })
               var date = (station.last_update)
            
              // var b = date.getHours()
               marker.addListener("click", () => {
                if (clicked==false) {
                var content= "<h3>" + station.name + " (No. " +station.number +")</h3>"
                + "<p><b>Available Bikes: </b>" + station.available_bikes + "</p>"
                + "<p><b>Available Stands: </b>" + station.available_bike_stands + "</p>"
                + "<p><b>Parking Slots: </b>" + station.available_bike_stands + "</p>"
                + "<p><b>Status: </b>" + station.status + "</p>" +"<p><b>Last Updated: </b>" + station.last_update + "</p>";
                infowindow.setContent(content);
                infowindow.open(map, marker);
                clicked = true;
                
                }
                   
                



                
            
                
          
            else if (clicked==true) {
                    infowindow.close();
                    clicked=false;
                }
                   
            
                                  

   
   
   
   
   
    
   })})



   }).catch(function () {
            console.log("error");
        })

   
     //       document.getElementById("stationid").selectedIndex
    

        

        
//
        
        
            
        
            //    hourlyChart(station.number);
            
        
    
        
        
    
    <!-- jsFiddle will insert css and js -->
     