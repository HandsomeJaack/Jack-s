#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v = {1,2,3,2,1};
    std::remove(v.begin(), v.end(),2);
    std::cout << v.size();
}
