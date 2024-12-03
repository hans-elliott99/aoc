#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <unordered_map> // hash table

/**
 * AOC 2023 Day 2
 * Hans Elliott
*/


// split string on delimiter into vector of strings
std::vector<std::string> stringsplit(std::string str, std::string delim) {
    std::vector<std::string> result;
    std::string sub;
    size_t delimlen = delim.length();

    size_t pos = str.find(delim);
    while (pos != std::string::npos) {
        sub = str.substr(0, pos);
        result.push_back(sub);
        str.erase(0, pos + delimlen); // remove first match from str (+ delim)
        pos = str.find(delim);
    }
    result.push_back(str); // what's left

    return result;
}

int getval_part1(std::string line) {
    std::vector<std::string> spltvec, game, sets, cubes;
    std::string tmp, color;
    int game_id, fail, n;

    spltvec = stringsplit(line, ": ");
    game = stringsplit(spltvec[0], " ");
    game_id = std::atoi(game.back().c_str());
    sets = stringsplit(spltvec.back(), "; ");

    for (std::string &draw : sets) {
        fail = 0;
        cubes = stringsplit(draw, ", ");
        for (std::string &cube : cubes) {
            spltvec = stringsplit(cube, " ");
            // n cubes
            tmp = spltvec[0];
            tmp.erase(remove_if(tmp.begin(), tmp.end(), isspace), tmp.end());
            n = std::atoi(tmp.c_str());
            // cube color
            color = spltvec[1];
            color.erase(remove_if(color.begin(), color.end(), isspace), color.end());

            if    ((color == "red"   && n > 12)
                || (color == "green" && n > 13)
                || (color == "blue"  && n > 14)) {
                fail = 1;
                break;
            }
        }
        // one set fails, whole game fails
        if (fail == 1) {
            game_id = 0;
            break;
        }
    }
    return game_id;
}



int getval_part2(std::string line) {
    std::vector<std::string> spltvec, game, sets, cubes;
    std::string tmp, color;
    int n;
    int cubepower = 1;
    std::unordered_map<std::string, int> cubedict = {
        {"red", 1},
        {"blue", 1},
        {"green", 1}
    };

    spltvec = stringsplit(line, ": ");
    game = stringsplit(spltvec[0], " ");
    sets = stringsplit(spltvec.back(), "; ");

    for (std::string &draw : sets) {
        cubes = stringsplit(draw, ", ");
        for (std::string &cube : cubes) {
            spltvec = stringsplit(cube, " ");
            // n cubes
            tmp = spltvec[0];
            tmp.erase(remove_if(tmp.begin(), tmp.end(), isspace), tmp.end());
            n = std::atoi(tmp.c_str());
            // cube color
            color = spltvec[1];
            color.erase(remove_if(color.begin(), color.end(), isspace), color.end());
            cubedict[color] = std::max(cubedict[color], n);
        }
    }
    // calculate the "cube power" (product)
    for (auto& it: cubedict) {
        cubepower *= it.second;
    }
    return cubepower;
}


int main() {
    std::ifstream input("input.txt");

    int total1 = 0;
    int total2 = 0;

    std::string line;
    while (std::getline(input, line)) {

        // sum of the game IDs which are possible according to the rules
        total1 += getval_part1(line);

        // total "cube product" of each game
        total2 += getval_part2(line);
    }

    std::cout << "part 1 total = " << total1 << std::endl;
    std::cout << "part 2 total = " << total2 << std::endl;

    return 0;
}