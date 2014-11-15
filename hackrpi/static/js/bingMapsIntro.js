var map = null;

function GetMap() {
    // Initialize the map
    // Register and load a new module
    Microsoft.Maps.loadModule('Microsoft.Maps.Themes.BingTheme', { callback: themesModuleLoaded });
}

function themesModuleLoaded() {
    var mapOptions =
    {
        credentials: "AmfRb1VkPWQZsViCeyFIxTEzaMnv5Qixhlar-qeOkgLGm0byEGP5v0nsXm9T5oQC",
        mapTypeId: Microsoft.Maps.MapTypeId.auto, //birdseye
        zoom: 2,
        showScalebar: false,
        showMapTypeSelector: false,
        showDashboard: false,
        enableSearchLogo: false,
        theme: new Microsoft.Maps.Themes.BingTheme() 
    };

    // Load the map using the Bing theme style. 
    map = new Microsoft.Maps.Map(document.getElementById("mapDiv"), mapOptions);

    ClickGeocode();
}

function ClickGeocode(credentials)
{
    map.getCredentials(MakeGeocodeRequest);
}

function MakeGeocodeRequest(credentials)
{
    var locn = ['Redmond, WA', 'Mountain View, CA', 'Mountain View, CA', 'Walldorf, Germany', 'San Jose, CA'];
    for (city in locn) {    
      var geocodeRequest = "http://dev.virtualearth.net/REST/v1/Locations?query=" + encodeURI(locn[city]) + "&output=json&jsonp=GeocodeCallback&key=" + credentials;
      CallRestService(geocodeRequest);
    }
}

function GeocodeCallback(result) 
{
   //alert("Found location: " + result.resourceSets[0].resources[0].name);
   if (result &&
          result.resourceSets &&
          result.resourceSets.length > 0 &&
          result.resourceSets[0].resources &&
          result.resourceSets[0].resources.length > 0) 
   {
      // Set the map view using the returned bounding box
      var bbox = result.resourceSets[0].resources[0].bbox;
      var viewBoundaries = Microsoft.Maps.LocationRect.fromLocations(new Microsoft.Maps.Location(bbox[0], bbox[1]), new Microsoft.Maps.Location(bbox[2], bbox[3]));
      map.setView({ bounds: viewBoundaries});
       
      //
      var location = new Microsoft.Maps.Location(result.resourceSets[0].resources[0].point.coordinates[0], result.resourceSets[0].resources[0].point.coordinates[1]);
      // Create an info box 
      var infoboxOptions = {width:300, 
                            height: 100, 
                            title: "Information Box Title", 
                            description: "This is the map.", 
                            showPointer: false, 
                            offset: new Microsoft.Maps.Point(-100,0)};
      var myInfobox = new Microsoft.Maps.Infobox(location, infoboxOptions);
      
      // Add a pushpin at the found location
      var pushpinOptions = 
      {
        width: 25,
        height: 39,
        infobox: myInfobox
      };
      var pushpin = new Microsoft.Maps.Pushpin(location, null);
      var pushpinOver= Microsoft.Maps.Events.addHandler(pushpin, 'mouseover', displayEventInfo);
       
      map.entities.push(pushpin, pushpinOptions);
    }
}
      
displayEventInfo = function (e) 
{
  //map.entities.push(e.target);
  //alert(e.target);
}


function CallRestService(request) 
{
   var script = document.createElement("script");
   script.setAttribute("type", "text/javascript");
   script.setAttribute("src", request);
   document.body.appendChild(script);
}
