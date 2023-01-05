
// initialize data to be sent to python server
let data = {}

// initialize list of sport ids
let ids = ["MBH", "MBA", "WBH", "WBA", "MLH", "MLA", "WSH", "WSA", "UFH", "UFA"]

// initialize variables: if not equal to zero then unable to send a server request
let eligiblePhone = true
let eligibleName = true
let eligibleCheck = true

// runs when user clicks the submit button
function submitted(){

    // for loop to iterate through the ids list
    for (let i = 0; i < ids.length; i++){

        // creates a new key within the data variable based on id name and assigns corresponding boolean value
        data[ids[i]] = document.getElementById(ids[i]).checked
    }

    // stores the input field value in the variable phoneNum
    let phoneNum = parseInt(document.getElementById('phone').value)

    // if phoneNum's value is not ten digits throw error function
    if (phoneNum.toString().length !== 10){
        
        // calls error function to establish a current error
        handlePhoneError(true)
    } else {
        // calls error function and establishes that there is no current error
        handlePhoneError(false)
    }

    // adds the phone number key and value to data
    data["phoneNumber"] = phoneNum

    let name = document.getElementById('name').value

    if (name.indexOf(' ') !== -1){
        // no error (contains a space)
        handleNameError(false)
    } else {
        // there is no space
        handleNameError(true)
    }

    // adds the name key and value to data
    data["fullName"] = name

    // check for checkbox error
    handleCheckBoxError()

    // check if eligible to send to server
    if (eligibleCheck && eligibleName && eligiblePhone){
        finalFunc()
    }

}

// displays text to user if their phone input is unusable
function handlePhoneError(bool){
    if (bool === true){
        document.getElementsByClassName('phoneError')[0].style.display = 'block'
        eligiblePhone = false
    }
    if (bool === false){
        document.getElementsByClassName('phoneError')[0].style.display = 'none'
        eligiblePhone = true
    }
}

// displays text to user if their name input is invalid
function handleNameError(bool){
    if (bool === true){
        document.getElementsByClassName('nameError')[0].style.display = 'block'
        eligibleName = false
    }
    if (bool === false){
        document.getElementsByClassName('nameError')[0].style.display = 'none'
        eligibleName = true
    }
}

// displays text to user if they did not check any boxes
function handleCheckBoxError(){
    let checkCounter = 0

    // for loop iterate through the id of each sport
    for (i = 0; i < ids.length; i++){

        // checks id the id of each sport in data is false
        if (data[ids[i]] == false){

        } else {
            checkCounter = checkCounter + 1
        }
    }

    if (checkCounter > 0){
        // all good
        document.getElementsByClassName('checkError')[0].style.display = 'none'
        eligibleCheck = true
    } else {
        // send error
        document.getElementsByClassName('checkError')[0].style.display = 'block'
        eligibleCheck = false
    }
}

function finalFunc(){
    // print data to console
    console.log(data)

    document.getElementsByClassName('success')[0].style.color = "blue"
    document.getElementsByClassName('success')[0].style.margin = "auto"
    document.getElementsByClassName('success')[0].style.display = "block"

}


// edited