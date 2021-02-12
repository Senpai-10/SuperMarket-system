#include <iostream>
#include <string>

class color {
    public:
        std::string reset = "\33[0m";
        const char *HelpMessage = R""""(Color class help message
---------------------------------

    bold
    italic
    url
    blink
    blink2
    selected
    white
    black

Dark colors:

    darkRed
    darkGreen
    darkYellow
    darkBlue
    darkViolet
    darkBeige
    darkWhite

Light colors:

    lightGrey
    lightRed
    lightGreen
    lightYellow
    lightBlue
    lightViolet
    lightBeige

bg(background) colors:

    bgBlack
    bgRed
    bgGreen
    bgYellow
    bgBlue
    bgViolet
    bgBeige
    bgWhite

    Light background colors:

        bgLightGrey
        bgLightRed
        bgLightGreen
        bgLightYellow
        bgLightBlue
        bgLightViolet
        bgLightBeige
        bgLightWhite
)"""";

        void help() {
            std::cout << HelpMessage;
        }
        
        std::string bold(std::string msg) {return "\33[1m" + msg + reset;}
        std::string italic(std::string msg) {return "\33[3m" + msg + reset;}
        std::string url(std::string msg) {return "\33[4m" + msg + reset;}
        std::string blink(std::string msg) {return "\33[5m" + msg + reset;}
        std::string blink2(std::string msg) {return "\33[6m" + msg + reset;}
        std::string selected(std::string msg) {return "\33[7m" + msg + reset;}
        std::string white(std::string msg) {return "\33[97m" + msg + reset;}
        std::string black(std::string msg) {return "\33[30m" + msg + reset;}
        
        std::string darkRed(std::string msg) {return "\33[31m" + msg + reset;}
        std::string darkGreen(std::string msg) {return "\33[32m" + msg + reset;}
        std::string darkYellow(std::string msg) {return "\33[33m" + msg + reset;}
        std::string darkBlue(std::string msg) {return "\33[34m" + msg + reset;}
        std::string darkViolet(std::string msg) {return "\33[35m" + msg + reset;}
        std::string darkBeige(std::string msg) {return "\33[36m" + msg + reset;}
        std::string darkWhite(std::string msg) {return "\33[37m" + msg + reset;}
        
        std::string lightGrey(std::string msg) {return "\33[90m" + msg + reset;}
        std::string lightRed(std::string msg) {return "\33[91m" + msg + reset;}
        std::string lightGreen(std::string msg) {return "\33[92m" + msg + reset;}
        std::string lightYellow(std::string msg) {return "\33[93m" + msg + reset;}
        std::string lightBlue(std::string msg) {return "\33[94m" + msg + reset;}
        std::string lightViolet(std::string msg) {return "\33[95m" + msg + reset;}
        std::string lightBeige(std::string msg) {return "\33[96m" + msg + reset;}
        
        std::string bgBlack(std::string msg) {return "\33[40m" + msg + reset;}
        std::string bgRed(std::string msg) {return "\33[41m" + msg + reset;}
        std::string bgGreen(std::string msg) {return "\33[42m" + msg + reset;}
        std::string bgYellow(std::string msg) {return "\33[43m" + msg + reset;}
        std::string bgBlue(std::string msg) {return "\33[44m" + msg + reset;}
        std::string bgViolet(std::string msg) {return "\33[45m" + msg + reset;}
        std::string bgBeige(std::string msg) {return "\33[46m" + msg + reset;}
        std::string bgWhite(std::string msg) {return "\33[47m" + msg + reset;}
        
        std::string bgLightGrey(std::string msg) {return "\33[100m" + msg + reset;}
        std::string bgLightRed(std::string msg) {return "\33[101m" + msg + reset;}
        std::string bgLightGreen(std::string msg) {return "\33[102m" + msg + reset;}
        std::string bgLightYellow(std::string msg) {return "\33[103m" + msg + reset;}
        std::string bgLightBlue(std::string msg) {return "\33[104m" + msg + reset;}
        std::string bgLightViolet(std::string msg) {return "\33[105m" + msg + reset;}
        std::string bgLightBeige(std::string msg) {return "\33[106m" + msg + reset;}
        std::string bgLightWhite(std::string msg) {return "\33[107m" + msg + reset;}
        
        
};
