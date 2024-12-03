#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <unordered_set>

/**
 * AOC 2023 Day 3
 * Hans Elliott
*/

std::vector<std::string> LINES;
size_t N_LINES = 0;

std::vector<std::pair<int, int>> offsets = {
    {-1, 1}, {-1, 0}, {-1, -1},
    {0, -1}, {0, 1},
    {1, -1}, {1, 0}, {1, 1}
};

std::unordered_set<int> adjacent_nums(int row, int col) {
    std::unordered_set<int> part_nums;
    size_t r, c, numstart, numend;
    unsigned char ch;

    for (const auto &it : offsets) {
        r = row + it.first;
        c = col + it.second;
        if (r < 0 || r >= N_LINES)
            continue;
        if (c < 0 || c >= LINES[r].size())
            continue;
        ch = LINES[r][c];
        if (std::isdigit(ch)) {
            numstart = numend = c;
            while (std::isdigit(LINES[r][numstart - 1]))
                numstart--;
            while (std::isdigit(LINES[r][numend + 1]))
                numend++;
            part_nums.insert(
                std::atoi(LINES[r].substr(numstart, numend + 1).c_str())
            );
        }
    }

    return part_nums;
}


int part1() {
    int partnum_sum = 0;
    unsigned char ch;
    std::unordered_set<int> adjacent;

    for (size_t i = 0; i < N_LINES; i++) {
        for (size_t j = 0; j < LINES[i].size(); j++) {
            ch = LINES[i][j];
            // A symbol is any char that's not a number or a period.
            // Any number adjacent to a symbol is a part number.
            // We need the sum of all part numbers.
            if (!std::isdigit(ch) && ch != '.') {
                adjacent = adjacent_nums(i, j);
                for (const int &num : adjacent) {
                    partnum_sum += num;
                }
            }
        }
    }
    return partnum_sum;
}


int part2() {
    int num_prod, gearratio_sum = 0;
    unsigned char ch;
    std::unordered_set<int> adjacent;

    for (size_t i = 0; i < N_LINES; i++) {
        for (size_t j = 0; j < LINES[i].size(); j++) {

            ch = LINES[i][j];
            // An asterik is a gear if it is adjacent to exactly 2 numbers.
            // The gear's "gear ratio" is the product of those 2 numbers.
            // We need the sum of all the gear ratios.
            if (ch == '*') {
                adjacent = adjacent_nums(i, j);
                if (adjacent.size() == 2) {
                    num_prod = 1;
                    for (const int &num : adjacent) {
                        num_prod *= num;
                    }
                    gearratio_sum += num_prod;
                }
            }
        }
    }
    return gearratio_sum;
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

    /**
     * Read all lines of file into vector so that they can be
     * accessed out of order.
    */
    std::string line;
    while (std::getline(infile, line)) {
        line = "." + line + ".";
        std::istringstream iss(line);
        LINES.emplace_back(std::istream_iterator<char>(iss),
                           std::istream_iterator<char>());
    }
    N_LINES = LINES.size();

    std::cout << "part 1 answer = " << part1() << std::endl;
    std::cout << "part 2 answer = " << part2() << std::endl;

    return 0;
}