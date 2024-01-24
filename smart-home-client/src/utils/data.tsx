import React from "react";
import {
  FaFacebookF,
  FaInstagram,
  FaLinkedin,
  FaTwitter,
} from "react-icons/fa";


export const theme = {
  colors: {
    main: "#b4e854",
    secondColor: "#263d3d",
    textColor: "white",
    red: "#f54263",
    grey: "#f0f0f0",
  },
  radius: {
    buttons: "4px",
  },
  fontSizes: {
    standard: "14px",
    large: "16px",
    small: "12px",
    header: "30px",
  },
};

export const icons = [
  { href: "https://www.facebook.com", icon: <FaFacebookF /> },
  { href: "https://www.twitter.com", icon: <FaTwitter /> },
  { href: "https://www.instagram.com", icon: <FaInstagram /> },
  { href: "https://www.linkedin.com", icon: <FaLinkedin /> },
];

export const infoItems = [
  { label: "Email", value: "smarthomeiot@gmail.com" },
  { label: "Phone", value: "+371 65 788 399" },
  { label: "Address", value: "Mise Dimitrijevica 43, Novi Sad" },
];
export const navbarTitle = "Smart Home";
  
  export const menuOptions = [
    { href: "", value: "Home"},
    { href: "/devices", value: "Devices" },
    { href: "#", value: "Login" },
    { href: "#", value: "Contact"},
  ];


  export const urls = [
    { type: "DHT", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=5s&from=1706041300054&to=1706041600054&viewPanel=3"},
    { type: "PIR", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=5s&from=1706041147050&to=1706041447050&viewPanel=4"},
    { type: "DUS", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=5s&from=1706041472428&to=1706041772428&viewPanel=5"},
    { type: "DS", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=5s&from=1706041371810&to=1706041671810&viewPanel=2"},
    { type: "DL", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=5s&from=1706041349239&to=1706041649239&viewPanel=1"},
    { type: "LCD", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=1d&from=1706096610941&to=1706100210941&viewPanel=7"},
    {type: "GYRO", url: ""},
    { type: "RGB", url: "" },
    { type: "IR", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=1d&from=1706111847715&to=1706112147715&viewPanel=9"},
    { type: "4SG", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=1d&from=1706096756494&to=1706100356494&viewPanel=8"},
    { type: "MS", url: "http://localhost:3000/d/e19f86a9-66db-4f92-adc4-a20c2a76738c/iot?orgId=1&refresh=5s&from=1706041324930&to=1706041624930&viewPanel=6"},


  ]
  export const devices = [
    { id : "RDHT1", name: "Room DHT 1", piNumber: 1, type:"DHT"},
    { id : "RDHT2", name: "Room DHT 2", piNumber: 1, type:"DHT"},
    { id : "RDHT3", name: "Room DHT 3", piNumber: 2, type:"DHT"},
    { id : "RDHT4", name: "Room DHT 4", piNumber: 3, type:"DHT"},
    { id : "GDHT", name: "Garage DHT", piNumber: 2, type:"DHT"},

    { id : "DPIR1", name: "Door PIR 1", piNumber: 1, type:"PIR"},
    { id : "DPIR2", name: "Door PIR 2", piNumber: 2, type:"PIR"},
    { id : "RPIR1", name: "Room PIR 1", piNumber: 1, type:"PIR"},
    { id : "RPIR2", name: "Room PIR 2", piNumber: 2, type:"PIR"},
    { id : "RPIR3", name: "Room PIR 3", piNumber: 2, type:"PIR"},
    { id : "RPIR4", name: "Room PIR 4", piNumber: 3, type:"PIR"},

    { id : "DUS1", name: "Door Ultrasonic Sensor 1", piNumber: 3, type:"DUS", url: ""},
    { id : "DUS2", name: "Door Ultrasonic Sensor 2", piNumber: 3, type:"DUS", url: ""},

    { id : "DS1", name: "Door Sensor 1", piNumber: 3, type:"DS", url: ""},
    { id : "DS2", name: "Door Sensor 2", piNumber: 3, type:"DS", url: ""},

    { id : "DL", name: "Door Light", piNumber: 1, type:"DL", url: ""},

    { id : "GLCD", name: "Garage LCD", piNumber: 2, type:"LCD", url: ""},

    { id : "GRG", name: "Gun Safe Gyro", piNumber: 2, type:"GYRO", url: ""},

    { id : "BRGB", name: "Bedroom RGB", piNumber: 3, type:"RGB", url: ""},

    { id : "BIR", name: "Bedroom Infrared", piNumber: 3, type:"IR", url: ""},

    { id : "B4SG", name: "Bedroom 4 Digit 7 Segment Display", piNumber: 3, type:"4SG", url: ""},

    { id : "DMS", name: "Door Membrane Switch", piNumber: 1, type:"MS", url: ""},











  ]
  


