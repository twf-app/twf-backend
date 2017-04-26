function app() {
    "use strict";

    // Closure Variables
    var markers = [];
    var meters = 100;
    var map;

    (function user_loc() {
        navigator.geolocation.getCurrentPosition(function (position) {
            var user_loc = {lat: position.coords.latitude, lng: position.coords.longitude};
            initMap(user_loc)
        })
    })();


    function addYourLocationButton(map, marker) {
        var controlDiv = document.createElement('div');

        var firstChild = document.createElement('button');
        firstChild.style.backgroundColor = '#fff';
        firstChild.style.border = 'none';
        firstChild.style.outline = 'none';
        firstChild.style.width = '28px';
        firstChild.style.height = '28px';
        firstChild.style.borderRadius = '2px';
        firstChild.style.boxShadow = '0 1px 4px rgba(0,0,0,0.3)';
        firstChild.style.cursor = 'pointer';
        firstChild.style.marginRight = '10px';
        firstChild.style.padding = '0px';
        firstChild.title = 'Your Location';
        controlDiv.appendChild(firstChild);

        var secondChild = document.createElement('div');
        secondChild.style.margin = '5px';
        secondChild.style.width = '18px';
        secondChild.style.height = '18px';
        secondChild.style.backgroundImage = 'url(https://maps.gstatic.com/tactile/mylocation/mylocation-sprite-1x.png)';
        secondChild.style.backgroundSize = '180px 18px';
        secondChild.style.backgroundPosition = '0px 0px';
        secondChild.style.backgroundRepeat = 'no-repeat';
        secondChild.id = 'you_location_img';
        firstChild.appendChild(secondChild);

        google.maps.event.addListener(map, 'dragend', function () {
            $('#your_location_img').css('background-position', '0px 0px');
        });

        firstChild.addEventListener('click', function () {
            var imgX = '0';
            var animationInterval = setInterval(function () {
                if (imgX === '-18') imgX = '0';
                else imgX = '-18';
                $('#your_location_img').css('background-position', imgX + 'px 0px');
            }, 500);
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                    marker.setPosition(latlng);
                    map.setCenter(latlng);
                    clearInterval(animationInterval);
                    $('#your_location_img').css('background-position', '-144px 0px');
                });
            }
            else {
                clearInterval(animationInterval);
                $('#your_location_img').css('background-position', '0px 0px');
            }
        });

        controlDiv.index = 1;
        map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(controlDiv);
    }


    function initMap(user_loc) {

        map = new google.maps.Map(document.getElementById('map-canvas'), {
            zoom: 16,
            center: user_loc,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true,
            styles: [
                {elementType: 'geometry', stylers: [{color: '#bbc5c9'}]},
                {elementType: 'labels.text.stroke', stylers: [{color: '#112636'}]},
                {elementType: 'labels.text.fill', stylers: [{color: '#5bf5fd'}]},
                {
                    featureType: 'administrative.locality',
                    elementType: 'labels.text.fill',
                    stylers: [{color: '#06e0ff'}]
                },
                {
                    featureType: 'poi',
                    elementType: 'labels.text.fill',
                    stylers: [{color: '#6ecaff'}]
                },
                {
                    featureType: 'poi.park',
                    elementType: 'geometry',
                    stylers: [{color: '#263c3f'}]
                },
                {
                    featureType: 'poi.park',
                    elementType: 'labels.text.fill',
                    stylers: [{color: '#6b9a76'}]
                },
                {
                    featureType: 'road',
                    elementType: 'geometry',
                    stylers: [{color: '#38414e'}]
                },
                {
                    featureType: 'road',
                    elementType: 'geometry.stroke',
                    stylers: [{color: '#212a37'}]
                },
                {
                    featureType: 'road',
                    elementType: 'labels.text.fill',
                    stylers: [{color: '#9ca5b3'}]
                },
                {
                    featureType: 'road.highway',
                    elementType: 'geometry',
                    stylers: [{color: '#746855'}]
                },
                {
                    featureType: 'road.highway',
                    elementType: 'geometry.stroke',
                    stylers: [{color: '#1f2835'}]
                },
                {
                    featureType: 'road.highway',
                    elementType: 'labels.text.fill',
                    stylers: [{color: '#9cf335'}]
                },
                {
                    featureType: 'transit',
                    elementType: 'geometry',
                    stylers: [{color: '#2f3948'}]
                },
                {
                    featureType: 'transit.station',
                    elementType: 'labels.text.fill',
                    stylers: [{color: '#fca000'}]
                },
                {
                    featureType: 'water',
                    elementType: 'geometry',
                    stylers: [{color: '#17263c'}]
                },
                {
                    featureType: 'water',
                    elementType: 'labels.text.fill',
                    stylers: [{color: '#515c6d'}]
                },
                {
                    featureType: 'water',
                    elementType: 'labels.text.stroke',
                    stylers: [{color: '#17263c'}]
                }
            ]
        });

        var image = '/static/img/my_profile.png';
        var user_marker = new google.maps.Marker({
            position: user_loc,
            map: map,
            icon: image,
            title: 'You are here.'
        });

        addYourLocationButton(map, user_marker);
    }


    function add_users(nearby_users) {
        var marker;
        var userIcon = '/static/img/testuser1.png';
        $.each(nearby_users, function (index, user) {
            console.log(user);
            var pos = user.zone.location.position.split(',');
            var nearby_user_loc = {lat: parseFloat(pos[0]), lng: parseFloat(pos[1])};
            var contentUser = $('<content>').addClass('user_info');
            var userImage = $('<img>', {'src': user.member.image, 'class': 'member_image'});
            var userName = $('<p>').text(user.member.username);
            var userEmail = $('<p>').text(user.member.email);
            contentUser.append(userImage, userName, userEmail);
            var infowindow = new google.maps.InfoWindow({
                disableAutoPan: true,
                content: contentUser.html(),
                position: nearby_user_loc
            });

            marker = new google.maps.Marker({
                position: new google.maps.LatLng(nearby_user_loc.lat, nearby_user_loc.lng),
                animation: google.maps.Animation.DROP,
                title: (user.member.username) + '  is  ' + 'Checked-in',
                map: map
                // icon: userIcon
            });
            marker.addListener('click', function () {
                map.panTo(marker.getPosition());
                infowindow.open(map, marker);
            });
            markers.push(marker);
        })
    }


    function postCheckin(user_loc, meters) {
        if (typeof $meters === "undefined") {
            var $meters = 500;
        }
        $.ajax({

            url: '/members/check_ins/',   // Target Server
            method: 'POST',                                            // Request Verb
            data: {
                'lat': user_loc.lat,
                'lng': user_loc.lng,
                'radius': meters
            },                                                       // Request Params
            success: function (rsp) {                                // Success Handler
                swal({
                    imageUrl: 'https://premium.wpmudev.org/blog/wp-content/uploads/2015/09/nasa-scroll2.gif',
                    type: "success",
                    title: "You are Checked-In!"
                })
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
                swal({
                    imageUrl: 'https://veggiefoodlover.files.wordpress.com/2017/02/giphy-74.gif?w=584',
                    type: "error",
                    title: "Failed to Checked-In!"
                })
            }
        });
    }


    function get_loc(meters) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var user_loc = {lat: position.coords.latitude, lng: position.coords.longitude};
            postCheckin(user_loc, meters);
            getCheckin(user_loc, meters);
        });
    }


    $('#check_in').on('click', function (event) {
        event.preventDefault();
        // marker.setMap(null);
        get_loc(meters);
    });


    function getCheckin(user_loc, meters) {
        if (typeof $meters === "undefined") {
            var $meters = 500;
        }
        $.ajax({
            url: '/members/check_ins/',   // Target Server
            method: 'GET',                                            // Request Verb
            data: {
                'lat': user_loc.lat,
                'lng': user_loc.lng,
                'radius': meters
            },                                                      // Request Params
            success: function (rsp) {                                // Success Handler
                var nearby_users = rsp;
                add_users(nearby_users);
            },
            error: function (err) {                                  // Error Handler
                console.log(err);
            }
        });
    }
}