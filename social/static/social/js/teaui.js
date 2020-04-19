var tempLabel
var startButton
var statusLabel

// Updates the UI temperature field
function stateUpdate(newState) {
    if (newState.freedomUnits == true) {
        tempLabel.innerText = newState.temp.toFixed(2) + "°F"
    } else {
        tempLabel.innerText = newState.temp.toFixed(2) + "°C"
    }
    if (newState.isDone == true) {
        statusLabel.innerText = "Status: Done!"
        startButton.setAttribute("class", "btn btn-success")
        if (newState.count == 0) {
            alert("Your tea is done now")
            teaModel.count = 1;
        }
    }
    if (newState.isBrewing == true) {
        statusLabel.innerText = "Status: Brewing"
        startButton.setAttribute("class", "btn btn-warning")
    }
    if (newState.isBrewing != true && newState.isDone != true) {
        statusLabel.innerText = "Status: Idle"
        startButton.setAttribute("class", "btn btn-success")
    }
}

function unitsChange() {
    if (tempLabel.getAttribute("data-units") == "fahrenheit") {
        tempLabel.setAttribute("data-units", "celsius")
        teaModel.displayCelsius(true)
    } else {
        tempLabel.setAttribute("data-units", "fahrenheit")
        teaModel.displayCelsius(false)
    }
}

function brewingChange() {
    teaModel.startBrewing(true)
    startButton.setAttribute("class", "btn btn-warning")
}

// UI setup
document.addEventListener("DOMContentLoaded", function(event) {
    tempLabel = document.getElementById("tempLabel")
    statusLabel = document.getElementById("statusLabel")
    startButton = document.getElementById("startButton")

    tempLabel.addEventListener("click", unitsChange)
    startButton.addEventListener("click", brewingChange)

    teaModel.setStateChangeListener(stateUpdate)
    teaModel.setup()
});
