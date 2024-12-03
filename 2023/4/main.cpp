#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <cmath> //pow

/**
 * AOC 2023 Day 4
 * Hans Elliott
*/
std::vector<int> NWINS_PER_CARD;

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
 * for each 'scratch card', calc the number of random numbers that
 * are winning numbers
*/
int get_nwins(std::string line) {
    std::vector<std::string> splt, wins, yournums;
    std::string numsetstr;
    int nwins = 0;
    // 2 sets of numbers: winning numbers, your numbers
    numsetstr = (stringsplit(line, ": ")).back();
    splt = stringsplit(numsetstr, " | ");
    wins = stringsplit(splt.front(), " ");
    yournums = stringsplit(splt.back(), " ");
    // find intersection - which of your nums is a winning num
    for (std::string num : yournums) {
        if (num.empty()) continue;
        if (std::find(wins.begin(), wins.end(), num) != wins.end()) {
            nwins++;
        }
     }
    return nwins;
}


/**
 * for each card, you get 1 point for a first winning number,
 * and then points double for each winning number after
 * (1, 2, 4, 8, ...).
 * compute total points
*/
int part1() {
    int tot_points = 0;
    for (int& nwins : NWINS_PER_CARD) {
        if (nwins > 0) {
            tot_points += pow(2, nwins - 1);
        }
    }
    return tot_points;
}

/**
 * The number of winning numbers x in a scratch card give you copies of the
 * next x cards. Determine the total number of cards we end up with.
*/
int part2() {
    int result = 0;
    size_t n = NWINS_PER_CARD.size();
    std::vector<int> cards(n, 0);
    size_t i,j;
    // If card i=1 has one winning number, then
    // card j=2 gets hit once.
    // Then we move to card i=2 which has 4 winning numbers,
    // so cards j=3...6 get hit once for each time card i=2 is hit.
    // continue.
    for (i=0; i < n; i++) {
        cards[i]++;
        for (j=i + 1; j < i + NWINS_PER_CARD[i] + 1; j++) {
            cards[j] += cards[i];
        }
    }
    // compute total number of cards that were hit
    for (i=0; i < n; i++) {
        result += cards[i];
    }
    return result;
}


int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Provide filepath\n";
        return 1;
    }
    std::ifstream infile(argv[1]);
    if (!infile) {
        std::cerr << argv[1] << ": file not found\n";
        return 1;
    }

    std::string line;
    while (std::getline(infile, line)) {
        NWINS_PER_CARD.push_back(get_nwins(line));
    }

    std::cout << "part 1 answer = " << part1() << std::endl;
    std::cout << "part 2 answer = " << part2() << std::endl;

    return 0;
}