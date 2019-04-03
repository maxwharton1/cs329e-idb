#this file handles conversions from url and to url. you're mostly going from url in python

def toURL(s){
    s.replace(" ", "_")
    return s
}

def fromURL(s){
    s.replace("_", " ")

    if s == "Kevin OLeary"{
        s = "Kevin O'Leary"
    }

    return s
}
