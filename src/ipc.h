#ifndef IPC_H
#define IPC_H

#include <string>
#include <vector>


// Protocol message headers
#define MESSAGE_START "<IPC_MSG_BEGIN>"
#define MESSAGE_END "<IPC_MSG_END>"
#define GAME_START "<START_GAME>"
#define GAME_END "<END_GAME>"


// Protocol communication class
class ALEComm {
  private:
    bool enabled;

  public:
    ALEComm(bool enable_comm) : enabled(enable_comm) {}

    void sendMessage(std::string message);
    void sendMessage(std::vector<std::string> lines);

    std::string getMessage();
    int getAction();
    bool getBool();
    bool isGameStarting();
};

#endif
