
class Style:

    style_bt_standard = """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(80, 94, 134);
        background-color: rgb(80, 94, 134);
        border-top-left-radius: 15px;
        border-bottom-left-radius: 15px;
        text-align: left;
        padding-left: 45px;
    }
    
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(80, 94, 134);
        background-color: rgb(80, 94, 134);
        text-align: left;
        border-top-left-radius: 20%;
        border-bottom-left-radius: 20%;
        padding-left: 45px;
    }
    
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 28px solid rgb(33, 37, 43);
    }
    
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    
    """

    style_bt_wallet = """
QPushButton {
	background-position: center;
	background-repeat: no-reperat;
	border:  rgb(27, 29, 35);
    background-color: rgb(80, 94, 134);
	border-radius:5%;
}
QPushButton:hover {
	background-color: rgb(33, 37, 43);
}
QPushButton:pressed {	
	background-color: rgb(85, 170, 255);
}"""
