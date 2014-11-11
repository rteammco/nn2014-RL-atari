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
#include "rlglue/RL_glue.h"

using namespace std;


bool isSame(IntMatrix &M, IntMatrix &N)
{
    for(int i=0; i<M.size(); i++)
        for(int j=0; j<3; j++)
            if(M[i][j] != N[i][j])
                return false;
    return true;
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
    cout << rom_file << endl;


    /* NOTES:
     * Representation of the screen pixels:
     *   ale.screen_matrix: IntMatrix === vector< vector<int> >
     * State:
     *  ale.game_controller->getState()
     */

    // set up the emulator and load the rom
    ALEInterface ale;
    ale.loadROM(rom_file, false, true);

    // TODO - test only!
    // SEE rlglue/examples/skeleton/SkeletonExperiment.c for more info
    RL_agent_message("sup");
    const char * task_spec;
    task_spec = RL_init();

    // play 10 episodes
    for(int i=0; i<10; i++)
    {
        float total_reward = 0;

        IntMatrix M = ale.screen_matrix;
        IntMatrix N = M;
        cout << M[0][0] << ", " << M[0][1] << endl;
        int same = 0;
        int frames = 0;
        while(!ale.game_over())
        {
            frames++;
            M = N;
            N = ale.screen_matrix;
            if(isSame(M, N))
                same++;

            // choose an action
            int choice = rand() % ale.legal_actions.size();
            Action a = ale.legal_actions[choice];
            
            // apply the action
            float reward = ale.act(a);
            total_reward += reward;
        }

        cout << frames << " frames, " << same << " same." << endl;
        cout << "Episode " << (i+1) << ", score = " << total_reward << endl;
        ale.reset_game();
    }
}
