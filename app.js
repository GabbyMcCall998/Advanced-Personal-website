const express = require("express");
const app = express();


app.use(express.static('public'));



app.get("/",function(req,res){
res.sendFile(__dirname+ "/index - Copy.html");
});


app.listen(5000,function(){
    console.log("The app is running on port 5000");
});

