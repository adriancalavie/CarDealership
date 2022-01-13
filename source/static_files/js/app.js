"use strict";

const Navbar = document.getElementsByClassName("nav_list")[0];
const Menu = document.getElementsByClassName("menu")[0];
const OpenBtn = document.getElementsByClassName("open_Btn")[0];
const CloseBtn = document.getElementsByClassName("close_Btn")[0];
const Content = document.getElementsByClassName("main")[0];
const Logo = document.getElementsByClassName("logo")[0];
const MenuItems = document.getElementsByClassName("menu_item");

// console.log(MenuItems)

let isMenuOpen = false;

function navigate(path) {
    console.log(path)
    window.location = path;
    console.log(window.location)
}

function setIsMenuOpen() {

    isMenuOpen = !isMenuOpen;
    isMenuOpen
        ? (Navbar.style.width = "100%") &&
        (Menu.style.opacity = "1") &&
        (Menu.style.visibility = "visible") &&
        (Menu.style.display = "flex") &&
        (OpenBtn.style.display = "none") &&
        (CloseBtn.style.display = "block") &&
        (Content.style.opacity = "0") &&
        (Content.style.visibility = "hidden") &&
        (Content.style.display = "none")
        
        : (Navbar.style.width = "90%") &&
        (Menu.style.opacity = "0") &&
        (Menu.style.visibility = "hidden") &&
        (Menu.style.display = "none") &&
        (OpenBtn.style.display = "block") &&
        (CloseBtn.style.display = "none") &&
        (Content.style.opacity = "1") &&
        (Content.style.visibility = "visible") &&
        (Content.style.display = "flex");

    for (var element of MenuItems) {
        console.log(element);
        element.disabled = isMenuOpen ? false : true
        element.style.pointerEvents = isMenuOpen ? "all" : "none"
        console.log(element);
    }
}