from flet import *;

def color_method(color: str):

    match color:
        case "AMBER":
            return colors.AMBER;
        case "RED":
            return colors.RED;
        case "BLUE":
            return colors.BLUE;
        case "GREEN":
            return colors.GREEN
        
def inverse_color_method(color: str):

    match color:
        case colors.AMBER:
            return "AMBER";
        case colors.RED:
            return "RED";
        case colors.BLUE:
            return "BLUE";
        case colors.GREEN:
            return "GREEN"