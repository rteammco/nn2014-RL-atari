/* File: main.cpp
 *
 * Neural Networks, Fall 2014
 *
 * Add documentation here...
 *
 * NOTE: ROM_DIRECTORY has been pre-defined by the Makefile.
 */

#include <iostream>
#include <string>
#include "ale_interface.hpp"

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
    cout << rom_file << endl;


    // set up the emulator and load the rom
    ALEInterface ale;
    ale.loadROM(rom_file.c_str());

    // get vector of legal actions
    ActionVect legal_actions = ale.getLegalActionSet();

    // play 10 episodes
    for(int i=0; i<10; i++)
    {
        float total_reward = 0;
        while(!ale.game_over())
        {
            // choose an action
            int choice = rand() % legal_actions.size();
            Action a = legal_actions[choice];
            
            // apply the action
            float reward = ale.act(a);
            total_reward += reward;
        }

        cout << "Episode " << (i+1) << ", score = " << total_reward << endl;
        ale.reset_game();
    }
}
