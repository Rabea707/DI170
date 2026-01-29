function userInfo(userName, userAge) {
    if (userName !== "Sarah") {
        return;
    } 
    alert("You are not the right person");
}

let girlInfo = userInfo("Sarah", 22);
console.log(girlInfo); //undefined