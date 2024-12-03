#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iterator>
#include <cmath>

/**
 * AOC 2023 Day 6
 * Hans Elliott
*/

std::vector<std::string> LINES;

// split string on delimiter into vector of sub-strings
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

/**
 * How the boat races work:
 * Given t seconds to race, if you hold your button down for
 * j ms, then you will move at j mm/ms for the remaining time (t-j).
 * Any value of j that results in a distance ((t-j)*j) greater than the record
 * counts as a win for us.
*/

// for each race we have the length of the race and the distance record.
// we need the number of ways to beat the distance record for each race,
// and then to multiply them to get final answer
int part1() {
    std::vector<int> times, dists;
    std::vector<std::string> splt;
    // parse times
    splt = stringsplit(LINES.front(), " ");
    for (auto& s : splt) {
        s.erase(remove_if(s.begin(), s.end(), isspace), s.end());
        if (s.compare("") == 0 || !std::isdigit(s.c_str()[0])) {
            continue;
        }
        times.push_back(std::stoi(s));
    }
    // parse dists
    splt = stringsplit(LINES.back(), " ");
    for (auto& s : splt) {
        s.erase(remove_if(s.begin(), s.end(), isspace), s.end());
        if (s.compare("") == 0 || !std::isdigit(s.c_str()[0])) {
            continue;
        }
        dists.push_back(std::stoi(s));
    }
    // solve the problem - for each race, how many ways to win?
    int tot = 1, wincnt, t, d, i, j;
    for (i=0; i < (int)times.size(); i++) {
        t = times[i];
        d = dists[i];
        wincnt = 0;
        for (j=1; j < t; j++) {
            //  dist traveled = (ms spent racing) * (dist per ms)
            if (((t - j) * j) > d) {
                wincnt++;
            }
        }
        tot *= wincnt;
    }
    return tot;
}

// now we combine all the race time numbers into one race time
// and all the distance numbers into one distance,
// and proceed the same for the single *long* race
int brute_part2() {
    std::string timestr = "", diststr = "";
    long time, dist;
    std::vector<std::string> splt;
    // parse times
    splt = stringsplit(LINES.front(), " ");
    for (auto& s : splt) {
        s.erase(remove_if(s.begin(), s.end(), isspace), s.end());
        if (s.compare("") == 0 || !std::isdigit(s.c_str()[0])) {
            continue;
        }
        timestr += s;
    }
    time = std::stol(timestr);
    // parse dists
    splt = stringsplit(LINES.back(), " ");
    for (auto& s : splt) {
        s.erase(remove_if(s.begin(), s.end(), isspace), s.end());
        if (s.compare("") == 0 || !std::isdigit(s.c_str()[0])) {
            continue;
        }
        diststr += s;
    }
    dist = std::stol(diststr);
    // solve
    long wincnt = 0, j;
    for (j = 1; j < time; j++) {
        if ((time - j) * j > dist)
            wincnt++;
    }
    return wincnt;
}

/**
 * Can solve this problem better, using some math...
 * Didn't think of this, but its a neat solution.
 * We have control over the pressTime, and we want to solve the following
 * (since we travel pressTime m/s for the remaining s to race):
 *   (raceTime - pressTime) * pressTime > distRecord
 *   = (raceTime * pressTime) - (pressTime)^2 > distRecord
 *   = -(pressTime)^2 + raceTime*pressTime - distRecord > 0
 *  i.e., ax^2 + bx + c > 0...
 * so we can use the quaratic formula to solve for pressTime on the LHS:
 *   pressTime = [-raceTime +/- sqrt(raceTime^2 - 4(-1)(-dist)] / 2(-1)
 *   pressTime = [raceTime +/- sqrt(raceTime^2 - 4dist)] / 2
 * Which gives us a lower and upper bound on raceTimes that satisfy the
 * inequality - just what we need to get the length of the range of winning
 * pressTimes.
 * 
 * part 2 done smarter:
*/
int part2() {
    std::string timestr = "", diststr = "";
    long time, dist;
    std::vector<std::string> splt;
    // parse times
    splt = stringsplit(LINES.front(), " ");
    for (auto& s : splt) {
        s.erase(remove_if(s.begin(), s.end(), isspace), s.end());
        if (s.compare("") == 0 || !std::isdigit(s.c_str()[0])) {
            continue;
        }
        timestr += s;
    }
    time = std::stol(timestr);
    // parse dists
    splt = stringsplit(LINES.back(), " ");
    for (auto& s : splt) {
        s.erase(remove_if(s.begin(), s.end(), isspace), s.end());
        if (s.compare("") == 0 || !std::isdigit(s.c_str()[0])) {
            continue;
        }
        diststr += s;
    }
    dist = std::stol(diststr);
    // solve
    long lower = std::ceil(time  - std::sqrt(time*time - 4*dist)) / 2;
    long upper = std::floor(time + std::sqrt(time*time - 4*dist)) / 2;
    return upper - lower + 1;
}





int main(int argc, char* argv[]) {
    // input
            if (argc < 2) {
                std::cerr << "Provide filepath\n";
                return 1;
            }
            std::ifstream infile(argv[1]);
            if (!infile) {
                std::cerr << argv[1] << ": file not found\n";
                return 1;
            }
    ////////////////////////////////////////////////////////////////////////
    std::string line;
    while (std::getline(infile, line)) {
        LINES.push_back(line);
    }
    std::cout << "part 1 answer:\n" << part1() << std::endl;
    std::cout << "part 2 answer:\n" << part2() << std::endl;

    return 0;
}