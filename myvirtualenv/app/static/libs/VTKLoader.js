/**
 * @author mrdoob / http://mrdoob.com/
 */

THREE.VTKLoader = function () {};

THREE.VTKLoader.prototype = {

    constructor: THREE.VTKLoader,

    addEventListener: THREE.EventDispatcher.prototype.addEventListener,
    hasEventListener: THREE.EventDispatcher.prototype.hasEventListener,
    removeEventListener: THREE.EventDispatcher.prototype.removeEventListener,
    dispatchEvent: THREE.EventDispatcher.prototype.dispatchEvent,

    load: function ( url, callback ) {

        var scope = this;
        var request = new XMLHttpRequest();

        request.addEventListener( 'load', function ( event ) {

            var res = scope.parse( event.target.responseText );

            scope.dispatchEvent( { type: 'load', content: res } );

            if ( callback ) callback( res);

        }, false );


        request.addEventListener( 'progress', function ( event ) {

            scope.dispatchEvent( { type: 'progress', loaded: event.loaded, total: event.total } );

        }, false );

        request.addEventListener( 'error', function () {

            scope.dispatchEvent( { type: 'error', message: 'Couldn\'t load URL [' + url + ']' } );

        }, false );

        request.open( 'GET', url, true );
        request.send( null );

    },



    parse: function ( data ) {

       
        var res= new Object();
       
        var value = [];
        

        function addValue(x){
            value.push(x);
        }

        var pattern, result;


        pattern = /DIMENSIONS+[ ]+([\d]+)[ ]+([\d]+)[ ]+([\d]+)/g;

        if ( result = pattern.exec( data ) ) {
            res.dimension = [parseInt(result[1]), parseInt(result[2]), parseInt(result[3])];
        }

        pattern = /ORIGIN+[ ]+([\+|\-]?[\d]+)[ ]+([\+|\-]?[\d]+)[ ]+([\+|\-]?[\d]+)/g;

        if ( result = pattern.exec( data ) ) {
            res.origin = [parseInt(result[1]), parseInt(result[2]), parseInt(result[3])];
        }

        pattern = /SPACING+[ ]+([\+|\-]?[\d]+[\.][\d]+)[ ]+([\+|\-]?[\d]+[\.][\d]+)[ ]+([\+|\-]?[\d]+[\.][\d]+)/g;

        if ( result = pattern.exec( data ) ) {
            res.spacing = [parseInt(result[1]), parseInt(result[2]), parseInt(result[3])];
        }

        // float
        //var lookupTable = "LOOKUP_TABLE default"
        var scalar = data.split("default")[1]; 
        //console.log(scalar);
        pattern = /[\+|\-]?\d+[\.\d]+[\s]/g;
        while ( ( result = pattern.exec( scalar ) ) != null ){

            addValue( parseFloat(result));
        }
        //console.log(result);

        // 3 int int int




        //geometry.computeCentroids();
        // geometry.computeFaceNormals();
        // geometry.computeVertexNormals();
        // geometry.computeBoundingSphere();
        res.weight = value;

        return res;

    }

}; 