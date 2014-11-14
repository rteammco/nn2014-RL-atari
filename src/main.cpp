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
#include "ale_interface.hpp"
#include "rlglue/RL_glue.h"

using namespace std;


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


    // TODO: see rlglue/examples/skeleton/SkeletonExperiment.c for more info
    // on incorporating RLGlue agent.


    // play n episodes
    const int num_episodes = 3;
    for(int i=0; i<num_episodes; i++)
    {
        float total_reward = 0;

        while(!ale.game_over())
        {
            // TODO - here is the map of all objects in the frame:
            // std::map<long,CompositeObject> (id => obj)
            cout << ale.visProc->composite_objs.size() << endl;
            // struct CompositeObject defined at:
            //  ale/src/common/visual_processor.h, 178

            // choose an action
            int choice = rand() % ale.legal_actions.size();
            Action a = ale.legal_actions[choice];
            
            // apply the action
            float reward = ale.act(a);
            total_reward += reward;

            // TODO - communicatin with python
            // to py: timestamp, state, action set, reward(t-1)
            // from py: selected action
        }

        cout << "Episode " << (i+1) << ", score = " << total_reward << endl;
        if(total_reward < 100)
            cout << "Wow, you really suck." << endl;
        ale.reset_game();
    }
}

