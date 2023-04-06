#include <string>

class RLAgent
{
    public:
    int reward;
    int move=4;
    int getMove()
    {
        //implement policy here.
        move++;
        return (move%7)+1;
    }
    void setReward(int x)
    {
        reward=x;
    }
};