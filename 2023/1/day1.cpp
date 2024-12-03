#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>


/** AOC 2023 Day 1
 * Hans Elliott
*/

std::vector<std::string> NUMBER = {"zero",  "0",
                                   "one",   "1",
                                   "two",   "2",
                                   "three", "3",
                                   "four",  "4",
                                   "five",  "5",
                                   "six",   "6",
                                   "seven", "7",
                                   "eight", "8",
                                   "nine",  "9"};

/**
 * if its a digit, just return it. if its a spelled digit, convert it to digit
*/
int intfromstr(std::string numstr) {
    unsigned char first = numstr[0];
    if (std::isdigit(first)) {
        return std::atoi(numstr.c_str());
    }

    int index;
    auto it = std::find(NUMBER.begin(), NUMBER.end(), numstr);
    if (it != NUMBER.end()) {
        index = it - NUMBER.begin();
    } else {
        // shouldn't be reachable
        std::cerr << numstr << ": number not found in NUMBER\n";
        std::exit(1);
    }

    return index / 2;
}

/*
 * search across string, 1 char at a time, to extract all digits (1...9)
*/
int mapnum_part1(std::string str) {
    std::vector<int> nums;
    size_t nchar = str.size();
    std::string sub;

    for (size_t i=0; i < nchar; i++) {
        sub = str.substr(i, 1);
        if (std::isdigit(str[i])) {
            nums.push_back(std::atoi(sub.c_str()));
        }
    }
    if (nums.empty())
        return 0;
    return nums.front() * 10 + nums.back();
}

/*
 * search from char i to the char that is j chars away until a digit (e.g., 1)
 * or spelled digit (e.g., one) is found,
 * or until the end of the string is reached
*/
int mapnum_part2(std::string str) {
    std::vector<int> nums;
    std::string sub;
    size_t nchar = str.size();

    for (size_t i=0; i < nchar; i++) {
        for (size_t j=0; j < nchar + 1 - i; j++) {
            sub = str.substr(i, j); //pos, len
            if (std::find(NUMBER.begin(), NUMBER.end(), sub) != NUMBER.end()) {
                nums.push_back(intfromstr(sub));
                break;
            }
        }
    }
    if (nums.empty())
        return 0;
    return nums.front() * 10 + nums.back();
}


int main() {
    std::ifstream input("day1.txt");

    int total1 = 0;
    int total2 = 0;

    std::string line;
    while (std::getline(input, line)) {
        total1 += mapnum_part1(line);
        total2 += mapnum_part2(line);
    }

    std::cout << "part 1 total = " << total1 << std::endl;
    std::cout << "part 2 total = " << total2 << std::endl;

    return 0;
}