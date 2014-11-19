/* File: main.cpp
 *
 * Neural Networks, Fall 2014
 *
 * Add documentation here...
 *
 * NOTES:
 * Representation of the screen pixels:
 *   ale.screen_matrix: IntMatrix === vector< vector<int> >
 * State:
 *  ale.game_controller->getState()
 *
 * ROM_DIRECTORY has been pre-defined by the Makefile.
 */

#include <iostream>
#include <string>
#include <vector>
#include "ale_interface.hpp"
#include "rlglue/RL_glue.h"

using namespace std;

typedef map<long,CompositeObject>::iterator ObjMapItr;
#define OBJECTS ale.visProc->composite_objs


#define MESSAGE_START "<IPC_MSG_BEGIN>"
#define MESSAGE_END "<IPC_MSG_END>"


void sendPipeMessage(string message)
{
    cout << MESSAGE_START << endl;
    cout << message << endl;
    cout << MESSAGE_END << endl;
}

void sendPipeMessage(vector<string> lines)
{
    cout << MESSAGE_START << endl;
    for(vector<string>::iterator it = lines.begin();
        it != lines.end();
        it++)
    {
        cout << (*it) << endl;
    }
    cout << MESSAGE_END << endl;
}

int getActionFromPipe()
{
    string msg;
    cin >> msg;
    while(msg != MESSAGE_START)
        cin >> msg;
    cin >> msg;
    int action = stoi(msg);
    while(msg != MESSAGE_END)
        cin >> msg;
    return action;
}


int main(int argc, char** argv)
{
    // set up the rom path
    if(argc < 2)
    {
        cout << "Please provide the name of a rom file." << endl;
        return 0;
    }
    string rom_file = string(ROM_DIRECTORY) + "/" + string(argv[1]) + ".bin";
    cout << "Loading ROM: " << rom_file << endl;


    // set up the emulator and load the rom
    ALEInterface ale;
    bool disp_screen = false;
    bool proc_screen = true;
    ale.loadROM(rom_file, disp_screen, proc_screen);

    // send initial greeting and set of valid actions
    sendPipeMessage("Hello from C++!");
    vector<string> legal_actions;
    for(ActionVect::iterator it = ale.legal_actions.begin();
        it != ale.legal_actions.end();
        it++)
    {
        legal_actions.push_back(to_string(*it));
    }
    sendPipeMessage(legal_actions);

    // play n episodes
    const int num_episodes = 3;
    for(int i=0; i<num_episodes; i++)
    {
        float total_reward = 0;

        while(!ale.game_over())
        {
            // send the state to python
            vector<string> obj_params;
            for(ObjMapItr it = OBJECTS.begin(); it != OBJECTS.end(); it++)
            {
                CompositeObject &obj = it->second;
                obj_params.push_back(to_string(obj.id));
                obj_params.push_back(to_string(obj.x_velocity));
                obj_params.push_back(to_string(obj.y_velocity));
                obj_params.push_back(to_string(obj.x_min));
                obj_params.push_back(to_string(obj.x_max));
                obj_params.push_back(to_string(obj.y_min));
                obj_params.push_back(to_string(obj.y_max));
                obj_params.push_back(to_string(obj.frames_since_last_movement));
                obj_params.push_back(to_string(obj.age));
            }
            sendPipeMessage(obj_params);

            // get an action selection from python
            int choice = getActionFromPipe();
            Action a = ale.legal_actions[choice];
            
            // apply the action and send back the reward
            float reward = ale.act(a);
            sendPipeMessage(to_string(reward));
            total_reward += reward;
        }

        cout << "Episode " << (i+1) << ", score = " << total_reward << endl;
        if(total_reward < 100)
            cout << "Wow, you really suck." << endl;
        ale.reset_game();
    }
}

