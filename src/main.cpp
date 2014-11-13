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


// Runtime options and argument strings
#define ARG_DISP_SCREEN "disp"
#define FLAG_DISP_SCREEN 1
#define ARG_PROC_SCREEN "proc"
#define FLAG_PROC_SCREEN 2


// Process arguments and return an options int with all
// the option flags summed up.
unsigned int processOptionalArgs(int argc, char** argv)
{
    unsigned int options = 0;
    for(int i=0; i<argc; i++)
    {
        string arg = string(argv[i]);
        if(arg.find(ARG_DISP_SCREEN))
            options += FLAG_DISP_SCREEN;
        else if(arg.find(ARG_PROC_SCREEN))
            options += FLAG_PROC_SCREEN;
    }
    return options;
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


    // set up other argument options
    unsigned int options = 0;
    if(argc > 2)
        options = processOptionalArgs(argc-2, &argv[2]);


    // set up the emulator and load the rom
    ALEInterface ale;
    bool disp_screen = options & FLAG_DISP_SCREEN;
    bool proc_screen = options & FLAG_PROC_SCREEN;
    ale.loadROM(rom_file, disp_screen, proc_screen);


    // TODO: see rlglue/examples/skeleton/SkeletonExperiment.c for more info
    // on incorporating RLGlue agent.


    // play 10 episodes
    for(int i=0; i<10; i++)
    {
        float total_reward = 0;

        while(!ale.game_over())
        {
            // TODO - here is a map of all the objects:
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
        }

        cout << "Episode " << (i+1) << ", score = " << total_reward << endl;
        ale.reset_game();
    }
}

