#include <string>
#include <iostream>
#include <algorithm>

namespace apple {

    void print(const std::string& text)
    {
        std::cout<< text<< std::endl;
    }
}

namespace orange {
    void print(const char* text)
    {
        std::string temp = text;
        std::reverse(temp.begin(), temp.end());
        std::cout<<temp<<std::endl;
    }
}
 using namespace apple;
 using namespace orange;

int main()
{
    print("Hello");
    apple::print("Hello");
    orange::print("Hello");
    return 0;
}
