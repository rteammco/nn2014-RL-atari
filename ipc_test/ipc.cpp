#include <iostream>
#include <string>

using namespace std;


int main(int argc, char ** argv)
{
    cout << argv[1] << endl;
    string str;
    cin >> str;
    cout << str + str << endl;
    return 0;
}
