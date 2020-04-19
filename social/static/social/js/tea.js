var myParticleAccessToken = "932e399794adf34fc02219e406d84350d4a50458"
var myDeviceId = "440030000c47363433353735"
var topic = "temperature"

var secondDeviceId = "3a002b000b47373336323230"

function newTeaEvent(objectContainingData) {
    var tempObject = JSON.parse(objectContainingData.data)
    console.log(tempObject)
    teaModel.fahrenheitTemp = tempObject.fahrenheit
    teaModel.celsiusTemp = tempObject.celsius
    if (teaModel.fahrenheitTemp >= 85) {
        teaModel.isDone()
    }
    teaModel.stateChange()
}

// Tea model
var teaModel = {
    particle: null,
    stateChangeListener: null,
    freedomUnits: true,
    fahrenheitTemp: 0,
    celsiusTemp: 0,
    brewing: false,
    done: false,
    count: 0,

    startBrewing: function(enabled) {
        this.brewing = enabled
        this.done = false
        this.count = 0

        if (enabled) {
            var functionData = {
                deviceId: secondDeviceId,
                name: "brewing",
                argument: "" + enabled,
                auth: myParticleAccessToken
            }
            function onSuccess(e) { console.log("brewing call success") }
            function onFailure(e) { console.log("brewing call failed")
                console.dir(e) }
            particle.callFunction(functionData).then(onSuccess, onFailure)
        }
    },

    isDone: function() {
        this.brewing = false
        this.done = true

        var functionData = {
                deviceId: secondDeviceId,
                name: "isDone",
                argument: "" + this.done,
                auth: myParticleAccessToken
            }
            function onSuccess(e) { console.log("isDone call success") }
            function onFailure(e) { console.log("isDone call failed")
                console.dir(e) }
            particle.callFunction(functionData).then(onSuccess, onFailure)
        },


    displayCelsius: function(enabled) {
        if (enabled) {
            this.freedomUnits = false
        }
        else {
            this.freedomUnits = true
        }
    },

    setStateChangeListener: function(aListener) {
        this.stateChangeListener = aListener
    },

    // Updates temp according to the state
    stateChange: function() {
        if (this.stateChangeListener) {
            var state = {}
            if (this.freedomUnits) {
                state = {
                    temp: this.fahrenheitTemp,
                    freedomUnits: this.freedomUnits,
                    isDone: this.done,
                    isBrewing: this.brewing,
                    count: this.count
                }
            }
            else {
                state = {
                    temp: this.celsiusTemp,
                    freedomUnits: this.freedomUnits,
                    isDone: this.done,
                    isBrewing: this.brewing,
                    count: this.count
                }
            }
            this.stateChangeListener(state)
        }
    },

    // Function that gets an event listener to a particle stream
    setup: function () {
        particle = new Particle();
        function onSuccess(stream) {
                    console.log("getEventStream Success")
                    stream.on('event', newTeaEvent)
                  }

              function onFailure(e) {
                          console.log("getEventStream call failed")
                          console.dir(e)
                        }
              particle.getEventStream( { name: topic, auth: myParticleAccessToken, deviceId: myDeviceId }).then(onSuccess, onFailure)
            }
      }
