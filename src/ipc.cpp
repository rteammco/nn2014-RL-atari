#include "ipc.h"

#include <iostream>

using namespace std;


// Send a single message using the pipes.
void ALEComm::sendMessage(string message)
{
    if(!enabled)
        return;
    cout << MESSAGE_START << endl;
    cout << message << endl;
    cout << MESSAGE_END << endl;
}


// Send multiple messages using the pipes.
void ALEComm::sendMessage(vector<string> lines)
{
    if(!enabled)
        return;
    cout << MESSAGE_START << endl;
    for(vector<string>::iterator it = lines.begin();
        it != lines.end();
        it++)
    {
        cout << (*it) << endl;
    }
    cout << MESSAGE_END << endl;
}


// Returns a message from the pipe.
string ALEComm::getMessage()
{
    if(!enabled)
        return "";
    string msg;
    cin >> msg;
    while(msg != MESSAGE_START) {
        cin >> msg;
    }
    cin >> msg;
    //cerr << "GOT MESSAGE: " << msg << endl;
    // TODO - buggy (only gets first letter?)
    return msg;
}


// Returns an action selection (int) from the pipe.
int ALEComm::getAction()
{
    if(!enabled)
        return 0;
    return stoi(getMessage());
}


// Returns a boolean value from the pipe (true or false).
bool ALEComm::getBool()
{
    if(!enabled)
        return false;
    if(getMessage() == "T") // TODO - True not T
        return true;
    else
        return false;
}


// Returns TRUE if the next message is a GAME_START message.
bool ALEComm::isGameStarting()
{
    if(!enabled)
        return true;
    if(getMessage() == GAME_START)
        return true;
    else
        return false;
}
