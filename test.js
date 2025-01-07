const myTime = "2021-06-11,2024-07-12"


function getTime(tenure) {
    const start = new Date(tenure.split(",")[0]).getTime();
    const today = new Date();
    today.setUTCHours(0, 0, 0, 0);
    console.log(typeof today)
    const end = tenure.split(",")[1].length > 0 ? new Date(tenure.split(",")[1]) : today.getTime();
    return (end - start) / 86400000;
}

console.log(getTime(myTime));